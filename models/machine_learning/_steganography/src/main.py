from pathlib import Path
from PIL import Image
import numpy as np

img_folder = Path(__file__).parent.parent / "data/input"
output_folder = Path(__file__).parent.parent / "data/output"


def extract_lsb_bits(image_path: Path) -> list[int]:
    """Return every channel LSB as a flat bit list."""
    img = Image.open(image_path).convert("RGB")
    arr = np.array(img)
    return (arr & 1).flatten().tolist()
 
 
def bits_to_int(bits: list[int]) -> int:
    """Interpret bits (MSB first) as an unsigned integer."""
    result = 0
    for b in bits:
        result = (result << 1) | b
    return result
 
 
def bits_to_text(bits: list[int]) -> str:
    """Convert bit list to ASCII string (8 bits per char, MSB first)."""
    chars: list[str] = []
    for i in range(0, len(bits) - 7, 8):
        byte_val = bits_to_int(bits[i:i + 8])
        if byte_val == 0:
            break
        chars.append(chr(byte_val))
    return "".join(chars)
 

def decode_text(image_path: Path) -> str | None:
    """
    Decode a text message with header [0, 0].
        bits 0-1:marker [0, 0]
        bits 2-17:payload length in bits (16-bit)
        bits 18+:ASCII payload
    """
    bits = extract_lsb_bits(image_path)
 
    payload_len = bits_to_int(bits[2:18])
    available   = len(bits) - 18
    if payload_len > available:
        payload_len = available
 
    return bits_to_text(bits[18: 18 + payload_len])
 
 
def decode_binary_image(image_path: Path, out_path: Path) -> None:
    """
    Decode a hidden binary image with header [1, 0].
        bits 0-1: marker [1, 0]
        bits 2-17:  image width  (16-bit)
        bits 18-33: image height (16-bit)
        bits 34+: raw pixel bits (0 or 1), mapped to 0 or 255
    Saves the result to out_path.
    """
    bits = extract_lsb_bits(image_path)
 
    width  = bits_to_int(bits[2:18])
    height = bits_to_int(bits[18:34])
    print(f"  Hidden image dimensions: {width} x {height} px")
 
    pixel_bits = bits[34: 34 + width * height]
 
    pixel_values = np.array(pixel_bits, dtype=np.uint8) * 255
    hidden_img   = Image.fromarray(pixel_values.reshape(height, width), mode="L")
    hidden_img.save(out_path)
    print(f"  Saved hidden image to: {out_path}")


def task_0():
    images = [
        img_folder / "black.png",
        img_folder / "contrast.png",
        img_folder / "natural.png",
    ]

    for img_path in images:
        message = decode_text(img_path)
        
        print(f"{message}")


def task_1():
    img_path = img_folder / "cat.png"
    message = decode_text(img_path)
    print(f"{message}")


def task_2():
    img_path = img_folder / "butterfly.png"
    output_img = output_folder / "output.png"
    decode_binary_image(img_path, output_img)


def main():
    print("--- Task 0 ---")
    task_0()
    print("")
    print("--- Task 1 ---")
    task_1()
    print("")
    print("--- Task 2 ---")
    task_2()
    print("")


if __name__ == "__main__":
    main()
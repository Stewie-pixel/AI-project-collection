## Hidden in Plain Sight — LSB Steganography Decoder
Solution for the Stack Overflow Coding Challenge #18 — May 2026.
Decodes messages hidden in images using Least Significant Bit (LSB) steganography.

### How it works
Each pixel in an image has three colour channels (R, G, B), each stored as 8 bits. By replacing the least significant bit of each channel with message data, information can be hidden without any visible change to the image.
The decoder reads those LSBs pixel by pixel, row by row, and reconstructs the hidden content — either an ASCII text message or a binary image.

### Project structure
```
steganography/
├── data/
│   ├── input/          # Source images (task0_*.png, cat.png, butterfly.png)
│   └── output/         # Decoded output images written here
├── src/
│   └── main.py         # Decoder — run this
├── pyproject.toml
├── uv.lock
└── README.md
```

### Setup
Requires uv.
```
bashuv sync
```

Usage
```
bashuv run src/main.py
```

Expected output:
```
--- Task 0 ---
  task0_black.png:    'Test Test Test Test Test...' (...)
  task0_contrast.png: 'Test Test Test Test Test...' (...)
  task0_natural.png:  'Test Test Test Test Test...' (...)

--- Task 1 ---
  The first part of the sentence is "Three may keep a secret, ...". ...

--- Task 2 ---
  Hidden image dimensions: W x H px
  Saved hidden image to: data/output/task2_hidden.png
```
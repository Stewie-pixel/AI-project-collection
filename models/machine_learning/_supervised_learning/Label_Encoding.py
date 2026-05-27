from sklearn import preprocessing

# Label Encoding
label_encoder = preprocessing.LabelEncoder()

labels = ['helium', 'hydrogen', 'oxygen', 'nitrogen']

label_encoder.fit(labels)
print("\nClass mapping: ")
for i, item in enumerate(label_encoder.classes_):
    print(f"{item}: {i}")

encoded_labels = label_encoder.transform(['hydrogen', 'oxygen'])
print("\nEncoded labels: ", encoded_labels)
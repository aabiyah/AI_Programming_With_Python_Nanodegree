import os

def get_pet_labels(image_dir):
    results = {}
    for filename in os.listdir(image_dir):
        if filename[0] != ".":
            label = ' '.join([word.lower() for word in filename.split('_') if word.isalpha()])
            results[filename] = [label]
    return results

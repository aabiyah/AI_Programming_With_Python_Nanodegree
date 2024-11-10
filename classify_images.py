from classifier import classifier

def classify_images(images_dir, results, model):
    for filename, label in results.items():
        image_path = images_dir + filename
        classifier_label = classifier(image_path, model).lower().strip()
        match = 1 if label[0] in classifier_label else 0
        results[filename].extend([classifier_label, match])

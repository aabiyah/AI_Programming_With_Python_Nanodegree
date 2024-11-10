def adjust_results4_isadog(results, dogfile):
    with open(dogfile, 'r') as f:
        dog_names = {line.strip().lower() for line in f}
        
    for filename, attributes in results.items():
        pet_label_is_dog = 1 if attributes[0] in dog_names else 0
        classifier_label_is_dog = 1 if attributes[1] in dog_names else 0
        results[filename].extend([pet_label_is_dog, classifier_label_is_dog])

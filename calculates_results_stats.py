def calculates_results_stats(results):
    stats = {'n_images': len(results), 'n_dogs_img': 0, 'n_notdogs_img': 0,
             'n_correct_dogs': 0, 'n_correct_notdogs': 0, 'n_correct_breed': 0}
    
    for key, value in results.items():
        is_dog = value[3]
        is_correct = value[2]
        
        if is_dog:
            stats['n_dogs_img'] += 1
            if value[3] == value[4]:
                stats['n_correct_dogs'] += 1
            if is_correct:
                stats['n_correct_breed'] += 1
        else:
            stats['n_notdogs_img'] += 1
            if value[3] == value[4]:
                stats['n_correct_notdogs'] += 1
                
    stats['pct_correct_dogs'] = (stats['n_correct_dogs'] / stats['n_dogs_img']) * 100
    stats['pct_correct_breed'] = (stats['n_correct_breed'] / stats['n_dogs_img']) * 100
    stats['pct_correct_notdogs'] = (stats['n_correct_notdogs'] / stats['n_notdogs_img']) * 100 if stats['n_notdogs_img'] > 0 else 0
    return stats

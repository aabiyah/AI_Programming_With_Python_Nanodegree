def print_results(results, results_stats, model, print_incorrect_dogs=False, print_incorrect_breed=False):
    print("\n\n*** Results Summary for Model Architecture", model.upper(), "***")
    print("N Images:", results_stats['n_images'])
    print("N Dog Images:", results_stats['n_dogs_img'])
    print("N Not-Dog Images:", results_stats['n_notdogs_img'])
    
    print("\nPercentage of Correct Dogs:", results_stats['pct_correct_dogs'])
    print("Percentage of Correct Breed Matches:", results_stats['pct_correct_breed'])
    print("Percentage of Correct 'Not-a-Dog':", results_stats['pct_correct_notdogs'])
    
    if print_incorrect_dogs:
        print("\nIncorrect Dog Classifications:")
        for filename, result in results.items():
            if sum(result[3:]) == 1:  # one of the labels is dog but not both
                print("Real:", result[0], "Classifier:", result[1])
    
    if print_incorrect_breed:
        print("\nIncorrect Breed Classifications:")
        for filename, result in results.items():
            if sum(result[3:5]) == 2 and result[2] == 0:  # both labels are dog but incorrect breed
                print("Real:", result[0], "Classifier:", result[1])

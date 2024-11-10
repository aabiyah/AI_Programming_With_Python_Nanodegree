from time import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    start_time = time()
    
    # Get input arguments
    in_arg = get_input_args()
    
    # Create pet image labels
    results = get_pet_labels(in_arg.dir)
    
    # Classify images and add classifier labels to results
    classify_images(in_arg.dir, results, in_arg.arch)
    
    # Adjust results to indicate if labels are dogs or not
    adjust_results4_isadog(results, in_arg.dogfile)
    
    # Calculate results statistics
    results_stats = calculates_results_stats(results)
    
    # Print results
    print_results(results, results_stats, in_arg.arch, True, True)
    
    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:", 
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":" + str(int((tot_time % 3600) % 60)))

if __name__ == "__main__":
    main()

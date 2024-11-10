import argparse

def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/', help='Directory with images')
    parser.add_argument('--arch', type=str, default='vgg', help='Model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='File with dog names')
    return parser.parse_args()

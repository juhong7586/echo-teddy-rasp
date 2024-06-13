import argparse
from matrix import draw_smiley, draw_sad_face

if __name__ == "__main__":
    # create matrix device
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    

    args = parser.parse_args()

    try: 
        draw_smiley(args.cascaded)
        draw_sad_face(args.cascaded)

    except KeyboardInterrupt:
        pass
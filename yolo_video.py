import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    # parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    # '''
    # Command line options
    # '''
    # parser.add_argument(
    #     '--model', type=str,
    #     help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    # )
    #
    # parser.add_argument(
    #     '--anchors', type=str,
    #     help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    # )
    #
    # parser.add_argument(
    #     '--classes', type=str,
    #     help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    # )
    #
    # parser.add_argument(
    #     '--gpu_num', type=int,
    #     help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    # )
    #
    # parser.add_argument(
    #     '--image', default=False, action="store_true",
    #     help='Image detection mode, will ignore all positional arguments'
    # )
    # '''
    # Command line positional arguments -- for video detection mode
    # '''
    # parser.add_argument(
    #     "--input", nargs='?', type=str,required=False,default='./path2your_video',
    #     help = "Video input path"
    # )
    #
    # parser.add_argument(
    #     "--output", nargs='?', type=str, default="",
    #     help = "[Optional] Video output path"
    # )
    #
    # FLAGS = parser.parse_args()
    #
    # if FLAGS.image:
    #     """
    #     Image detection mode, disregard any remaining command line arguments
    #     """
    #     print("Image detection mode")
    #     if "input" in FLAGS:
    #         print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
    #     detect_img(YOLO(**vars(FLAGS)))
    # elif "input" in FLAGS:
    #     detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    # else:
    #     print("Must specify at least video_input_path.  See usage with --help.")

    test_file = "VOCdevkit/VOC2007/ImageSets/Main/trainval.txt"
    path = "VOCdevkit/VOC2007/JPEGImages/"
    save_path = "VOCdevkit/VOC2007/Test2/"

    yolo_test_args = {
        "model_path": 'logs/000/trained_weights_final3.h5',
        "anchors_path": 'model_data/yolo_anchors.txt',
        "classes_path": 'model_data/voc_classes.txt',
        "score": 0.3,
        "iou": 0.45,
        "model_image_size": (160, 320),
        "gpu_num": 1,
    }

    yolo_test = YOLO(**yolo_test_args)
    with open(test_file, "r", encoding="utf-8") as f:
        files = f.readlines()
        for file in files:
            image_file = path + file.strip() + ".jpg"
            image = Image.open(image_file)
            r_image = yolo_test.detect_image(image)
            r_image.save(save_path+file.strip()+".jpg")

    yolo_test.close_session()
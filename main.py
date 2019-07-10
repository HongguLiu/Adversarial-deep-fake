import os
import argparse
import utils
'''
	Advesarial video generate application.
	Author: Honggu Liu
	Date: July, 10, 2019
'''

'''
	This is a adversarial videos generating application. Please reading the instruction carefully.
	First, you must downdload our trained XceptionNet model and save the picklefile at ./models.
	Second, we suggest you make a directory like ours test_video to save original videos.
	Then, we make a default output directory named adv_videos.
	Finally, you can run this app with command 'python main'.

	Of course, you can use your own parameters in the function.
	The example is:
	python main --video_path='input_path' --model_path='./models/best_xception_c40_full.pkl' --output_path='output_path'
	Thanks for your support of our recently works. If any questions, you can contact with us. Email: lhg9754@mail.ustc.edu.cn
'''



if __name__ == '__main__':
	parse = argparse.ArgumentParser(
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parse.add_argument('--video_path', type=str, default='./test_video', help="This is input videos's directory.")
	parse.add_argument('--model_path', type=str, default='./models/best_xception_c40_full.pkl', help="The trained detection model's path.")
	parse.add_argument('--output_path', type=str, default='./adv_videos/', help="The output path.")
	args = parse.parse_args()
	utils.generate(**vars(args))
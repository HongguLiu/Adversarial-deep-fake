# Adversarial-deep-fake
A project to generate adversarial video to resist detection of XceptionNet
## Description
This is a implemention to resist FaceForensics of CNNs, we have successfully attacked XceptionNet and MesoNet, 
and the follow-up work is black-box attack.
## Requirements
You will need following to run above:
* python 3.5.6
* pytorch 1.1.0
* torchvison 0.2.2
* advertorch 0.1.2
* opencv-python
* pillow
* tqdm

We suggest you install all dependence by two step:
1. `conda install pytorch torchvision cudatoolkit=9.0 -c pytorch`:install pytorch and torchvision for GPU version(CPU version is allowed)
2. `pip install -r requirements`:install all dependence.
## Model
For XceptionNet, we have two pretrained models for DeepFakes and Face2Face:
* DeepFakes pretrained detection [model](https://drive.google.com/open?id=1vX4rE1zpTQxZYP7ZnrxMu0fbLeuNUmmZ)
* Face2Face pretrained detection [model](https://drive.google.com/open?id=1yp3N-_HXL_MkgWLUpvmDfbfng3XI2pvw)

After downloaded pretrained models, you should make a directory named models and move all models to this directory.

## Generate adversarial videos
`python main.py --video_path='./test_video' --model_path='./models/xxx.pkl' --output_path='./adv_videos'`
* `--video_path`: path to original videos
* `--model_path`: path to pretrained models
* `--output_path`: path to output videos

## Experiments

 |                      |classification accuracy | 
 |:--------------------:|:----------------------:|
 |    Original videos   |        95.50%          |
 |  Adversarial videos  |        19.76%          |
 
## License
The provided implementation is strictly for academic purposes only. Should you be interested in using our technology for any commercial use, 
please feel free to contact us.

## Acknowledgement
The code benefits from outstanding prior work and theirs implementations including:
- [FaceForensics++ Learning to Detect Manipulated Facial Images](https://arxiv.org/pdf/1901.08971.pdf) 
Andreas Rössler *et al.* ([code](https://github.com/ondyari/FaceForensics))
- [advertorch v0.1: An Adversarial Robustness Toolbox based on PyTorch](https://arxiv.org/pdf/1902.07623v1.pdf) 
by Ding *et al.* ([code](https://github.com/BorealisAI/advertorch)) 

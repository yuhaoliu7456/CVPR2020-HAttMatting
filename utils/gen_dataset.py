
# -*- coding: utf-8 -*-
# File   : gen_dataset.py
# Author : Yuhao Liu
# Email  : yuhaoLiu7456@gmail.com
# Date   : 07/04/2020
# 
# This file is part of HAttMatting.
# https://github.com/wukaoliu/CVPR2020-HAttMatting
# Distributed under MIT License.

"""
The following is an example of generating test images.
While for the composition of training dataset, you need do some modification.
1. for the Adobe composition-1K: modify the num_bgs from 20 to 100; 
   for our Distinctions-646: modify the num_bgs from 20 to 80;
2. load fg_train.txt and bg_train.txt to replace the test files.
3. modify the original_path and saving_path
   For example(for Adobe datasets):
        fg_path = './Train_ori/Fg_images/'            
        a_path = './Train_ori/Alpha_matte/'
        bg_path = './COCO/'
        
        out_img_path = './Train/Image/'
        out_gt_path  = './Train/GT/'
        out_fg_path  = './Train/FG/' 
        out_bg_path  = './Train/BG/'
        
4. The most important thing is to create the corresponding data set in advance.

"""


import os 
import math
import cv2
import torch
import numpy as np
from PIL import Image

# for configuring original fg, mattes, bg
fg_path = './Test_ori/Fg_images/'            
a_path = './Test_ori/Alpha_matte/'
bg_path = './VOCdevkit/VOC2012/JPEGImages/'

# out_* for saving various images
out_img_path = './Test/Image/'
out_gt_path  = './Test/GT/'
out_fg_path  = './Test/FG/'
out_bg_path  = './Test/BG/'
def composite(fg, bg, a, w, h):
    bg = bg[0:w, 0:h] 
    bg = torch.from_numpy(bg).transpose(0, 2).double()
    fg = torch.from_numpy(fg).transpose(0, 2).double()
    alpha = torch.from_numpy(a).transpose(0, 1).double() /255
    composite_img = alpha * fg + (1 - alpha) * bg
    composite_img = composite_img.int()
    composite_img = composite_img.transpose(0, 2).numpy()

    return composite_img


num_bgs = 20
fg_files = [line.rstrip('\n') for line in open('./fg_test.txt')]
bg_files = [line.rstrip('\n') for line in open('/bg_test.txt')]

bg_iter = iter(bg_files)
index = 0
for im_name in fg_files:
    im = cv2.imread(os.path.join(fg_path, im_name))
    a = cv2.imread(os.path.join(a_path , im_name), cv2.IMREAD_GRAYSCALE)

    bbox = im.shape
    w = bbox[0]
    h = bbox[1]
    
    bcount = 0 
    for i in range(num_bgs):

        bg_name = next(bg_iter)        
        bg = cv2.imread(os.path.join(bg_path , bg_name))
        bg_bbox = bg.shape
        bw = bg_bbox[0]
        bh = bg_bbox[1]
        wratio = w / bw
        hratio = h / bh
        ratio = wratio if wratio > hratio else hratio     
        if ratio > 1:     
            # cv2--->PIL--->cv2 for keep the same. Since the resize of PIL and the resize of cv2 is different
            bg = Image.fromarray(cv2.cvtColor(bg,cv2.COLOR_BGR2RGB))
            bg = bg.resize((math.ceil(bh*ratio),math.ceil(bw*ratio)), Image.BICUBIC)
            bg = cv2.cvtColor(np.asarray(bg),cv2.COLOR_RGB2BGR)            
        
        out = composite(im, bg, a, w, h)
        cv2.imwrite(out_img_path  +im_name.split('_')[0] + '_' + str(index) + '.png', out) # +'train_img_'
        gt = a
        cv2.imwrite(out_gt_path + im_name.split('_')[0] + '_' + str(index) + '.png', gt) #  +'train_gt_'
        
        bf_for_save = bg[0:w, 0:h]
        cv2.imwrite(out_bg_path  +im_name.split('_')[0] + '_' + str(index) + '.png', bf_for_save)
        cv2.imwrite(out_fg_path  +im_name.split('_')[0] + '_' + str(index) + '.png', im)
        
        print(out_gt_path +im_name.split('_')[0] + '_' + str(index) + '.png' + '-----%d' %index)
        index += 1





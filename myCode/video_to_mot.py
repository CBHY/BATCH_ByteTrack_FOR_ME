import cv2
import numpy as np
import PIL
import sys
import os
import configparser

pwd = os.getcwd()


# 동영상을 Frame Image로 변환
for tt in ['train','test']:
    list_dir = os.listdir(f'./{tt}')
    for dir in list_dir:
        seq = os.path.join(pwd, tt ,dir)
        video_path = seq+f'\\'+str(dir)+'.mp4'
        # print(video_path)
        cap = cv2.VideoCapture(video_path)
        frame = 1
        if os.path.isdir(seq+'\img1'):
            pass
        else:
            os.mkdir(seq+'\img1')
        if cap.isOpened():
            while True:
                ret, image = cap.read()
                if ret:
                    cv2.imwrite(seq+'\\img1\\'+str(frame).zfill(6)+'.jpg', image)
                    print('finish : ', seq+'\\img1\\'+str(frame).zfill(6)+'.jpg')
                    frame+=1
                else:
                    break
                


# seqinfo.ini 생성
for tt in ['train','test']:
    list_dir = os.listdir(f'./{tt}')
    for dir in list_dir:

        seq = os.path.join(pwd, tt ,dir)        
        video_path = seq+f'\\'+str(dir)+'.mp4'
        cap = cv2.VideoCapture(video_path)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        
        ini_path = seq+f'\\'
        WriteINI = configparser.ConfigParser()
        WriteINI['Sequence'] = {}
        WriteINI['Sequence']['name'] = str(dir)        
        WriteINI['Sequence']['imDir'] = 'img1'        
        WriteINI['Sequence']['frameRate'] = str(int(fps))
        WriteINI['Sequence']['seqLength'] = str(int(frame_count))
        WriteINI['Sequence']['imWidth'] = str(int(width))
        WriteINI['Sequence']['imHeight'] = str(int(height))
        WriteINI['Sequence']['imExt'] = '.jpg'
        
        read = 0
        with open(f'{seq}/seqinfo.ini','w') as configfile:
            WriteINI.write(configfile)
        with open(f'{seq}/seqinfo.ini','r') as configfile:
            read = configfile.read()
            read = read.replace(' ', '')
        with open(f'{seq}/seqinfo.ini','w') as configfile:
            configfile.write(read)

# 가짜 detection 정보, 가짜 GT 생성(MOT Form에서 COCO Format으로 변경하는 함수에서 이를 요구)
for tt in ['train','test']:
    list_dir = os.listdir(f'./{tt}')
    for dir in list_dir:
        seq = os.path.join(pwd, tt ,dir)
        if tt == 'train':
            if os.path.isdir(seq+'\det'):
                pass
            else:
                os.mkdir(seq+'\det')
                
            if os.path.isdir(seq+'\gt'):
                pass
            else:
                os.mkdir(seq+'\gt')
            
            with open(f'{seq}/det/det.txt','w') as f:
                f.write('1,-1,1,1,1,1,1,-1,-1,-1')
            with open(f'{seq}/gt/gt.txt','w') as f:
                f.write('1,1,1,1,1,1,1,1,1')
        
        else:
            if os.path.isdir(seq+'\det'):
                pass
            else:
                os.mkdir(seq+'\det')
                
            with open(f'{seq}/det/det.txt','w') as f:
                f.write('1,-1,1,1,1,1,1,-1,-1,-1')


# 동영상 파일 이동





# MOT FORM TO COCO



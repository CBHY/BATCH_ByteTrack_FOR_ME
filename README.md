# BATCH_ByteTrack_FOR_ME
python tools/track.py -f exps/example/mot/dataset_MTMC_arranged_exps.py -c pretrained/bytetrack_x_mot20.tar -b 1 -d 1 --fp16 --fuse --match_thresh 0.7

윈도우에서 돌리는거면,  
원래 bytetrack repository에 있는 내용으로 설치가 불가능한 경우가 있음  
1. cython 설치, pycocotools 설치는 conda 버전으로 진행 
2. cython-bbox는 cython-bbox로 설치 진행


사용법

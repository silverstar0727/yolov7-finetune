### 출처
- 모델
  - [원본 yolov7 repository](https://github.com/WongKinYiu/yolov7)
  - [YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors](https://arxiv.org/abs/2207.02696)
- 데이터
  - [kaggle mask detection](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection)


도커 실행
```
docker run \
--name yolov7 \
-it -d --rm \
-v /home/ubuntu/yolov7-finetune:/yolov7 \
--ipc=host \
--gpus all \
nvcr.io/nvidia/pytorch:21.08-py3

docker exec -it yolov7 /bin/bash
```

필요한 패키지 설치
```
apt update
apt install -y zip htop screen libgl1-mesa-glx

pip install seaborn thop boto3
```

데이터 다운로드 및 전처리 (aws 인증 필요)
```
cd /yolov7
python download_data.py
python xml_to_yolo.py
python split_yolo_data.py
```

모델 다운로드 및 학습 진행
```
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt

python yolov7/train.py \
--workers 8 \
--device 0 \
--batch-size 16 \
--data yolov7/data/coco.yaml \
--img 640 640 \
--cfg yolov7/cfg/training/yolov7.yaml \
--weights yolov7.pt \
--name yolov7 \
--hyp yolov7/data/hyp.scratch.p5.yaml
```
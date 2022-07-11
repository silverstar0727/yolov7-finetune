```
docker run \
--name yolov7 \
-it -d --rm \
-v /home/ubuntu/yolov7-finetune:/yolov7 \
--ipc=host \
--gpus all \
nvcr.io/nvidia/pytorch:21.08-py3
```

```
docker exec -it yolov7 /bin/bash

# apt install required packages
apt update
apt install -y zip htop screen libgl1-mesa-glx

# pip install required packages
pip install seaborn thop boto3

cd /yolov7
python download_data.py
python xml_to_yolo.py
python split_yolo_data.py

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
```
docker run \
--name yolov7 \
-it -d \
-v /workspace:/home/ubuntu/yolov7-finetune \
--ipc=host \
nvcr.io/nvidia/pytorch:21.08-py3
```

```
docker exec -it yolov7 /bin/bash

# apt install required packages
apt update
apt install -y zip htop screen libgl1-mesa-glx

# pip install required packages
pip install seaborn thop

cd /workspace
python download_data.py
python xml_to_yolo.py
python split_yolo_data.py

python /content/yolov7/train.py \
--workers 8 \
--device 0 \
--batch-size 16 \
--data /content/yolov7/data/coco.yaml \
--img 640 640 \
--cfg /content/yolov7/cfg/training/yolov7.yaml \
--weights /content/yolov7.pt \
--name yolov7 \
--hyp /content/yolov7/data/hyp.scratch.p5.yaml
```

#模型训练
#python train.py --data data/CB_UAV.yaml --epochs 100 --weights weights --cfg models/yolov5s.yaml  --batch-size 64
#python train.py --data data/CB_UAV.yaml --epochs 100 --weights weights --cfg models/yolov5s_C3Ghost.yaml  --batch-size 64
# python train.py --data data/CB_UAV.yaml --epochs 1 --weights weights --cfg models/yolov5s_C3Ghost_SimAM.yaml  --batch-size 64
#python train.py --data data/CB_UAV.yaml --epochs 100 --weights weights --cfg models/yolov5s_C3Ghost_SMFA.yaml  --batch-size 64
#模型检测
python detect.py $PREFIX --source /media/user/新加卷1/data/YOLO/YOLO/yolo_UAV/datasets/CB_UAV/test --weights weights/yolov5.pt --conf 0.6





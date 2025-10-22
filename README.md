

## <div align="center">A lightweight feature enhancement model for UAV detection in real-world scenarios</div>
•	We release RWSD, a large-scale UAV detection dataset of 14,592 real-world images covering diverse backgrounds, UAV sizes, and viewpoints to benchmark robust detectors.

•	We present a lightweight feature enhancement model (LFEM) tailored for UAV detection and Extensive experimental results demonstrate the effectiveness and ef-ficiency of our approach.

## <div align="left">Introduction</div>

<div style="font-weight: bold;">Abstract: </div>Real-time Unmanned Aerial Vehicle (UAV) detection is a growing research field centered on advanced computer vision and deep learning algorithms. However, the rise of un-manned aerial vehicles (UAVs) has sparked numerous concerns due to their potential for malicious use in illegal activities. To address these concerns, Vision-based object detec-tion approaches for UAVs have recently been developed. Nonetheless, UAV detection in real-world scenarios, such as images with diverse backgrounds and various perspectives, remains underexplored. To fill this gap, we present a new UAV detection dataset called the real-world scenarios dataset (RWSD). This dataset leverages real-world footage and is constructed under challenging conditions, including complex backgrounds, varying UAV sizes, different perspectives, and multiple UAV types. It aims to support the de-velopment of robust UAV detection algorithms that can perform well in diverse and re-alistic conditions. YOLO, a popular one-stage object detection approach, is widely em-ployed for UAV detection across different environments due to its efficiency and sim-plicity. However, this series of detectors encounter challenges in real-world scenarios, such as excessive computation and suboptimal detection rates. In this study, we propose a lightweight feature enhancement model (LFEM) to address these limitations.

## <div align="left">Requirements</div>
•	Python 3.8

•	Pytorch 2.1.2

All experiments in this work was run on a single NVIDIA RTX4090 GPU.
## <div align="left">Benchmarks</div>
<font size=6><b>1.Prepare data</b></font>

The dataset can be downloaded:

<font size=6><b>2. Run experiments</b></font>

To replicate our results, run 


## Citation

If you use this work, please cite our paper:

Han, Yanan and Yan, Xufei and Li, Yuan and Li, Danyang and Liu, Xiao-chao and Huang, Haishan and Bie, Da-wei；A lightweight feature enhancement model for UAV detection in real-world scenarios,2025




For YOLOv5 bug reports and feature requests please visit [GitHub Issues](https://github.com/ultralytics/yolov5/issues), and join our [Discord](https://ultralytics.com/discord) community for questions and discussions!

<br>
<div align="center">
  <a href="https://github.com/ultralytics" style="text-decoration:none;">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="" />
  <a href="https://www.linkedin.com/company/ultralytics/" style="text-decoration:none;">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="" />
  <a href="https://twitter.com/ultralytics" style="text-decoration:none;">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="" />
  <a href="https://youtube.com/ultralytics" style="text-decoration:none;">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="" />
  <a href="https://www.tiktok.com/@ultralytics" style="text-decoration:none;">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="" />
  <a href="https://www.instagram.com/ultralytics/" style="text-decoration:none;">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="" />
  <a href="https://ultralytics.com/discord" style="text-decoration:none;">
    <img src="https://github.com/ultralytics/assets/blob/main/social/logo-social-discord.png" width="3%" alt="" /></a>
</div>

[tta]: https://docs.ultralytics.com/yolov5/tutorials/test_time_augmentation

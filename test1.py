# import torch
# import torch.nn as nn

# class SimAM(torch.nn.Module):
#     def __init__(self, e_lambda=1e-4):
#         super(SimAM, self).__init__()

#         self.activaton = nn.Sigmoid()
#         self.e_lambda = e_lambda

#     def __repr__(self):
#         s = self.__class__.__name__ + '('
#         s += ('lambda=%f)' % self.e_lambda)
#         return s

#     @staticmethod
#     def get_module_name():
#         return "simam"

#     def forward(self, x):
#         b, c, h, w = x.size()
#         n = w * h - 1
#         x_minus_mu_square = (x - x.mean(dim=[2, 3], keepdim=True)).pow(2)
#         y = x_minus_mu_square / (4 * (x_minus_mu_square.sum(dim=[2, 3], keepdim=True) / n + self.e_lambda)) + 0.5
#         return x * self.activaton(y)

import numpy as np
from scipy.signal import KalmanFilter

# 初始化状态转移矩阵和测量矩阵
A = np.array([[1, 1], [0, 1]])
C = np.array([[1, 0]])

# 初始化状态估计和误差协方差
x = np.array([0, 0])
P = np.array([[1, 0], [0, 1]])

# 创建卡尔曼滤波器对象
kf = KalmanFilter(dim_x=2, dim_z=1, F=A, H=C, P=P)

# 模拟数据
measurements = np.array([0, 1, 2, 3, 4, 5])

# 执行卡尔曼滤波
for z in measurements:
    kf.predict()  # 预测
    kf.update(z)  # 更新
    print(f"状态估计：{kf.x}")

# 打印最终的状态估计和误差协方差
print(f"最终状态估计：{kf.x}")
print(f"最终误差协方差：{kf.P}")
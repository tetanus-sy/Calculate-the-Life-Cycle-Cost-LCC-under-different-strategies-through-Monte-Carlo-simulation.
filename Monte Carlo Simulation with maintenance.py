import matplotlib.pyplot as plt
import numpy as np
from function import seal_fault_cost as seal
from function import motor_fault_maintenance as motor
from function import impeller_fault_maintenance as impeller

# 设置中文和英文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 1080  # 图片清晰度

# 模拟次数
simulation_times = 20000
total_LCC_list = []

# 蒙特卡洛模拟
for _ in range(simulation_times):
    seal_fault_cost = seal()
    motor_fault_cost = motor()
    impeller_fault_cost = impeller()
    total_LCC = 591.9222 + 54.2603 + seal_fault_cost + motor_fault_cost + impeller_fault_cost
    total_LCC_list.append(total_LCC)

# 转换为NumPy数组便于统计
total_LCC_array = np.array(total_LCC_list)

# 计算统计数据
mean_val = np.mean(total_LCC_array)
std_val = np.std(total_LCC_array)
min_val = np.min(total_LCC_array)
max_val = np.max(total_LCC_array)
median_val = np.median(total_LCC_array)

# 输出统计信息
print(f"模拟次数：{simulation_times}")
print(f"平均LCC：{mean_val:.2f}")
print(f"标准差：{std_val:.2f}")
print(f"最小值：{min_val:.2f}")
print(f"最大值：{max_val:.2f}")
print(f"中位数：{median_val:.2f}")

# 绘图
plt.figure(figsize=(10, 6))
plt.hist(total_LCC_array, bins=50, edgecolor='black')
plt.axvline(mean_val, color='red', linestyle='--', linewidth=2,
            label=f'均值：{mean_val:.2f}')

plt.xlabel('总生命周期成本（LCC）', fontsize=16)
plt.ylabel('频数', fontsize=16)
plt.xticks( fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.tight_layout()
plt.show()







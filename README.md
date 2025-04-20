# Calculate-the-Life-Cycle-Cost-LCC-under-different-strategies-through-Monte-Carlo-simulation.

# 作业内容
---

## 题目主体
某化工厂计划对关键设备“高温离心泵组”制定维护策略，设备设计寿命10年。需考虑以下三种独立失效模式：

• 机械密封磨损（威布尔分布，浴盆曲线特征）

• 电机绝缘老化（指数分布，恒定故障率）

• 叶轮疲劳断裂（正态分布，集中性耗损）

要求：

1、不考虑故障损失成本时，计算10年期的基础LCC；

2、仅考虑故障损失成本且不考虑做任何维护动作，计算10年期的期望LCC（有能力的同学可通过蒙特卡洛方法实现，从而获得LCC的数值分布情况）；

3、考虑故障损失成本且采取维护策略I时，计算10年期的期望LCC（有能力的同学可通过蒙特卡洛方法实现，从而获得LCC的数值分布情况）。

## 设备参数
![Image](https://github.com/user-attachments/assets/5f6acd3f-e5b5-4499-9150-a3e0f3c8f62b)

## 成本参数
![Image](https://github.com/user-attachments/assets/af319680-435c-4f77-ad39-9e9066420c1b)

# 使用说明

第一问不需要代码可以完成

第二问：文件motor_fault.py，seal_failure.py, impeller_failure.py表示没有维护的三类故障损失计算，第二问需要用到，对这三个文件单独运行可以得到每种故障损失一次模拟的结果
这三个文件中都包含了损失计算函数，封装在function.py中，通过Monte Carlo Simulation without maintenance.py调用相关函数进行计算结果如下
![Image](https://github.com/user-attachments/assets/3c2d6917-8d28-4aeb-acbb-8dafe1a1aee5)


第三问：由于密封故障没有维护，所以仍然采用seal_feilure.py中的计算思路，motor_maintenance.py和impeller_maintenance.py是采用预防性维护后的计算代码
同样封装在function.py中，通过Monte Carlo Simulation with maintenance.py调用相关函数进行计算，结果如下
![Image](https://github.com/user-attachments/assets/59eda27c-f014-42f0-8052-eb4740ca343c)

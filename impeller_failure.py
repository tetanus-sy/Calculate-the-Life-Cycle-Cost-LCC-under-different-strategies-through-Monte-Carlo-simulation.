import numpy as np

def impeller_failure_cost(mean=8, std=1.5, cost_per_fault=190, discount_rate=0.06):
    fault_years = []
    current_time = 0
    impeller_failure_cost = 0

    while current_time < 10:
        # 生成服从正态分布的故障时间
        failure_time = np.random.normal(loc=mean, scale=std)
        # 确保故障时间为正数
        if failure_time <= 0:
            continue
        current_time += failure_time
        if current_time >= 10:
            break
        fault_years.append(int(np.ceil(current_time)))
        discounted_cost = cost_per_fault / ((1 + discount_rate) ** current_time)
        impeller_failure_cost += discounted_cost

    return fault_years,impeller_failure_cost
    
for _ in range(5):
    faults, costs = impeller_failure_cost()
    print(f"故障发生年份：{faults if faults else '10年内未发生故障'}")
    print(f"故障损失成本：{costs:.2f}")




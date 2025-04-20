import numpy as np

def motor_fault_cost(lambd=0.15, cost_per_fault=60, discount_rate=0.06):
    fault_years = []
    current_time = 0
    motor_fault_cost = 0

    while current_time < 10:
        failure_time = np.random.exponential(scale=1 / lambd)
        current_time += failure_time
        if current_time >= 10:
            break
        fault_years.append(int(np.ceil(current_time)))
        discounted_cost = cost_per_fault / ((1 + discount_rate) ** current_time)
        motor_fault_cost += discounted_cost

    return fault_years,motor_fault_cost

for _ in range(5):
    faults, costs = motor_fault_cost()
    print(f"故障发生年份：{faults if faults else '10年内未发生故障'}")
    print(f"故障损失成本：{costs:.2f}")
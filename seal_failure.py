import numpy as np

def seal_fault_cost():
    years = np.arange(0, 11)  # 包括0，代表“完全不发生故障”
    probs = [0.014, 0.3605, 0.2045, 0.1260, 0.0846, 0.0591,
             0.0423, 0.0308, 0.0226, 0.0396, 0.0160]
    current_time = 0
    total_cost = 0

    # 第一次先判断是否完全不发生故障
    interval = np.random.choice(years, p=probs)
    if interval == 0:
        return 0

    while current_time + interval <= 10:
        current_time += interval
        cost = 60 / ((1 + 0.06) ** current_time)
        total_cost += cost
        interval = np.random.choice(years, p=probs)
        if interval == 0:
            break  # 后续不再发生故障

    return total_cost

for _ in range(5):
    costs = seal_fault_cost()
    print(f"故障损失成本：{costs:.2f}")
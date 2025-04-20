import numpy as np

def motor_fault_maintenance(lambd=0.15, max_years=10, maintenance_interval=2):
    current_year = 0
    t = 1  # 失效模型里的相对时间，初始为1
    fault_years = []
    failure_cost = 0

    while current_year < max_years:
        # 模拟下一次故障的时间，从当前相对时间 t 开始
        u = np.random.uniform(0, 1)
        failure_time = - (1 / lambd) * np.log(u) + t - 1

        # 判断下一个事件是"故障"还是"维护"
        time_to_maintenance = maintenance_interval - (t - 1)

        if failure_time < time_to_maintenance:
            # 故障发生
            current_year += failure_time
            if current_year >= max_years:
                break
            fault_years.append(int(np.ceil(current_year)))
            cost = 130 / ((1 + 0.06) ** current_year)
            failure_cost += cost
            # 故障后将相对时间 t 重置为 1
            t = 1
        else:
            # 没故障但到了维护时间，维护一次
            current_year += time_to_maintenance
            # 维护后将相对时间 t 重置为 1
            t = 2

    total_cost = failure_cost
    return fault_years, total_cost

# 测试代码
for _ in range(5):
    faults, costs = motor_fault_maintenance()
    print(f"故障发生年份：{faults if faults else '10年内未发生故障'}")
    print(f"总损失成本：{costs:.2f}")
    print("-" * 30)


import numpy as np

def impeller_fault_maintenance(mean=8, std=1.5,  max_years=10, maintenance_interval=8):
    current_year = 0
    fault_years = []
    failure_cost = 0

    while current_year < max_years:
        # 8年强制更换
        failure_time = np.random.normal(loc=mean, scale=std)

        # 判断下一个事件是"故障"还是"维护"
        time_to_maintenance = maintenance_interval

        if failure_time < time_to_maintenance:
            # 故障发生
            current_year += failure_time
            if current_year >= max_years:
                break
            fault_years.append(int(np.ceil(current_year)))
            cost = 190 / ((1 + 0.06) ** current_year)
            failure_cost += cost
        else:
            # 没故障但到了维护时间，维护一次
            current_year += time_to_maintenance

    total_cost = failure_cost
    return fault_years, total_cost

for _ in range(5):
    faults, costs = impeller_fault_maintenance()
    print(f"故障发生年份：{faults if faults else '10年内未发生故障'}")
    print(f"总损失成本：{costs:.2f}")
    print("-" * 30)
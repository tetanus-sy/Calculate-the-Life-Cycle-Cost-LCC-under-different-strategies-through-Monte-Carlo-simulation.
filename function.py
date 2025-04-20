import numpy as np

"""
seal_fault_cost. motor_fault_cost 和 impeller_failure_cost 为第二问所用函数
"""
def seal_fault_cost():
    years = np.arange(0, 11)  # 包括0，代表“完全不发生故障”
    probs = [0.014, 0.3605, 0.2045, 0.1260, 0.0846, 0.0591,
             0.0423, 0.0308, 0.0226, 0.0396, 0.0160]#认为分布是离散的，实际并不是
    current_time = 0
    seal_fault_cost = 0

    # 第一次先判断是否完全不发生故障
    interval = np.random.choice(years, p=probs)
    if interval == 0:
        return 0

    while current_time + interval <= 10:
        current_time += interval
        cost = 60 / ((1 + 0.06) ** current_time)
        seal_fault_cost += cost
        interval = np.random.choice(years, p=probs)
        if interval == 0:
            break  # 后续不再发生故障

    return seal_fault_cost

def motor_fault_cost(lambd=0.15, cost_per_fault=130, discount_rate=0.06):
    fault_years = []
    current_time = 0
    motor_fault_cost = 0

    while current_time < 10:
        failure_time = np.random.exponential(scale=1 / lambd)#此时保持分布连续
        current_time += failure_time
        if current_time >= 10:
            break
        fault_years.append(int(np.ceil(current_time)))#将发生时间向上取整
        discounted_cost = cost_per_fault / ((1 + discount_rate) ** current_time)
        motor_fault_cost += discounted_cost

    return motor_fault_cost

def impeller_fault_cost(mean=8, std=1.5, cost_per_fault=190, discount_rate=0.06):
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

    return impeller_failure_cost

"""
motor_fault_maintenance 和 impeller_fault_maintenance 为第三问所用函数；
由于对密封故障没有维护措施，所以采取seal_fault_cost函数
"""

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

    return failure_cost


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

    
    return failure_cost
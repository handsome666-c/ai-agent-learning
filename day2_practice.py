import time

# 1. 定义一个装饰器：打印"开始读取"和"读取完成"
def log_sensor(func):
    def wrapper(*args, **kwargs):
        print(f"[开始] 调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[完成] {func.__name__} 返回 {result}")
        return result
    return wrapper

# 2. 定义一个生成器：模拟温度传感器，yield 返回 5 次数据
def temperature_sensor():
    for i in range(5):
        yield {"time": i, "temp": 20 + i * 2}  # 温度递增
        time.sleep(0.1)

# 3. 用 @log_sensor 装饰一个读取函数
@log_sensor
def read_sensor_once():
    # 从生成器取一条数据（用 next）
    gen = temperature_sensor()
    return next(gen)

# 4. 主程序
print("=== 测试装饰器 ===")
read_sensor_once()

print("\n=== 测试生成器 ===")
for data in temperature_sensor():
    print(data)

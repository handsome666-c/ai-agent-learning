import asyncio
import time

async def read_temperature(interval):
    """温度传感器：每 interval 秒读取一次"""
    sensor_id = "温度"
    while True:
        await asyncio.sleep(interval)
        temp = 20 + (time.time() % 10)  # 模拟温度变化
        print(f"  [{sensor_id}] {temp:.1f}℃")

async def read_humidity(interval):
    """湿度传感器：每 interval 秒读取一次"""
    sensor_id = "湿度"
    while True:
        await asyncio.sleep(interval)
        humidity = 40 + (time.time() % 20)  # 模拟湿度变化
        print(f"  [{sensor_id}] {humidity:.1f}%")

async def read_voltage(interval):
    """电压传感器：每 interval 秒读取一次"""
    sensor_id = "电压"
    while True:
        await asyncio.sleep(interval)
        voltage = 220 + (time.time() % 5)  # 模拟电压波动
        print(f"  [{sensor_id}] {voltage:.1f}V")

async def llm_analyze(timeout=3):
    """LLM分析：每2秒尝试分析一次，超时3秒放弃"""
    while True:
        await asyncio.sleep(2)
        print("[LLM] 开始分析传感器数据...")
        try:
            result = await asyncio.wait_for(
                llm_inference(),  # 模拟推理
                timeout=timeout
            )
            print(f"[LLM] 分析结果: {result}")
        except asyncio.TimeoutError:
            print("[LLM] 超时！使用本地策略")

async def llm_inference():
    """模拟LLM推理：实际需要5秒"""
    await asyncio.sleep(5)  # 模拟慢推理
    return "建议降低充电功率"

async def heartbeat(interval):
    """心跳上报：每 interval 秒向云端发状态"""
    count = 0
    while True:
        await asyncio.sleep(interval)
        count += 1
        print(f"[心跳] 第{count}次上报，设备在线")

async def main():
    print("=== 边缘设备异步数据采集器 ===")
    print("按 Ctrl+C 停止\n")
    
    # 同时创建所有任务
    tasks = [
        asyncio.create_task(read_temperature(0.5)),   # 温度：0.5秒
        asyncio.create_task(read_humidity(0.8)),      # 湿度：0.8秒
        asyncio.create_task(read_voltage(1.0)),        # 电压：1秒
        asyncio.create_task(llm_analyze(timeout=3)),    # LLM：2秒一次，超时3秒
        asyncio.create_task(heartbeat(1.0)),           # 心跳：1秒
    ]
    
    # 等待所有任务（实际上会一直运行）
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n=== 程序已停止 ===")

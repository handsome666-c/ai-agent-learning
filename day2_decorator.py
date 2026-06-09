import time

# ========== 装饰器 1：计时器 ==========
def timer(func):
    """给函数加上计时功能"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[计时] {func.__name__} 耗时: {end-start:.3f} 秒")
        return result
    return wrapper

# ========== 装饰器 2：日志记录 ==========
def log_api(func):
    """自动记录函数入参和返回值"""
    def wrapper(*args, **kwargs):
        print(f"[日志] 调用: {func.__name__}, 参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[日志] 返回: {result}")
        return result
    return wrapper

# ========== 使用装饰器 ==========

@timer
@log_api
def llm_predict(prompt, model="glm-4"):
    """模拟 LLM 推理"""
    time.sleep(0.5)  # 模拟网络+推理延迟
    return f"模型 {model} 对 '{prompt}' 的回答"

# 调用
print("=== 测试装饰器 ===")
answer = llm_predict("什么是嵌入式AI",model="glm-4-flash")
print(f"最终结果: {answer}")

# ========== 生成器：模拟流式输出 ==========
def stream_response(text):
    """像大模型一样，逐字返回结果"""
    for char in text:
        yield char          # 暂停，返回一个字
        time.sleep(0.05)    # 模拟推理延迟

# ========== 使用生成器 ==========
print("\n=== 测试流式输出 ===")
full_text = "嵌入式AI是指在设备上运行人工智能。"
for chunk in stream_response(full_text):
    print(chunk, end="", flush=True)  # 逐字打印，不换行
print()  # 最后换行

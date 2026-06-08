class ModelLoader:
    """模拟一个AI模型加载器"""
    
    def __init__(self, model_name, api_key):
        """构造函数：创建对象时自动执行"""
        self.model_name = model_name
        self.api_key = api_key
        self.is_loaded = False
        print(f"[初始化] 创建加载器：{model_name}")
    
    def load(self):
        """加载模型"""
        self.is_loaded = True
        print(f"[加载] {self.model_name} 加载完成")

    def predict(self, prompt):
        """模拟推理"""
        if not self.is_loaded:
            print("[错误] 模型未加载，请先调用 load()")
            return None
        print(f"[推理] 输入：{prompt}")
        return f"这是 {self.model_name} 对 '{prompt}' 的回答"
    
    def unload(self):
        """卸载模型"""
        self.is_loaded = False
        print(f"[卸载] {self.model_name} 已卸载")

    def get_status(self):
        if self.is_loaded:
            return f"{self.model_name}已加载"
        else:
            return f"{self.model_name}未加载"
# ========== 使用这个类 ==========

# 1. 创建对象（实例化）
loader = ModelLoader("deepseek-chat", "sk-xxx")
print(loader.get_status())

# 2. 调用方法
loader.load()

print(loader.get_status())

result = loader.predict("什么是嵌入式AI？")
print(f"结果：{result}")

loader.unload()

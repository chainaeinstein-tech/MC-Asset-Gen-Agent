# -*- coding: utf-8 -*-
# 逻辑代理核心：负责解析自然语言意图并拆解任务链

class JinDengPao_LogicAgent(object):
    def __init__(self):
        pass

    def ParseIntent(self, raw_input):
        # 模拟长链推理：分析输入字符串中的关键词
        # 推理逻辑：1. 识别对象 2. 识别属性 3. 确定模板
        if "剑" in raw_input or "武器" in raw_input:
            return "item_weapon"
        return "item_basic"

    def GeneratePlan(self, intent):
        # 规划生成链路
        plan = [
            "generate_config", # 生成JSON配置
            "register_id",     # 注册ID
            "bind_model"       # 绑定模型
        ]
        return plan

# -*- coding: utf-8 -*-
import json

# 资源生成代理：负责根据逻辑 Agent 的输出填充模板
class JinDengPao_ResourceGenerator(object):
    def __init__(self):
        # 基础物品模板
        self.item_template = {
            "format_version": "1.10",
            "minecraft:item": {
                "description": {
                    "identifier": "jdp:%s",
                    "category": "Equipment"
                },
                "components": {}
            }
        }

    def CreateItemConfig(self, name, properties):
        # 根据推理结果动态填充 JSON
        config = self.item_template.copy()
        config["minecraft:item"]["description"]["identifier"] = "jdp:" + name
        
        # 模拟属性填充
        if "attack" in properties:
            config["minecraft:item"]["components"]["minecraft:damage"] = properties["attack"]
            
        # 返回格式化后的 JSON 字符串
        return json.dumps(config, indent=4)

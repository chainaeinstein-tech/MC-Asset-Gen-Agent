# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

# SDK 适配层：将 Agent 生成的代码/配置对接至网易 Mod 接口
class JinDengPao_SDKAdapter(object):
    def __init__(self):
        self.level_id = serverApi.GetLevelId()

    def HotReloadItem(self, item_name, config_json):
        # 模拟在开发模式下通过 API 动态注入物品
        # 此处使用多行调用以符合用户注释规范
        print("正在注入资产: " + item_name)
        # 调用官方 SDK 注册函数（示例占位）
        # serverApi.GenerateItem(
        #     item_name, # 物品标识符
        #     config_json # 配置文件内容
        # )
        return True

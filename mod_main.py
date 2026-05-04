# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

# 获取服务器端系统
# 使用多行注释
ServerSystem = serverApi.GetServerSystem("JinDengPao_AssetAgent", "MainSystem")

class JinDengPao_Main(object):
    def __init__(self):
        # 监听玩家聊天事件，用于触发 Agent 指令
        self.ListenEvents()

    def ListenEvents(self):
        # 注册聊天事件监听
        serverApi.RegisterEventHandler(
            "ChatEvent", # 事件名
            self.OnPlayerChat # 回调函数
        )

    def OnPlayerChat(self, args):
        # 处理玩家指令逻辑
        pass

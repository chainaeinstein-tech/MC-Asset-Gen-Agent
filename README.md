Minecraft Asset Agent (Asset-to-Code Pipeline) v1.0
-----------------------------------------------------------
作者：Golden Lightbulb Studio
版本：Python 2.7 (网易版兼容)

项目结构说明：
1. mod_main.py: 插件入口，负责事件监听。
2. logic_agent_core.py: 核心 Agent 逻辑，负责意图识别与任务规划。
3. resource_generator_agent.py: 资源生成模块，处理 JSON 模板。
4. mod_sdk_adapter.py: 对接网易 Mod SDK 的适配层。

使用方法：
1. 将此文件夹内容放入您的 Mod 脚本目录下。
2. 在 mod_main.py 中初始化 JinDengPao_LogicAgent。
3. 通过监听 ChatEvent 捕获指令并调用 Agent 管道。

注意事项：
- 所有 Python 文件均符合 Python 2.7 规范。
- 遵循参数注释规范（多行调用或上行注释）。

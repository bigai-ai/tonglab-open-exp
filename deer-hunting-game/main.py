import tkinter as tk
import constant
from agent import Agent
from gui_AI import AutomationGUI
from util_sio import sio, send_action

@sio.event(namespace=constant.namespace)
def connect():
    print(f"成功与{constant.room_id}房间建立连接！请检查{constant.room_id}是否和前端页面的房间号一致，点击前端页面上的“开始挑战”按钮即可开始游戏")

@sio.on('message', namespace=constant.namespace) # 信令返回结果
def message(data):
    print("message begin", data)
    message_type = data['messageType'] # 信令类型
    data_code = data['statusCode'] # 状态码，0表示成功
    data_msg = data['statusMsg'] # 状态信息
    if message_type == 6:
        if data_code != 0:
            print("message data_msg", data_msg) # 执行动作失败，打印日志
    print("message end")

@sio.on('broadcast', namespace=constant.namespace) # 收到广播
def broadcast(data):
    message_type = data['messageType']
    print("broadcast message_type", message_type)
    if message_type in [11, 12]: # 游戏结束
        root.quit()
        return
    if message_type in [10, 14, 15]:# 游戏开始或者获取最新地图信息，触发动作规划函数
        agent.add_env_data(data)
        if gui.mode == constant.STOP_AUTOMATION: # 不使用AI托管
            return
        
        action = agent.take_action() # 根据环境信息计算得到action并采用
        if gui.mode == constant.FULL_AUTOMATION: # 全程AI托管
            send_action(action)  # 调用新函数发送消息
        elif gui.mode == constant.SUGGESTION_ONLY: # AI只输出动作建议，不执行动作
            # 更新GUI显示AI建议
            gui.update_suggestion(action)
            print(f"AI建议的动作：{action}")

    print("broadcast end")



if __name__ == '__main__':
    try:
        sio.connect(constant.socket_url)  # 与云端建立socket连接
        agent = Agent() # 创建agent
        root = tk.Tk()
        gui = AutomationGUI(root,agent) # 创建GUI
        root.mainloop() # 启动GUI
    finally:
        print("连接已断开")
        sio.disconnect() # 断开连接
    print("脚本退出")




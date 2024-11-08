import tkinter as tk
import agent
import constant
from util_sio import send_action

class AutomationGUI:

    def __init__(self, root, agent: agent.Agent):
        self.root = root
        self.agent = agent
        root.title("猎鹿游戏AI托管程序")
        root.geometry("400x300") 
        
        # 添加以下行以设置窗口图标
        root.iconbitmap("imgs/icon.ico")  # 替换为您的图标文件路径
        
        tk.Label(root, text="温馨提示：",fg="red").pack()
        tk.Label(root, text=f"成功与{constant.room_id}房间建立连接！",fg="red").pack()
        tk.Label(root, text=f"请检查{constant.room_id}是否和前端页面的房间号一致。",fg="red").pack()
        tk.Label(root, text=f"点击前端页面上的“开始挑战”按钮即可开始游戏。", fg="red").pack()

        self.is_top = tk.BooleanVar(value=True) # 是否置顶
        self.toggle_top()  # 添加此行以使窗口默认置顶
        # 创建置顶开关
        self.top_switch = tk.Checkbutton(root, text="置顶窗口", variable=self.is_top, command=self.toggle_top)
        self.top_switch.pack()

        self.mode = constant.FULL_AUTOMATION # 默认全程AI托管
        
        tk.Label(root, text="AI托管模式（选中自动生效）: ", fg="blue").pack(anchor='w', padx=10, pady=10)
        
        self.automation_var = tk.StringVar(value=constant.FULL_AUTOMATION)  
        
        tk.Radiobutton(root, text=constant.STOP_AUTOMATION, variable=self.automation_var, value=constant.STOP_AUTOMATION, 
                       command=self.update_mode).pack(anchor='w', padx=10, pady=5)
        
        tk.Radiobutton(root, text=constant.FULL_AUTOMATION, variable=self.automation_var, value=constant.FULL_AUTOMATION, 
                       command=self.update_mode).pack(anchor='w', padx=10, pady=5)
        
        tk.Radiobutton(root, text=constant.SUGGESTION_ONLY, variable=self.automation_var, value=constant.SUGGESTION_ONLY, 
                       command=self.update_mode).pack(anchor='w', padx=10, pady=5)
        
        self.suggestion_label = tk.Label(root, text="AI建议:  暂无")
        self.suggestion_label.pack(pady=5)
    def update_mode(self):
        if self.automation_var.get() == constant.FULL_AUTOMATION:
            self.full_automation()
        elif self.automation_var.get() == constant.SUGGESTION_ONLY:
            self.suggestion_only()
        else:
            self.stop_automation()
    
    def full_automation(self):
        self.mode = constant.FULL_AUTOMATION
        action = self.agent.take_action() # 根据环境信息计算得到action并采用
        send_action(action) 
        
    def stop_automation(self):
        self.mode = constant.STOP_AUTOMATION
        self.suggestion_label.config(text="AI建议:  暂无")

    def suggestion_only(self):
        self.mode = constant.SUGGESTION_ONLY
        action = self.agent.take_action() # 根据环境信息计算得到action并采用
        self.update_suggestion(action)
    
    def update_suggestion(self, action): # 更新AI建议
        map_action = {
            constant.UP: "↑",
            constant.DOWN: "↓",
            constant.LEFT: "←",
            constant.RIGHT: "→",
            constant.STOP: "原地不动"
        }
        self.suggestion_label.config(text=f"AI建议:  {map_action[action]}")

    def toggle_top(self):
        # 根据复选框状态控制窗口置顶属性
        if self.is_top.get():
            self.root.attributes("-topmost", True)
        else:
            self.root.attributes("-topmost", False)

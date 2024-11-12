# 重要提示：room_id、user_id、agent_id要与前端页面上的房间号、用户id、智能体id一致！！！！！！
room_id = 4237 # 房间号
user_id = "8a7f8352-dec0-453f-b242-e0eab727d878" # 用户id
agent_id = "6c36afef-32d7-4f16-a3c9-fd8ee65604bb" # 智能体id

# socket连接配置
# ip_port = "10.1.100.94:6103" # 从实验手册中获取
# ip_port = "10.1.101.76:6103" # 从实验手册中获取
ip_port = "123.127.249.42:6103" # 从实验手册中获取
# http://123.127.249.42:3107/#/experiment/detail/ef6700d6-53f0-4a43-b996-c2b78c917860 tonglab前端地址
socket_url = f'http://{ip_port}/?userId={user_id}_py'
namespace = '/staghunt'

# 动作常量
UP    = "ArrowUp"    # 上
DOWN  = "ArrowDown"  # 下
LEFT  = "ArrowLeft"  # 左
RIGHT = "ArrowRight" # 右
STOP  = "space"      # 空格，静止不动

# AI托管模式常量
STOP_AUTOMATION = "不使用AI托管"
FULL_AUTOMATION = "全程AI托管"
SUGGESTION_ONLY = "AI只输出动作建议，不执行动作"

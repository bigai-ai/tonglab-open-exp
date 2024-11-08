import random
import constant

class Agent:
    def __init__(self):
        self.lst_env_data = [] # 存储每一轮的环境数据，用于动作规划

    def add_env_data(self, env_data): # 添加环境数据
        self.lst_env_data.append(env_data) 

    def take_action(self): # 根据环境数据规划动作
        # 学生在这里写根据环境数据进行动作规划的逻辑。
        # 这里展示一个简单的例子
        if not self.lst_env_data:
            return constant.STOP
        env_data_last = self.lst_env_data[-1] # 获取最新一轮的环境数据
        lst_wall_xy = [[v['position']['x'],v['position']['y']] for k,v in env_data_last['data']['mapInfo']['6']['objectPositions'].items()]
        lst2d_wall_xy = [[False for _ in range(19)] for _ in range(19)]  # 使用列表推导式创建独立的列表
        for x,y in lst_wall_xy:
            lst2d_wall_xy[y][x] = True
        pos_sunwukong = [v for k,v in env_data_last['data']['mapInfo']['5']['objectPositions'].items()][0]['position']
        x_sunwukong, y_sunwukong = pos_sunwukong['x'], pos_sunwukong['y']
        # 孙悟空不能撞墙，也不能走出地图边界
        lst_action = [constant.UP, constant.DOWN, constant.LEFT, constant.RIGHT, constant.STOP]
        if x_sunwukong == 0:
            lst_action.remove(constant.LEFT)
        elif x_sunwukong == 18:
            lst_action.remove(constant.RIGHT)
        if y_sunwukong == 0:
            lst_action.remove(constant.UP)
        elif y_sunwukong == 18:
            lst_action.remove(constant.DOWN)
        if x_sunwukong < 18 and lst2d_wall_xy[y_sunwukong][x_sunwukong+1]:
            lst_action.remove(constant.RIGHT)
        elif x_sunwukong > 0 and lst2d_wall_xy[y_sunwukong][x_sunwukong-1]:
            lst_action.remove(constant.LEFT)
        if y_sunwukong < 18 and lst2d_wall_xy[y_sunwukong+1][x_sunwukong]:
            lst_action.remove(constant.DOWN)
        elif y_sunwukong > 0 and lst2d_wall_xy[y_sunwukong-1][x_sunwukong]:
            lst_action.remove(constant.UP)
        random_action = random.choice(lst_action)
        action = random_action
        return action


        

import random
import constant

class Agent:
    def __init__(self):
        """
        初始化智能体
        """
        self.lst_env_data = []  # 存储每一轮的环境数据
        self.collaborating_agent = None  # 协作捕获的智能体

    def add_env_data(self, env_data):
        """
        添加环境数据到列表中
        """
        self.lst_env_data.append(env_data)

    def take_action(self):
        """
        根据环境数据规划智能体动作，示例代码并不是标准答案，可以扩展自己的完善逻辑扩展自己的思路
        """
        if not self.lst_env_data:
            return constant.STOP  # 如果没有环境数据，则停止

        env_data_last = self.lst_env_data[-1]  # 获取最新的环境数据

        # 提取智能体、鹿、兔子和墙壁的信息
        obj_agent = next((i for i in env_data_last['data']['mapInfo'] if i['objectName'] == "孙悟空"), None)
        obj_deer = next((i for i in env_data_last['data']['mapInfo'] if i['objectName'] == "stag"), None)
        obj_rabbit = next((i for i in env_data_last['data']['mapInfo'] if i['objectName'] == "hare"), None)
        obj_wall = next((i for i in env_data_last['data']['mapInfo'] if i['objectName'] == "wall"), None)
        obj_other_agents = [
                i for i in env_data_last['data']['mapInfo'] if i['objectName'] != "孙悟空" and i['objectType'] == 11
            ]
        other_agents_positions = [
            pos['position'] for agent in obj_other_agents
            for pos in agent.get('objectPositions', {}).values()
        ]
        
        if not obj_agent:
            return constant.STOP  # 如果没有智能体数据，停止

        # 智能体位置
        agent_position = next(iter(obj_agent['objectPositions'].values()))['position']


        # 墙壁位置列表
        lst_wall_positions = obj_wall['wallPositions'] if obj_wall else []
        lst2d_wall_map = [[False for _ in range(19)] for _ in range(19)]
        for wall in lst_wall_positions:
            lst2d_wall_map[wall['y']][wall['x']] = True

        # 鹿的位置列表
        lst_deer_positions = [pos['position'] for pos in obj_deer.get('objectPositions', {}).values()] if obj_deer else []
        # 兔子的位置列表
        lst_rabbit_positions = [pos['position'] for pos in obj_rabbit.get('objectPositions', {}).values()] if obj_rabbit else []

        # 如果没有目标（鹿或兔），停止
        if not lst_deer_positions and not lst_rabbit_positions:
            return constant.STOP

        # 如果鹿存在，优先捕鹿
        if lst_deer_positions:
            nearest_deer = self.find_nearest(agent_position, lst_deer_positions)

            # 如果智能体在鹿的位置上，且没有其他智能体，则保持静止
            if agent_position == nearest_deer and agent_position not in other_agents_positions:
                return constant.STOP
            return  self.plan_movement(agent_position, nearest_deer, lst2d_wall_map)
        
        # 如果鹿为空但兔存在，捕兔
        if not lst_deer_positions and lst_rabbit_positions:
            nearest_rabbit = self.find_nearest(agent_position, lst_rabbit_positions)
            return  self.plan_movement(agent_position, nearest_rabbit, lst2d_wall_map)



    def find_nearest(self, agent_position, lst_positions):
        """
        根据智能体位置找到最近的目标（鹿或兔）
        """
        if not lst_positions:
            return None

        distances = [
            (obj, abs(agent_position['x'] - obj['x']) + abs(agent_position['y'] - obj['y']))
            for obj in lst_positions
        ]
        # 返回距离最近的目标
        nearest_obj = min(distances, key=lambda x: x[1])[0]
        return nearest_obj

    def plan_movement(self, agent_position, target_position, wall_map):
        """
        根据智能体当前的位置和目标位置规划动作，并防止撞墙和越界
        """
        dx = target_position['x'] - agent_position['x']
        dy = target_position['y'] - agent_position['y']

        # 存储合法动作
        possible_actions = [constant.UP, constant.DOWN, constant.LEFT, constant.RIGHT]

        # 根据墙壁和边界限制合法动作
        if agent_position['x'] == 0 or wall_map[agent_position['y']][agent_position['x'] - 1]:
            possible_actions.remove(constant.LEFT)
        if agent_position['x'] == 18 or wall_map[agent_position['y']][agent_position['x'] + 1]:
            possible_actions.remove(constant.RIGHT)
        if agent_position['y'] == 0 or wall_map[agent_position['y'] - 1][agent_position['x']]:
            possible_actions.remove(constant.UP)
        if agent_position['y'] == 18 or wall_map[agent_position['y'] + 1][agent_position['x']]:
            possible_actions.remove(constant.DOWN)

        # 优先根据目标位置选择动作
        if dx > 0 and constant.RIGHT in possible_actions:
            return constant.RIGHT
        elif dx < 0 and constant.LEFT in possible_actions:
            return constant.LEFT
        elif dy > 0 and constant.DOWN in possible_actions:
            return constant.DOWN
        elif dy < 0 and constant.UP in possible_actions:
            return constant.UP

        # 如果目标位置不可到达，随机选择一个合法动作
        return random.choice(possible_actions) if possible_actions else constant.STOP

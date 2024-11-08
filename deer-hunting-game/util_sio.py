import uuid
import socketio
import constant

sio = socketio.Client()

def send_action(action):
    message = {
        "traceId": str(uuid.uuid4()),"messageType": 6,
        "data": {"roomId": constant.room_id, "uuid": constant.agent_id, "action": action}
    }
    sio.emit('message', message, namespace=constant.namespace) # 执行动作

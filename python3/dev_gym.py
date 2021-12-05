import asyncio
from gym import Gym
import os

fwd_model_uri = os.environ.get(
    "FWD_MODEL_CONNECTION_STRING") or "ws://127.0.0.1:6969/?role=admin"

mock_6x6_state = {"units": [{"coordinates": [0, 1], "hp":3, "inventory":{"bombs": 3}, "blast_diameter": 3, "unit_id": "c", "agent_id": "a", "invulnerability": 0}, {"coordinates": [5, 1], "hp":3, "inventory":{"bombs": 3}, "blast_diameter": 3, "unit_id": "d", "agent_id": "b", "invulnerability": 0}, {"coordinates": [3, 3], "hp":3, "inventory":{"bombs": 3}, "blast_diameter": 3, "unit_id": "e", "agent_id": "a", "invulnerability": 0}, {"coordinates": [2, 3], "hp":3, "inventory":{"bombs": 3}, "blast_diameter": 3, "unit_id": "f", "agent_id": "b", "invulnerability": 0}, {"coordinates": [2, 4], "hp":3, "inventory":{"bombs": 3}, "blast_diameter": 3, "unit_id": "g", "agent_id": "a", "invulnerability": 0}, {"coordinates": [3, 4], "hp":3, "inventory":{"bombs": 3}, "blast_diameter": 3, "unit_id": "h", "agent_id": "b", "invulnerability": 0}], "entities": [
    {"created": 0, "x": 0, "y": 3, "type": "m"}, {"created": 0, "x": 5, "y": 3, "type": "m"}, {"created": 0, "x": 4, "y": 3, "type": "m"}, {"created": 0, "x": 1, "y": 3, "type": "m"}, {"created": 0, "x": 3, "y": 5, "type": "m"}, {"created": 0, "x": 2, "y": 5, "type": "m"}, {"created": 0, "x": 5, "y": 4, "type": "m"}, {"created": 0, "x": 0, "y": 4, "type": "m"}, {"created": 0, "x": 1, "y": 1, "type": "w", "hp": 1}, {"created": 0, "x": 4, "y": 1, "type": "w", "hp": 1}, {"created": 0, "x": 3, "y": 0, "type": "w", "hp": 1}, {"created": 0, "x": 2, "y": 0, "type": "w", "hp": 1}, {"created": 0, "x": 5, "y": 5, "type": "w", "hp": 1}, {"created": 0, "x": 0, "y": 5, "type": "w", "hp": 1}, {"created": 0, "x": 4, "y": 0, "type": "w", "hp": 1}, {"created": 0, "x": 1, "y": 0, "type": "w", "hp": 1}, {"created": 0, "x": 5, "y": 0, "type": "w", "hp": 1}, {"created": 0, "x": 0, "y": 0, "type": "w", "hp": 1}]}


async def main():
    gym = Gym(fwd_model_uri)
    await gym.connect_forward_model()
    env = gym.make("bomberland-open-ai-gym", mock_6x6_state)
    observation = env.reset()
    for _ in range(100):
        actions = []
        observation, reward, done, info = await env.step(actions)

        if done:
            observation = env.reset()
    await env.close()

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(main()),
]
loop.run_until_complete(asyncio.wait(tasks))

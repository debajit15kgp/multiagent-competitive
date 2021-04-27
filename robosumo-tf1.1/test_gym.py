
#Importing OpenAI gym package and MuJoCo engine
import gym
import robosumo
import mujoco_py
#Setting MountainCar-v0 as the environment
env = gym.make('RoboSumo-Half_Cheetah-vs-Half_Cheetah-v0')
# env = gym.make('RoboSumo-Humanoid-vs-Humanoid-v0')
# env = gym.make('HalfCheetah-v2')
#Sets an initial state
env.reset()
# Rendering our instance 300 times
for _ in range(300000000):
  #renders the environment
  env.render('human')
  #Takes a random action from its action space 
  # aka the number of unique actions an agent can perform
  env.step(env.action_space.sample())
env.close()
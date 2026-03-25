import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent


class Agent6(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "NASIMI Mohamad Abobaker" # replace with your chosen name

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        target = obs["paths_end"][0] #prendre des x,y,z de pist pour etre au centre 
        steerx = target[0]  #prendre x pour entre en centre 
        dist = obs["distance_down_track"]
        acceleration = 0.90
        if (abs(steerx) > 75 and dist > 25):
            acceleration = 0.35



        action = {
            "acceleration": acceleration,
            "steer": steerx,
            "brake": False, # bool(random.getrandbits(1)),
            "drift": False,
            "nitro": False,
            "rescue": False,
            "fire": False,
        }
        return action

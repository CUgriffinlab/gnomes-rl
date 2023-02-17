"""Reinforcment learning submission template"""
from submission.rl_training import *
import pkg_resources

def load_agent():
    """
    Load reinforcment learning agent

    Returns
    -------
    _type_
        Reinforcement learning agent
    """
    stream = pkg_resources.resource_stream(__name__, "my_test.zip")
    agent = SAC.load(stream)
    return agent

def predict(home):
    """
    Simple rule-based prediction function as a template

    Parameters
    ----------
    home : dragg_comp.player.PlayerHome
        Your home

    Returns
    -------
    list
        List of actions (floats in [-1,1]) corresponding to hvac, wh, and electric vehicle
    """
    # Load agent
    agent = load_agent()

    # Normalize observations
    norm_obs = normalization(home)

    # Make predictions
    action = agent.predict(norm_obs)[0]
    return action

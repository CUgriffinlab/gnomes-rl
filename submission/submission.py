"""Reinforcment learning submission template"""
from submission.rl_training import *

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
        List of actions corresponding to hvac, wh, and electric vehicle
    """
    # Load agent
    agent = SAC.load("../../submission/my_test")

    # Normalize observations
    norm_obs = normalization(home)

    # Make predictions
    action = agent.predict(norm_obs)[0]
    return action
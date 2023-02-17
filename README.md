# gnomes-rl
GNOMES reinforcement learning template.

# Getting Your Submission to Use Reinforcement Learning

Just like the rule-based controller, you are still fundamentally supplying a `predict` function in `submission.py` to supply actions to your home. However, instead of your `predict` function using a series of conditional logic controls, it will now use a pretrained reinforcement learning agent (created using the stable baselines package). We have supplied an example of this in the `submission` directory. Note, that the new `submission.py` loads a pretrained agent saved in `my_agent.zip`. You must also make sure your submission loads this `my_agent.zip` by adding it to the `setup.py` file as we have done.

# How to train your agent

The trained agent we have supplied as an example in `my_agent.zip` performs fairly poorly, so you may want to train a new agent to new data. To change RL performance modify `training/rl_training.py` with the desired functions to modify (1) the RL environment and (2) the training process. The following functions are defined in `training/rl_training.py` and used in `training/train_player.py`. We strongly recommend customizing the definitions in `training/rl_training.py` but you may also modify the training process in `training/train_player.py` if you wish. To use the default training process you shoudl define the following functions (with the same naming convention):

1) `reward(home)`

  This function is used to modify the RL environment and returns a numeric value (float) that characterizes the RL performance. 

2) `normalization(home)`

  This function is used to modify the RL environment and returns a list of numeric values (float, arbitrary length) that characterizes the state of the environment. You may want to use the data provided in `home.obs_dict`.

3) `train(home)`

  This function is used to create and save an RL agent. You may use any method you would like to create and save an agent, but ensure that it can be called from `submission.py`.

4) Helper functions

  You may use any helper functions throughout the script (ex. we define `norm_helper()`.) There is no naming convention you need to follow.

5) Custom imports

  Unlike `submission.py` this script will not be run during the scoring process. As such you may use any custom imports you would like.

You can train your agent (and generate a new `my_agent.zip`) using Docker or non-docker setups:

## Training using docker

1) Build the training using `docker-compose -f ./training/docker-compose.yml build`

2) Run the training using `docker-compose -f ./training/docker-compose.yml up --abort-on-container-exit`

3) The trained network should appear in submission as `my_agent.zip`. You *must* include this file with your submission. 

## Training using non-docker

1) Follow steps 1-4 from the [non-docker submission documentation]( https://cugriffinlab.github.io/gnomes-submission/tutorial.html#self-evaluation-testing-for-non-docker-setups )

2) Open two new terminal windows

    * In each window, change the directory to the sandbox simulation folder using `$ cd <your-username-gnomes>/training/simulation`

    * In one terminal window, start the player submission using `$ python train_player.py`

    * In the other terminal window, run the simualtion using `$ python run_aggregator.py`
    
# How to test your agent

You will need to modify `submission.py` to accomodate the RL agent. Specifically to load the agent from any pre-training you did in the previous section. Any packages or supporting files you require should be added to the setup.py with the following lines:

  `package_data={'': ['<your-file-name-here>']},`
  `install_requires=['<your-package-names-here>']`

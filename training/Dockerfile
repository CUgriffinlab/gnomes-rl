# Install python
FROM python:3.9

# Install dragg
RUN pip install dragg==2.0.6

# Install dragg-comp
RUN pip install dragg-comp
RUN pip install cvxopt
RUN pip install stable-baselines3

# Copy parent directory
ADD . /gnomes-rl

# Install submission
RUN pip install /gnomes-rl/.

# Run simulation
WORKDIR  /gnomes-rl/training/simulation
CMD python run_aggregator.py -r "redis://redis" & python train_player.py -r "redis://redis" 

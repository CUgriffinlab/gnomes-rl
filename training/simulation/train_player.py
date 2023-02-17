from datetime import datetime
import asyncio
import argparse

from dragg_comp.envs import *
from rl_training import *

REDIS_URL = "redis://localhost"

if __name__=="__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--redis", help="Redis host URL", default=REDIS_URL)
	args = parser.parse_args()

	env = RLTrainingEnv(redis_url=args.redis, 
		normalization=normalization, 
		reward=reward)

	obs = env.reset()
	tic = datetime.now()
	print("Training your agent...")
	train(env)

	asyncio.run(env.post_status("done"))
	toc = datetime.now()
	print(toc-tic)
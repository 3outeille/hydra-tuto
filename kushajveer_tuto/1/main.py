### main.py

import hydra
import logging
import os
from omegaconf import DictConfig

logger = logging.getLogger(__name__)

@hydra.main(config_path="config", config_name="config")
def func(cfg: DictConfig):
    logger.debug("Debug level message")
    logger.info("Info level message")
    logger.warning("Warning level message")

    orig_cwd = hydra.utils.get_original_cwd()
    print(orig_cwd)
    # Read file
    path = f"{orig_cwd}/test.txt"
    print(path)

    with open(path, "r") as f:
        print(f.read())

    # Write file
    path = f"output.txt"
    with open(path, "w") as f:
        f.write("This is a dog")

if __name__ == "__main__":
    func()

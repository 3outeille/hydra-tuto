import hydra
from omegaconf import DictConfig

@hydra.main(config_path="config", config_name="config")
def main_func(cfg: DictConfig):
    server_address = cfg.server.address
    print(f"The server address = {server_address}")

if __name__ == "__main__":
    main_func()

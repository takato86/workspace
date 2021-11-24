import hydra
from omegaconf import DictConfig


@hydra.main(config_path=".", config_name="config")
def main(cfg: DictConfig):
    cwd = hydra.utils.get_original_cwd()
    print(cwd)
    print(cfg)


if __name__ == "__main__":
    main()

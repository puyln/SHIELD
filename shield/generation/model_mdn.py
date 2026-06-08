from cdm.mdn.util import instantiate_from_config
from omegaconf import OmegaConf
import torch 

## define mdn model 
config = OmegaConf.load("./config.yaml")
model = instantiate_from_config(config.model)




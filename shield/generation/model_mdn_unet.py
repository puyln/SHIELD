

from guided_diffusion.unet_mdn import UNetModel

from cdm.mdn.util import instantiate_from_config
from omegaconf import OmegaConf
from cdm.mdn.models.diffusion.ddim import DDIMSampler

## initialize the MDN model
config = OmegaConf.load("config")
mdn_model = instantiate_from_config(config.model)
## load mdn training weight
mdn_model.load_state_dict("")

## define ddim sampler
sampler = DDIMSampler(model=mdn_model)

## define unet with cross-conditioned embedding
model = UNetModel(image_size=256, in_channels=2,
            model_channels=96, out_channels=2, 
            num_res_blocks=1, attention_resolutions=[32,16,8],
            channel_mult=[1, 1, 2, 2])


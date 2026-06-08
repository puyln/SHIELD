
from guided_diffusion.unet_raw import UNetModel
from utils.patch_masking import mask_func
import torch


## define mrm model
model = UNetModel(image_size=256, in_channels=2,
                  model_channels=96, out_channels=2, 
                  num_res_blocks=1, attention_resolutions=[32,16,8],
                  channel_mult=[1, 1, 2, 2])

mask_input = torch.rand(1, 2, 256, 256)

## perform random masking
mask_output, _ = mask_func(mask_input, 2, 0.75, [16, 16], [16, 16])

model_output = model(mask_output)



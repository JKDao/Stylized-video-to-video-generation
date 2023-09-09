# Interactive Video Stylization Using Few-Shot Patch-Based Training

This is a demo that showcases the ability of the algorithm proposed in 
this SIGGRAPH 2020 paper: [Interactive Video Stylization Using Few-Shot Patch-Based Training](https://ondrejtexler.github.io/res/Texler20-SIG_patch-based_training_main.pdf)
to transfer the style generated from Stable Diffusion for a few keyframes to the rest of the video.

## Img2Img Settings

To run this demo, you should first run the Stable Diffusion WebUI to generate the style for the video.
For this example, we already provided the generated images in `examples/fspbt/woman_dance/output/` folder.
But if you want to generate your own style, the following can serve as a reference for the Img2Img settings:

```yaml
model: inpainting model (https://huggingface.co/runwayml/stable-diffusion-inpainting)

i2i denoising strength: 0.5

conditioning mask strength: 0.5

prompt: a woman, digital character illustration, 
        anime key visual trending pixiv fanbox by 
        wlop and greg rutkowski and makoto shinkai 
        and studio ghibli

```

## Configuration
The official Github repository is available [here](https://github.com/OndrejTexler/Few-Shot-Patch-Based-Training).
You are supposed to clone this repository to this directory:

```shell
git clone https://github.com/OndrejTexler/Few-Shot-Patch-Based-Training.git
```

If you use the original codebase, there might be some problems when installing the dependencies. If so, you will have make some minor changes to the code to make it work as Tensorflow 1.15 is not supported anymore
and Pytorch has already had TensorBoard integrated. Specifically, you'll need to replace the `Logger` class in logger.py
to the following equivalent code:

```python
from torch.utils.tensorboard import SummaryWriter
import os
import shutil


class Logger(object):
    def __init__(self, log_dir, suffix=None):
        """Create a summary writer logging to log_dir."""
        if suffix is None:
            self.writer = SummaryWriter(log_dir)
        else:
            self.writer = SummaryWriter(log_dir, filename_suffix=suffix)

    def scalar_summary(self, tag, value, step):
        """Log a scalar variable."""
        self.writer.add_scalar(tag, value, step)
```
In this way, Tensorflow can be removed from the dependencies.

**For convenience, I have also provided a modified version of the code** by forked the original repository, and it is
available in the `fspbt_src` folder.

After that, run the following command to install the dependencies:
```shell
pip install -r requirements.txt
```
Then you are good to go.

## Preprocessing

You should arrange your data in the following structure:
```
── {project_name}
   ├── {process_name}_gen
   │   ├── input_filtered
   │   └── whole_video_input
   └── {process_name}_train
       ├── input_filtered
       └── output
```

* `{projectName}` : The name of your project, e.g. "woman_dance".
* `{process_name}_gen/input_filtered` : Put raw frames that are not keyframes, 10 is enough to observe the effect during training.
* `{process_name}_gen/whole_video_input` : Put all raw video frames. It is used to final generation.
* `{process_name}_train/input_filtered` : Put raw keyframe images.
* `{process_name}_train/output` : Put generated keyframe images by stable diffusion's image-to-image. Image names should be the same as input_filtered.

For you to run the demo, we have already prepared a `woman_dance` dataset in the `woman_dance` folder. Everything is organized in the above structure,
except for the masks.

FSPBT allows user to use masks to control the part of the image that will be stylized, but for this demo, we want to keep it minimized, 
so we simply leave them empty by running:

```shell
python gen_empty_masks.py
```
Then, you are ready to run the demo.

If you are interested in preprocessing your own data, the `woman_dance/preprocess` directory can serve as a reference.


## Training

To train the model, run the following command:
```shell
$ cd fspbt_src
$ python train.py --config "_config/reference_P.yaml" --data_root {train_dir} --log_interval 2000 --log_folder logs_reference_P
```
where {train_dir} is the path to the training data directory. In our case, it could be `../woman_dance/woman_train`.
You can also change the configuration file to train the model with different parameters. You can find more preset configuration files
in `fspbt_src/_config/`.

## Testing

After training, you will have your model saved in the `logs_reference_P` folder. To test the model, run the following command:
```shell
cd fspbt_src
MODEL_PATH="../woman_dance/logs_reference_P/model_00020.ckpt" 
GEN_DIR="../woman_dance/woman_gen/" 
OUTPUT_PATH="${GEN_DIR}/whole_video_output"
python generate.py --checkpoint $MODEL_PATH --data_root $GEN_DIR --dir_input whole_video_input --outdir $OUTPUT_PATH --device "cuda:0"
```
Then you will find the generated frames in your `whole_video_output` folder, you can use them to generate the final video with:
```shell
python gen_video.py
```

Note that this is just an naive demo that lacks many features, such as:
1. Using some tools to eliminate the distortion of the generated frames, such as FaceEdit.
2. Using the optical flow and temporal consistency tools provided in the original repository to improve the quality of the generated video.
3. Did not apply any refinement to the keyframes, such as color correction.
4. Using only 6 keyframes to train (for the sake of simplicity), which is far from enough to generate a good style.

However, this demo has already shown the ability of the algorithm to transfer the style from keyframes to the rest of the video in an efficient way,
which provides a good starting point for further development.




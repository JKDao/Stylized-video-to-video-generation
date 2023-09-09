# Quickr-V2

In this version, we have developed our workflow by building upon the existing codebase from Deforum-art. 
They offer a powerful interface and a wide range of robust utilities for us to leverage. We reused some of their
video processing code and added our own algorithms to the workflow.
This workflow serves as an extension of the AUTOMATIC1111/Stable-Diffusion-WebUI.

## How to use
To utilize the entire workflow, you need to set up a complete pipeline for Stable Diffusion and its WebUI (will introduce in the next section). 
This process involves numerous options and buttons to choose from, making deployment and usage more complex. 
Additionally, to run the entire pipeline, you must have a GPU with at least 8GB of memory. 
For video processing with controlNet, a minimum of 24GB of CPU memory is also required (based on my own experience, 
I initially used a 16GB CPU memory, and it failed to load the controlNet model).

**To facilitate easier testing of our code by the Professor/TA**, we have created an example folder 
containing some scripts. These python scripts demonstrate our key algorithms and illustrate 
how we rapidly prototype our ideas. The extension is built to provide the internal algorithms with a graphical
user interface and an integration with Stable Diffusion configurations.

### Example (🌟 Easy-to-run training scripts for TA/Professor to test our code)

The `fspbt` folder consists of the code and the data needed for a simple run of the Few-Shot Patch-Based Training algorithm.
There is another README.md file in the folder that explains how to run the code.

### Deployment (🤖️ For serious users with decent GPU and CPU memory)

1. Install the AUTOMATIC1111/Stable-Diffusion-WebUI. 
   Please refer to the [official repository](https://github.com/AUTOMATIC1111/stable-diffusion-webui/) for guidance. Note that this repo is updating frequently, so for your reference we are using commit `22bcc7be`.
2. Install our extension. You can put this directory to the `extensions` folder of the Stable Diffusion WebUI, or you can open your WebUI and install for URL under the `Extension` tab.
![Installation](https://user-images.githubusercontent.com/32998901/233818333-49220bea-0472-4563-8b8d-c4074b6d4fde.png)
3. After reloading the window, you should be able to see `Quickr` tab on the top bar. Click on it and you will see the interface of our extension:
![Quickr](https://user-images.githubusercontent.com/32998901/234482813-e590bf4e-f133-4c31-97f7-cee678c6850c.png)
   This example is the setting of our stage 5: training FSPBT. For the meaning of each input box, please refer to the [official repository](https://github.com/OndrejTexler/Few-Shot-Patch-Based-Training), or our [example folder](./examples/fspbt/README.md).
4. The usage of each stage is shown on the right. You can tune configs for each stage on the left, and select one stage and click 'Generate' on the right once you finish configuring one stage. For step 3, you should go back to the `img2img` tab, and select `Quickr Script` in `Script` dropdown menu. Then you can tune your configuration for Quickr and img2img and run the script there.
![Quickr Script](https://user-images.githubusercontent.com/32998901/234483987-21b2aaaa-c9bd-4ac9-af0d-5e69769c4701.png)

# Audio Generation Pipeline

The acompanied Jupyter Notebook demonstrates how we did the technical part, here we briefly summarize how the audio generation pipeline works in our project with an example.

1. We first get a select number of keyframes from the video based on the frequency given by the user. By default it selects only 1 key frame from the entire video which is usually in the middle of the video. Let’s say the selected key frame is as follows.

![frame_0046](https://user-images.githubusercontent.com/32998901/235375920-10c297ea-19ce-473a-89d9-bcc29007268e.png)

2. Then we get the caption for this image using the ViT-GPT2 image captioning model:
*“['a young girl is standing on a sidewalk']”*.

3. Then we create a prompt and feed it into GPT-4 to get the music style: 
   * **Without any user prompt**: *Charming, playful indie-pop reflecting youthful curiosity and city life.* **Given the user prompt** (“Japanese traditional music”): *Playful indie-pop infused with traditional Japanese instruments and melodies.*

4. Then we pass these prompts to the Riffusion mode and the ouptuts are as follows
   * **Without any user prompt**: https://drive.google.com/file/d/1UExpsZ8zPtKK6NjHM422K3ywRwLLAvFI/view?usp=sharing
   * **Given the user prompt**: https://drive.google.com/file/d/1uy_DZnCvw-YbafEnYpiEyOk_TI6Hmp8B/view?usp=sharing



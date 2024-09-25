import os
import requests
import openai 

openai.api_key = os.environ.get("OPENAI_API_Key")

def UseDALLe_then_save_Image(prompt, file_path):

    response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024")
    image_url = response.data[0].url
    image_data = requests.get(image_url).content
    
    with open(file_path, 'wb') as file:
        file.write(image_data)
    print(f"Image saved to {file_path}")

prompts = ['a photo of a unhealthy man', 'a photo of a woman with good discipline']
for i, prompt in enumerate(prompts):
    file_path = f"images/{i}_image.png"
    UseDALLe_then_save_Image(prompt, file_path)
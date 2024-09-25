import os
from dotenv import load_dotenv
import requests
import openai 
load_dotenv()

def path_finder(prompt):

    working_directory = os.getcwd()
    negative_paths = os.path.join(working_directory,'images', 'negative_prompts')
    positive_paths = os.path.join(working_directory, 'images','positive_prompts')

    negative_subdirectories = list(sorted([os.path.join(negative_paths, subfolder) for subfolder in os.listdir(negative_paths) if os.path.isdir(os.path.join(negative_paths, subfolder))]))
    positive_subdirectories = list(sorted([os.path.join(positive_paths, subfolder) for subfolder in os.listdir(positive_paths) if os.path.isdir(os.path.join(positive_paths, subfolder))]))
    all_subdirectories = negative_subdirectories + positive_subdirectories
    all_prompts = [subdirectory.split('/')[-1].split('_')[-1] for subdirectory in all_subdirectories]
    mapping_dic = dict(zip(all_prompts, all_subdirectories))
    return prompt, mapping_dic[prompt]

openai.api_key = os.getenv('OPENAI_API_KEY')

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

prompt = 'impure'
n_images = 100

selected_prompt, corresponding_path = path_finder(prompt)

for i in range(n_images):

    file_path = f"{corresponding_path}/{i+1}_{prompt}.png"
    print(file_path)
    prompt_dalle = f'a photo of a person who is {prompt}'
    UseDALLe_then_save_Image(prompt_dalle, file_path)
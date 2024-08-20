from PIL import Image
import chromadb
from chromadb.utils.data_loaders import ImageLoader
from transformers import CLIPProcessor, CLIPModel
import numpy as np
import torch
from tqdm import tqdm
import os

# Function to get image embeddings using Hugging Face's CLIP model
def get_single_image_embeddings(img_np):
    # Load the CLIP model and processor
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    
    # Convert the numpy image to PIL Image
    img_pil = Image.fromarray(img_np)
    
    # Process the image to create inputs for the model
    inputs = processor(images=img_pil, return_tensors="pt")
    
    # Generate embeddings using the CLIP model
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)
    
    # Return the embedding as a numpy array
    return image_features.cpu().numpy().flatten()

# Function to get file paths of all images in the specified folder
def get_files_path(folder_path):
    files_path = []
    for class_name in os.listdir(folder_path):
        path_class_name = os.path.join(folder_path, class_name)
        for img_name in os.listdir(path_class_name):
            files_path.append(os.path.join(path_class_name, img_name))
    
    return files_path

# Function to add images and their embeddings to the collection
def add_images_to_collection(collection: chromadb.Collection, files_path):
    ids_path = []
    embeddings = []
    for id, file_path in tqdm(enumerate(files_path), desc="Creating Image Embeddings and Adding to DB"):
        try:
            img_np = np.array(Image.open(file_path)).astype(np.uint8)
            embedding_img = get_single_image_embeddings(img_np)
            ids_path.append(f"id_{id}")
            embeddings.append(embedding_img.tolist())
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    collection.add(ids=ids_path, embeddings=embeddings)

# Main code
db_path = r"D:\Python\Text_Image_Retrieval-Streamlit\database"
image_loader = ImageLoader()
client = chromadb.PersistentClient(path=db_path)

# Since we're using Hugging Face's CLIP model, we don't need the embedding_function in the collection creation
collection = client.get_or_create_collection(
    name='multimodal_collection',
    data_loader=image_loader
)

ROOTS = r"D:\Python\Text_Image_Retrieval-Streamlit\data\train"
files_path = get_files_path(ROOTS)

add_images_to_collection(collection, files_path)

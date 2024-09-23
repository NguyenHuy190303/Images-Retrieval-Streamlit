# Test Image Retrieval

This project demonstrates content-based image retrieval using Streamlit and ChromaDB.

## Project Setup

### Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/NguyenHuy190303/Images-Retrieval-Streamlit
```

### Navigate to the Project Directory

```bash
cd Images-Retrieval-Streamlit
```

### Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Setup and Running [`create_images_db.py`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FPython%2FText_Image_Retrieval-Streamlit%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A31%2C%22character%22%3A22%7D%7D%5D%2C%2299b6edb5-ccaf-4008-b703-4ec8b400d90e%22%5D "Go to definition")

This script is used to set up the ChromaDB and process the training dataset.

### 1. Set Up Directory Paths

Before running the script, ensure you have the following directories set up on your system:

- **Training Dataset**: Store your images in the directory specified by the [`ROOTS`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FPython%2FText_Image_Retrieval-Streamlit%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A39%2C%22character%22%3A77%7D%7D%5D%2C%2299b6edb5-ccaf-4008-b703-4ec8b400d90e%22%5D "Go to definition") variable.
- **Database Path**: The ChromaDB database will be stored in the directory specified by the [`db_path`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FPython%2FText_Image_Retrieval-Streamlit%2Fcomponents%2Finit.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A8%2C%22character%22%3A2%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FPython%2FText_Image_Retrieval-Streamlit%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A40%2C%22character%22%3A93%7D%7D%5D%2C%2299b6edb5-ccaf-4008-b703-4ec8b400d90e%22%5D "Go to definition") variable.

### 2. Update the Script

Open [`create_images_db.py`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FPython%2FText_Image_Retrieval-Streamlit%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A31%2C%22character%22%3A22%7D%7D%5D%2C%2299b6edb5-ccaf-4008-b703-4ec8b400d90e%22%5D "Go to definition") and update the following variables:

```python
# Path to your training dataset
ROOTS = r"D:\Python\Text_Image_Retrieval-Streamlit\data\train"

# Path to where the ChromaDB will be created/stored
db_path = r"D:\Python\Text_Image_Retrieval-Streamlit\database"
```

### 3. Initialize and Embed Vectors in ChromaDB

Run the script to initialize and embed vectors in the ChromaDB:

```bash
python create_images_db.py
```

## Run Streamlit Application

Once the database is set up, you can run the Streamlit application:

```bash
streamlit run main.py
```

## Usage

The application provides a web interface to perform content-based image retrieval. You can upload an image, and the application will return similar images from the dataset.

## License

This project is licensed under the MIT License.
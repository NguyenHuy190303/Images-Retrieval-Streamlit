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

## Setup and Running `create_images_db.py`

This script is used to set up the ChromaDB and process the training dataset.

### 1. Set Up Directory Paths

Before running the script, ensure you have the following directories set up on your system:

- **Training Dataset**: Store your images in the directory specified by the `ROOTS` variable.
- **Database Path**: The ChromaDB database will be stored in the directory specified by the [`db_path`](command:_github.copilot.openSymbolInFile?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FPython%2FText_Image_Retrieval-Streamlit%2Fcomponents%2Finit.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22db_path%22%2C%22887d6a5f-f922-43e5-8e1f-7e17ebab57c1%22%5D "d:\Python\Text_Image_Retrieval-Streamlit\components\init.py") variable.

### 2. Update the Script

Open `create_images_db.py` and update the following variables:

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

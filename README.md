# QA_with_PDF_RAG

## Overview
QA_with_PDF_RAG is a project that builds a basic Retrieval-Augmented Generation (RAG) program. The program is applied to document-based question answering for educational materials. It uses the LangChain library, which is designed specifically for building applications involving Large Language Models (LLMs). After developing the RAG program, it is integrated into a chat interface to create a complete chat application. The chat interface is built using the Chainlit library.

## Purpose
The purpose of this repository is to provide a robust framework for extracting information from PDF or text documents and enabling interactive question answering through a conversational interface. This can be particularly useful for educational purposes, allowing users to upload their study materials and ask questions to get answers.

## Installation on Local Machine

1. **Clone the repository**
    ```bash
    git clone https://github.com/PUVHAM/QA_with_PDF_RAG.git
    cd QA_with_PDF_RAG
    ```

2. **Set up a conda environment**
    ```bash
    conda create -n qawithpdfrag python=3.9
    conda activate qawithpdfrag
    ```

3. **Install the required dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up GPU for TensorFlow**
    - Follow the instructions [here](https://www.tensorflow.org/install/pip) to install TensorFlow with GPU support.

5. **Run Chainlit to start the application**
    ```bash
    chainlit run app.py
    ```
  
## Using Google Colab with Free GPU and Ngrok

1. **Open file `rag_with_ui.ipynb` in Google Colab and enable the free T4 GPU**
   - Click on **Runtime** in the top menu, then select **Change runtime type**.
   - In the dialog that appears, choose **T4 GPU** from the **Hardware accelerator** dropdown.
   - Click **Save**

2. **Upload necessary files**
    - Upload `app.py`, `file.py`, `llm.py`, `vector.py`, and `requirements.txt` to the Colab notebook.
  
3. **Install dependencies**
    - In the first code cell, run:
      ```bash
      !pip install -q -r requirements.txt
      !pip install -q pypdf
      ```
4. **Run the application**
    - In the next code cell, run:
      ```python
      !python app.py
      ```
5. **Using Ngrok to Expose Local Server to the Internet**
    - Add a new code cell and follow these steps:
      ```python
      !pip install pyngrok -q
      from pyngrok import ngrok
      ```
6. **Authenticate Ngrok**
    - Go to [ngrok.com](https://ngrok.com/), create an account, and log in.
    - Go to Your Authtoken, copy your authtoken.
    - Back in Colab, add a new code cell and run:
      ```python
      !ngrok config add-authtoken "your-authtoken"
      public_url = ngrok.connect(8000).public_url
      print(public_url)
      ```
7. **Run the Chainlit app**
    - After running the previous cells, add a new code cell and run:
      ```python
      !chainlit run app.py
      ```
    - Once it displays `http://localhost:8000`, click on the `public_url` printed above.

## Usage

* Upon starting, you will be prompted with a welcome message.
* Upload a PDF or text file.
* Ask questions about the content of the uploaded file.

## Files in the Repository
* `app.py`: Main application script
* `file.py`: File processing script
* `llm.py`: Script to get HuggingFace language model
* `vector.py`: Script to get vector database
* `requirements.txt`: List of dependencies

## Acknowledgments
* Special thanks to the contributors of LangChain and Chainlit libraries.
* Inspired by the advancements in NLP and RAG models.

Feel free to customize this template further to suit your project's specific requirements. Happy coding!

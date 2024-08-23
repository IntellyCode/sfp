# PDF Abstract Extractor

This project provides a tool for reading PDF files, extracting abstracts from them, and saving the abstracts along with the titles of the papers to a text file. It uses the PyMuPDF library for processing PDF documents and custom classes to extract relevant information.

## Features

- Extracts bold text (assumed to be titles) from introductory pages.
- Finds and extracts abstracts based on specified keywords.
- Saves the extracted data to a text file.

## Requirements

- Python 3.x
- PyMuPDF (`pymupdf` library)
- `logging` (included with Python)

## Installation

1. **Clone the Repository**: Download or clone the source code from GitHub. If you are not familiar with GitHub, you can manually download the ZIP file of the repository.

   - To clone the repository, run:
     ```sh
     git clone https://github.com/yourusername/pdf-abstract-extractor.git
     ```
   - Alternatively, download the ZIP file from the GitHub repository page and extract it.

2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

   ```sh
   cd path/to/pdf-abstract-extractor

## Usage
To run the program create a /data and /output directories in the project directory. To the /data directory add your pdf file. Open the config.json file and adjust the pdf_path and output_path variables by changing only the file part. You can then run main.py using a python interpreter. 

## Troubleshooting

- File Not Found: Ensure that the path to the PDF file is correct and that the file exists.
- Dependency Issues: Verify that all required libraries are installed.
    ```sh
      pip install requirements.txt
  
## License

This project is licensed under the MIT License. See the LICENSE file for details.


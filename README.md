# File Organizer with GUI

This Python application allows you to easily organize files in a folder based on their extensions. The application uses a graphical user interface (GUI) built with `tkinter`. Users can select multiple files and the program will automatically move them into folders named after their respective file extensions (e.g., `.txt` files into a `txt` folder, `.pdf` files into a `pdf` folder, etc.).

## Features

- Select multiple files from your computer.
- Automatically organize files based on their extensions.
- Create a new folder for each file extension (if not already present).
- Simple and user-friendly GUI with `tkinter`.

## Requirements

Before running the application, make sure you have Python installed. This program also requires the `tkinter` library (which is usually included by default with Python).

- Python 3.x
- `tkinter` (usually included with Python)

## Installation

1. Clone or download this repository to your local machine.
2. Make sure you have Python 3.x installed. You can check this by running:
   ```bash
   python --version
   ```
   If you don’t have Python installed, download and install it from the official [Python website](https://www.python.org/downloads/).

3. Ensure `tkinter` is available (it should be included by default with Python). If you face any issues, you can install it using:
   ```bash
   pip install tk
   ```

## Usage

1. Run the Python script:
   ```bash
   python file_organizer.py
   ```

2. The application window will appear. Click the **"Click here to upload files"** button.
   - You can select multiple files of any type (e.g., `.txt`, `.pdf`, `.jpg`, etc.).
   
3. After selecting the files, choose a target folder where you want the files to be organized.
   
4. The program will create folders based on file extensions (e.g., `.txt` files will be moved into a folder named `txt`, `.jpg` files will go into a `jpg` folder, and so on).

5. Once the files are organized, you will receive a success message. If an error occurs, an error message will be shown.

## Example

If you have the following files:
- `document1.txt`
- `image1.jpg`
- `music.mp3`
- `document2.txt`

After running the program and selecting the target folder, the program will organize them into the following structure:
```
target_folder/
├── txt/
│   ├── document1.txt
│   └── document2.txt
├── jpg/
│   └── image1.jpg
└── mp3/
    └── music.mp3
```

## License

This project is open source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Troubleshooting

- **tkinter not installed**: If you encounter issues related to `tkinter`, make sure it's installed. For Windows, `tkinter` is usually included by default with Python. On Linux or Mac, it might require additional installation (`sudo apt-get install python3-tk` or `brew install python-tk`).
- **No files selected**: Make sure you select files before proceeding. The program will prompt a warning if no files are selected.

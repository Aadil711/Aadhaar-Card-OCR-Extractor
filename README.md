# 🤖 Aadhaar Card OCR Extractor

A smart Python script that uses **Optical Character Recognition (OCR)** to automatically detect and extract structured information like **Aadhaar Number**, **Date of Birth**, and **Gender** from Aadhaar card images.

> ⚠️ **Disclaimer:** This project is intended for **educational purposes only** to demonstrate OCR and Regex-based information extraction. Handle all personal data **responsibly and ethically**.

---

## ✨ Features

- **Structured Data Extraction:** Intelligently extracts:
  - Aadhaar Number
  - Date of Birth
  - Gender
- **Dual Input Modes:**
  - **Live Scan**: Use your webcam for real-time scanning.
  - **File Upload**: Process existing image files (`.jpg`, `.png`, etc.).
- **Accurate Parsing:** Utilizes Regular Expressions (Regex) for format validation.
- **Data Export:** Automatically saves extracted details into a clean `.csv` file.
- **User-Friendly:** Simple command-line interface with interactive prompts.

---

## 📸 Demo

> 💡 *Tip: Add a screen-recorded GIF (via [ScreenToGif](https://www.screentogif.com/) or [Kap](https://getkap.co/)) demonstrating both webcam and image file input modes here.*

---

## 🧰 Tech Stack & Dependencies

| Tool        | Purpose                                         |
|-------------|-------------------------------------------------|
| OpenCV      | Image processing & webcam capture               |
| Pytesseract | OCR (wrapper for Google Tesseract)              |
| Pandas      | CSV creation and structured data handling       |
| Regex (`re`)| Pattern recognition for Aadhaar/DOB/Gender data |

---

## 🛠️ Installation & Setup

Follow these steps to get started:

### 1. Install Tesseract-OCR

#### Windows
- Download and install from [Tesseract-OCR Windows Installer](https://github.com/tesseract-ocr/tesseract/wiki#windows).
- Note the installation path (e.g., `C:\Program Files\Tesseract-OCR`).

#### macOS
```bash
brew install tesseract
```

#### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install tesseract-ocr
```

---

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

### 3. Create a Virtual Environment (Recommended)
```bash
# Create the environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

---

### 4. Install Python Libraries
Make sure you have a `requirements.txt` file containing:
```
opencv-python
pytesseract
pandas
```

Then run:
```bash
pip install -r requirements.txt
```

---

### 5. Configure Tesseract Path (Windows Only)
In your script, set the Tesseract path:
```python
# Example for Windows users:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 🚀 Usage

Make sure you're in the project directory and the virtual environment is active:

```bash
python text_extraction.py
```

> 🔁 *Rename your script to `main.py` or `app.py` for better clarity.*

### You'll be prompted to:
- Press `1` for **webcam scan**:
  - An OpenCV window opens.
  - Point your webcam at the Aadhaar card.
  - Press `'s'` to scan or `'q'` to quit.
- Press `2` for **image file upload**:
  - Enter the full path to your image file.

### Output:
- Console displays extracted raw text and a structured dictionary.
- If valid data is found, it’s saved to `aadhaar_details.csv`.

---

## 📁 Project Structure

```
.
├── text_extraction.py                # Main script (rename accordingly)
├── aadhaar_details.csv    # Output file (generated after run)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🐞 Troubleshooting

- **Tesseract not found?**
  - Double-check your `tesseract_cmd` path.
  - Make sure Tesseract is added to system PATH or referenced explicitly in the script.

- **Incorrect OCR output?**
  - Ensure high-quality images.
  - Try increasing contrast or resizing images using OpenCV filters.

- **Regex not matching?**
  - Check if the card layout or font style is unusual.
  - Test with another Aadhaar card sample.

---

## 👨‍💻 Contributors

| Name             | Role          |
|------------------|---------------|
| Your Name Here   | Creator & Developer |

> Want to contribute? Feel free to fork the repo and open a pull request!

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 🙏 Acknowledgments

- Thanks to the amazing open-source communities behind:
  - [OpenCV](https://opencv.org/)
  - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
  - [Pandas](https://pandas.pydata.org/)

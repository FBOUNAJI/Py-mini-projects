# QR Code Generator

A simple **Python QR code generator** that converts a URL or text into a PNG QR code using the **PyQRCode** library.

The user enters a URL or text, chooses an output filename, and the program generates and saves the QR code as a PNG image.

## 🚀 Features

* 🔗 Generate a QR code from a URL or text
* 📝 Get data from user input
* 📁 Choose a custom output filename
* 🖼️ Save the QR code as a PNG image
* ✅ Validate empty input
* 🔍 Automatically add the `.png` extension if needed

## 🛠️ Technologies Used

* **Python**
* **PyQRCode**
* **PyPNG**

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/qr-code-generator.git
```

Go to the project folder:

```bash
cd qr-code-generator
```

Install the required libraries:

```bash
pip install PyQRCode pypng
```

## ▶️ How to Run

Run the Python file:

```bash
python app.py
```

Enter a URL or text when prompted:

```text
Enter the URL: https://github.com/
```

Choose an output filename:

```text
Enter output filename (default: myqr.png): github.png
```

Example output:

```text
QR code generated successfully as 'github.png'.
```

The generated QR code will be saved in the project folder as a PNG image.

## 📚 What I Learned

Through this project, I practiced:

* Getting user input with Python
* Validating user input
* Working with strings
* Using conditional statements
* Checking file extensions with `.endswith()`
* Using an external Python library
* Generating QR codes
* Saving files programmatically

## 🔮 Future Improvements

Possible improvements for future versions:

* Add support for different QR code sizes
* Allow users to choose the QR code scale
* Add different image formats
* Create a graphical user interface
* Add error handling
* Allow users to generate multiple QR codes

## 📄 License

This project is for learning and educational purposes.

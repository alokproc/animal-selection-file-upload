# 🚀 VS Code Setup Guide - Animal Selection & File Upload App

## 📋 Prerequisites
- **Python 3.8+** installed on your system
- **VS Code** installed
- **Python extension** for VS Code (install from Extensions marketplace)

## 🛠️ Step-by-Step Setup

### 1. Open Project in VS Code
```bash
# Extract the project files to your desired location
# Open VS Code and use "File > Open Folder" to open the project directory
```

### 2. Set Up Python Virtual Environment
Open VS Code terminal (`Ctrl+`` ` or `View > Terminal`) and run:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure VS Code Python Interpreter
1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "Python: Select Interpreter"
3. Choose the interpreter from your `venv` folder:
   - Windows: `./venv/Scripts/python.exe`
   - macOS/Linux: `./venv/bin/python`

### 4. Run the Application
In the VS Code terminal:
```bash
# Make sure virtual environment is activated
python src/main.py
```

### 5. Access the Application
- Open your browser and go to: `http://localhost:5000`
- The application will be running with both animal selection and file upload features

## 🎯 VS Code Features You Can Use

### Debug Configuration
- Set breakpoints in Python files by clicking on line numbers
- Use `F5` to start debugging
- The Flask app will run in debug mode automatically

### Extensions Recommendations
- **Python** (Microsoft) - Essential for Python development
- **Flask Snippets** - Helpful Flask code snippets
- **HTML CSS Support** - Better HTML/CSS editing
- **Live Server** - For frontend development (optional)

### File Structure in VS Code
```
animal-file-app-vscode/
├── src/
│   ├── main.py              # 🐍 Main Flask app - START HERE
│   ├── routes/
│   │   ├── animal_file.py   # 🐾 Animal & file upload routes
│   │   └── user.py          # 👤 User routes (template)
│   ├── models/
│   │   └── user.py          # 🗄️ Database models
│   ├── static/
│   │   ├── index.html       # 🌐 Frontend application
│   │   └── images/          # 🖼️ Animal images
│   └── uploads/             # 📁 Uploaded files storage
├── requirements.txt         # 📦 Dependencies
├── README.md               # 📖 Documentation
└── VS_CODE_SETUP.md       # 🚀 This file
```

## 🧪 Testing the Features

### Animal Selection
1. Click on Cat, Dog, or Elephant checkboxes
2. Beautiful animal images will appear
3. Only one animal can be selected at a time

### File Upload
1. Click on the upload area or drag & drop a file
2. File metadata will be displayed (name, size, type)
3. Files are saved in the `src/uploads/` folder

## 🔧 Development Tips

### Making Changes
- **Backend changes**: Modify files in `src/routes/` or `src/main.py`
- **Frontend changes**: Edit `src/static/index.html`
- **Styling**: CSS is embedded in the HTML file
- **JavaScript**: Also embedded in the HTML file

### Auto-Reload
The Flask app runs in debug mode, so it will automatically reload when you make changes to Python files.

### Adding New Features
- Add new routes in `src/routes/animal_file.py`
- Modify the frontend in `src/static/index.html`
- Add new static files in `src/static/`

## 🐛 Troubleshooting

### Common Issues
1. **Port already in use**: Change port in `src/main.py` (line with `app.run()`)
2. **Module not found**: Make sure virtual environment is activated
3. **Permission errors**: Run VS Code as administrator (Windows) or check file permissions

### Checking if Everything Works
1. Terminal should show: `Running on http://127.0.0.1:5000`
2. Browser should load the application with purple gradient background
3. Animal selection should show images
4. File upload should display file information

## 🎉 You're Ready!
Your Animal Selection & File Upload application is now ready to run in VS Code. Happy coding! 🚀


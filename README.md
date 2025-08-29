# Animal Selection & File Upload Web Application

A modern, responsive web application built with Flask backend and vanilla HTML/CSS/JavaScript frontend that allows users to select animals and view their images, as well as upload files and view their metadata.

## Features

### 🐾 Animal Selection
- Choose from three animals: Cat, Dog, or Elephant
- Beautiful high-quality images displayed for each selection
- Only one animal can be selected at a time
- Smooth animations and transitions

### 📁 File Upload
- Drag and drop file upload support
- Click to select file functionality
- File metadata display including:
  - File name
  - File size (formatted for readability)
  - File type/extension
  - MIME type
- Support for multiple file types (max 16MB)
- Real-time upload progress and status

### 🎨 Design Features
- Modern gradient background
- Responsive design (works on desktop and mobile)
- Clean, professional UI with rounded corners and shadows
- Hover effects and smooth transitions
- Loading states and error handling

## Technology Stack

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Werkzeug** - File upload handling and security

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with flexbox/grid
- **JavaScript (ES6+)** - Interactive functionality
- **Fetch API** - Asynchronous HTTP requests

## Project Structure

```
animal-file-app/
├── src/
│   ├── main.py                 # Flask application entry point
│   ├── routes/
│   │   ├── user.py            # User management routes (template)
│   │   └── animal_file.py     # Animal selection and file upload routes
│   ├── models/
│   │   └── user.py            # Database models (template)
│   ├── static/
│   │   ├── index.html         # Frontend application
│   │   ├── favicon.ico        # Website icon
│   │   └── images/            # Animal images
│   │       ├── cat.jpg
│   │       ├── dog.jpg
│   │       └── elephant.jpg
│   ├── uploads/               # Uploaded files storage
│   └── database/              # SQLite database
├── venv/                      # Python virtual environment
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## API Endpoints

### Animal Selection
- **POST** `/api/animal`
  - Request: `{"animal": "cat|dog|elephant"}`
  - Response: `{"success": true, "image_path": "/static/images/animal.jpg", "animal": "selected_animal"}`

### File Upload
- **POST** `/api/upload`
  - Request: FormData with file
  - Response: `{"success": true, "file_info": {...}}`

### Health Check
- **GET** `/api/health`
  - Response: `{"status": "healthy", "message": "Animal File API is running"}`

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd animal-file-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python src/main.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5000`

## Usage

1. **Select an Animal**: Click on any of the three animal checkboxes (Cat, Dog, Elephant) to see a beautiful image of that animal.

2. **Upload a File**: 
   - Click on the upload area or drag and drop a file
   - View the file metadata including name, size, type, and MIME type
   - Files are stored in the `src/uploads/` directory

## Configuration

- **Maximum file size**: 16MB (configurable in `animal_file.py`)
- **Allowed file types**: All types supported (configurable in `animal_file.py`)
- **Server host**: 0.0.0.0 (allows external access)
- **Server port**: 5000 (configurable in `main.py`)

## Development

The application uses Flask's development server with debug mode enabled. For production deployment, use a production WSGI server like Gunicorn.

## Browser Support

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (responsive design)

## License

This project is created for educational and demonstration purposes.

## Contributing

Feel free to submit issues and enhancement requests!


import os
from flask import Blueprint, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename

animal_file_bp = Blueprint('animal_file', __name__)

# Configuration for file uploads
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'zip', 'csv', 'xlsx'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@animal_file_bp.route('/animal', methods=['POST'])
def get_animal_image():
    """
    API endpoint to get animal image path based on selection
    Expected JSON: {"animal": "cat|dog|elephant"}
    Returns: {"success": True, "image_path": "/static/images/animal.jpg", "animal": "selected_animal"}
    """
    try:
        data = request.json
        if not data or 'animal' not in data:
            return jsonify({"success": False, "error": "Animal selection required"}), 400
        
        animal = data['animal'].lower()
        if animal not in ['cat', 'dog', 'elephant']:
            return jsonify({"success": False, "error": "Invalid animal selection. Choose cat, dog, or elephant"}), 400
        
        # Return the static image path for the selected animal
        image_path = f"/static/images/{animal}.jpg"
        
        return jsonify({
            "success": True,
            "image_path": image_path,
            "animal": animal
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@animal_file_bp.route('/upload', methods=['POST'])
def upload_file():
    """
    API endpoint to handle file uploads
    Returns file metadata: name, size, type
    """
    try:
        # Check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({"success": False, "error": "No file part in the request"}), 400
        
        file = request.files['file']
        
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            return jsonify({"success": False, "error": "No file selected"}), 400
        
        if file and allowed_file(file.filename):
            # Get file information
            filename = secure_filename(file.filename)
            file_size = len(file.read())
            file.seek(0)  # Reset file pointer after reading for size
            
            # Check file size
            if file_size > MAX_FILE_SIZE:
                return jsonify({
                    "success": False, 
                    "error": f"File too large. Maximum size is {MAX_FILE_SIZE // (1024*1024)}MB"
                }), 400
            
            # Get file type/extension
            file_extension = filename.rsplit('.', 1)[1].lower() if '.' in filename else 'unknown'
            
            # Save file (optional - for demo purposes)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            
            # Format file size for display
            if file_size < 1024:
                size_display = f"{file_size} bytes"
            elif file_size < 1024 * 1024:
                size_display = f"{file_size / 1024:.1f} KB"
            else:
                size_display = f"{file_size / (1024 * 1024):.1f} MB"
            
            return jsonify({
                "success": True,
                "file_info": {
                    "name": filename,
                    "size": size_display,
                    "size_bytes": file_size,
                    "type": file_extension,
                    "mime_type": file.content_type
                }
            })
        
        else:
            return jsonify({
                "success": False, 
                "error": f"File type not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
            }), 400
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@animal_file_bp.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({"status": "healthy", "message": "Animal File API is running"})


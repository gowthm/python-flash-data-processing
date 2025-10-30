# Python Flask API for Data Processing

A RESTful API built with Flask for efficient data processing operations including data transformation, validation, cleaning, and analysis.

## Features

- **Data Upload & Processing**: Upload CSV, JSON, and Excel files for processing
- **Data Transformation**: Convert between different data formats
- **Data Validation**: Validate data against predefined schemas
- **Data Cleaning**: Remove duplicates, handle missing values, and normalize data
- **Data Analysis**: Perform statistical analysis and generate insights
- **RESTful Endpoints**: Clean and intuitive API design
- **Error Handling**: Comprehensive error handling and validation
- **Logging**: Detailed logging for debugging and monitoring

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/python-flash-data-processing.git
   cd python-flash-data-processing
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory with the following variables:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
MAX_CONTENT_LENGTH=16777216  # 16MB max file size
UPLOAD_FOLDER=uploads
```

## Usage

### Starting the Server

```bash
flask run
```

Or with Python:

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check

```http
GET /api/health
```

Returns the API status.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### Upload Data

```http
POST /api/upload
```

Upload a file for processing.

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (CSV, JSON, or Excel file)

**Response:**
```json
{
  "message": "File uploaded successfully",
  "file_id": "abc123",
  "filename": "data.csv"
}
```

### Process Data

```http
POST /api/process
```

Process uploaded data with specified operations.

**Request Body:**
```json
{
  "file_id": "abc123",
  "operations": [
    {
      "type": "clean",
      "params": {
        "remove_duplicates": true,
        "handle_missing": "drop"
      }
    },
    {
      "type": "transform",
      "params": {
        "output_format": "json"
      }
    }
  ]
}
```

**Response:**
```json
{
  "status": "success",
  "processed_data": {...},
  "statistics": {
    "rows_processed": 1000,
    "rows_removed": 50
  }
}
```

### Validate Data

```http
POST /api/validate
```

Validate data against a schema.

**Request Body:**
```json
{
  "file_id": "abc123",
  "schema": {
    "name": {"type": "string", "required": true},
    "age": {"type": "integer", "min": 0, "max": 150},
    "email": {"type": "email", "required": true}
  }
}
```

**Response:**
```json
{
  "valid": true,
  "errors": [],
  "validated_rows": 1000
}
```

### Analyze Data

```http
POST /api/analyze
```

Perform statistical analysis on data.

**Request Body:**
```json
{
  "file_id": "abc123",
  "analysis_type": "descriptive"
}
```

**Response:**
```json
{
  "analysis": {
    "mean": 45.5,
    "median": 43.0,
    "std_dev": 12.3,
    "min": 18,
    "max": 95
  }
}
```

### Download Processed Data

```http
GET /api/download/{file_id}
```

Download processed data.

**Query Parameters:**
- `format`: Output format (csv, json, excel)

**Response:**
- File download

## Project Structure

```
python-flash-data-processing/
├── app.py                  # Main application entry point
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── .gitignore             # Git ignore rules
├── LICENSE                # License file
├── README.md              # This file
├── api/
│   ├── __init__.py
│   ├── routes.py          # API route definitions
│   ├── validators.py      # Data validation logic
│   └── processors.py      # Data processing functions
├── models/
│   ├── __init__.py
│   └── schemas.py         # Data schemas
├── utils/
│   ├── __init__.py
│   ├── file_handler.py    # File upload/download utilities
│   ├── data_cleaner.py    # Data cleaning functions
│   └── logger.py          # Logging configuration
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
│   └── test_processors.py
└── uploads/               # Temporary file storage
```

## Error Handling

The API uses standard HTTP status codes:

- `200 OK`: Successful request
- `201 Created`: Resource created successfully
- `400 Bad Request`: Invalid request parameters
- `404 Not Found`: Resource not found
- `413 Payload Too Large`: File size exceeds limit
- `415 Unsupported Media Type`: Invalid file format
- `500 Internal Server Error`: Server error

Error responses follow this format:

```json
{
  "error": "Error message",
  "status_code": 400,
  "details": "Additional error details"
}
```

## Testing

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=api --cov-report=html
```

## Development

### Code Style

This project follows PEP 8 style guidelines. Format code using:

```bash
black .
flake8 .
```

### Adding New Processors

1. Create a new processor function in `api/processors.py`
2. Add the processor to the route handler in `api/routes.py`
3. Update the API documentation
4. Add tests in `tests/test_processors.py`

## Performance Considerations

- Large files are processed in chunks to manage memory usage
- Async processing for long-running operations
- Caching for frequently accessed data
- Rate limiting to prevent abuse

## Security

- File type validation
- File size limits
- Input sanitization
- CORS configuration
- Environment-based secrets management

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues and questions:
- Open an issue on GitHub
- Email: support@example.com

## Roadmap

- [ ] Add support for more file formats (Parquet, Avro)
- [ ] Implement real-time data streaming
- [ ] Add machine learning preprocessing pipelines
- [ ] Create web dashboard for visualization
- [ ] Add authentication and user management
- [ ] Implement job queue for batch processing
- [ ] Add data export to cloud storage (S3, Azure Blob)

## Acknowledgments

- Flask framework
- Pandas for data processing
- NumPy for numerical operations

---

**Version:** 1.0.0  
**Last Updated:** 2024

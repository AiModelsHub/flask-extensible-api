# Flask Google Maps API Service

This project is a Flask-based backend service demonstrating:
- Google Maps API request bursts with concurrency
- Dynamic request generation with randomized coordinates
- Swagger (OpenAPI) integration using Flasgger for API documentation

## Features

- Concurrent HTTP requests using ThreadPoolExecutor
- Environment variable based configuration
- Centralized request headers and payload utils
- Swagger UI available at `/apidocs/`

## Project Structure

app/
├── core/
│ ├── config.py # Configuration (loads .env)
│ └── extensions.py # Flask extensions (if any)
├── models/
│ ├── init.py
│ ├── response.py # Global API response model
│ └── requests/
│ ├── init.py
│ └── burst_request.py # BurstRequest model
├── routes/
│ └── burst_routes.py # Flask route(s)
├── services/
│ ├── init.py
│ ├── google_maps_service.py
│ └── swagger_service.py # Swagger config
├── utils/
│ └── request_utils.py # Headers and data builders
└── main.py # Flask app factory and entry point

## Setup

1. Clone the repo
2. Create and activate a Python virtual environment
3. Install dependencies:
pip install -r requirements.txt
4. Create a `.env` file at the project root with required environment variables, e.g.:
    GOOGLE_MAPS_API_SALT=your_salt_here
    GOOGLE_MAPS_API_SIGNATURE=your_signature_here
    GOOGLE_MAPS_CLIENT_ID=your_client_id_here
    GOOGLE_MAPS_GMP_CLIENT_SIGNALS=your_client_signals_here
    GOOGLE_MAPS_SESSION_ID=your_session_id_here
    SECRET_KEY=supersecretkey
    DEBUG=True
5. Run the app:
python app/main.py
6. Visit Swagger UI at:
http://localhost:5000/apidocs/

## Usage
Use the `/api/run-burst` POST endpoint to trigger concurrent requests.  
Request body example:
```json
{
"total_requests": 100,
"workers": 10
}
```

## License
MIT License
from .google_maps_service import GoogleMapsService
from .openai_service import OpenAIService
from .burst_service import run_burst_service

google_maps_service = GoogleMapsService()
openai_service = OpenAIService()

services = {
    "google_maps": google_maps_service,
    "run_burst": run_burst_service,
    "openai": openai_service
}

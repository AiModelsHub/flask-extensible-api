import requests
import concurrent.futures
from tqdm import tqdm

from app.utils.request_utils import build_headers, build_data

class GoogleMapsService:
    """
    Service class to interact with Google Maps internal API
    to send burst requests and collect errors.
    """

    def __init__(self):
        """
        Initialize the GoogleMapsService with the endpoint URL.
        """
        self.url = "https://maps.googleapis.com/$rpc/google.internal.maps.mapsjs.v1.MapsJsInternalService/GetViewportInfo"

    def _send_request(self, i):
        """
        Send a single POST request to the Google Maps API.

        Args:
            i (int): The request number, used for error identification.

        Returns:
            None if the request is successful with status code 200,
            else a string describing the error or failure.
        """
        headers = build_headers()
        data = build_data()
        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=10)
            if response.status_code != 200:
                return f"Request #{i} failed with status {response.status_code}"
        except Exception as e:
            return f"Request #{i} error: {e}"
        return None

    def run_burst(self, total_requests=100, workers=10):
        """
        Send multiple concurrent POST requests to the Google Maps API
        using a thread pool executor, and collect any errors encountered.

        Args:
            total_requests (int): Total number of requests to send. Defaults to 100.
            workers (int): Number of concurrent worker threads. Defaults to 10.

        Returns:
            List[str]: A list of error messages from failed requests. Empty if all succeed.
        """
        errors = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(self._send_request, i) for i in range(1, total_requests + 1)]
            for future in tqdm(concurrent.futures.as_completed(futures), total=total_requests, desc="Sending Requests"):
                result = future.result()
                if result:
                    errors.append(result)
        return errors

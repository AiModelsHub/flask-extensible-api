import concurrent.futures
from app.services.google_maps_service import GoogleMapsService

maps_service = GoogleMapsService()

def run_burst_service(total_requests: int, workers: int, stream: bool = False):
    """
    Run burst requests either streaming progress or return full result at once.

    :param total_requests: Number of requests to send
    :param workers: Number of concurrent threads
    :param stream: If True, yield incremental progress dicts; else return full dict.
    :return: Generator if stream=True, else dict
    """
    if stream:
        completed = 0
        errors = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(maps_service._send_request, i) for i in range(1, total_requests + 1)]

            for future in concurrent.futures.as_completed(futures):
                error = future.result()
                if error:
                    errors.append(error)
                completed += 1
                yield {
                    "message": f"Request {completed} / {total_requests} completed",
                    "progress": completed / total_requests,
                    "errors_count": len(errors),
                    "last_error": error if error else None
                }

        yield {
            "message": "Burst completed",
            "progress": 1.0,
            "errors_count": len(errors),
            "errors": errors
        }

    else:
        errors = maps_service.run_burst(total_requests, workers)
        return {
            "status": "completed",
            "total_requests": total_requests,
            "workers": workers,
            "errors_count": len(errors),
            "errors": errors
        }

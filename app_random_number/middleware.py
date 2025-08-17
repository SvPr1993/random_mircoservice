import time
import logging

# специально фиксированное имя логгера — так проще не промахнуться в LOGGING
logger = logging.getLogger("request_timing")


class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        duration_ms = (time.perf_counter() - start) * 1000

        user = getattr(request, "user", None)
        user_repr = str(user) if getattr(user, "is_authenticated", False) else "anon"

        # лог + (опционально) заголовок для удобства в браузере/Postman
        response["X-Response-Time"] = f"{duration_ms:.2f} ms"
        logger.info(
            "method=%s path=%s status=%s user=%s duration_ms=%.2f",
            request.method,
            request.get_full_path(),
            getattr(response, "status_code", "-"),
            user_repr,
            duration_ms,
        )
        return response

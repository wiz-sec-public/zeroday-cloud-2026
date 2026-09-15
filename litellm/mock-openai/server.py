import json
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


API_KEY = os.environ.get("MOCK_OPENAI_API_KEY", "internal-mock-key")


class OpenAIHandler(BaseHTTPRequestHandler):
    def write_json(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def authorized(self):
        return self.headers.get("Authorization") == f"Bearer {API_KEY}"

    def do_GET(self):
        if self.path == "/health":
            self.write_json(200, {"status": "ok"})
            return
        if self.path == "/v1/models" and self.authorized():
            self.write_json(
                200,
                {"object": "list", "data": [{"id": "zdc-mock", "object": "model"}]},
            )
            return
        self.write_json(401 if not self.authorized() else 404, {"error": "unauthorized"})

    def do_POST(self):
        if not self.authorized():
            self.write_json(401, {"error": {"message": "invalid internal key"}})
            return
        if self.path != "/v1/chat/completions":
            self.write_json(404, {"error": {"message": "not found"}})
            return

        length = int(self.headers.get("Content-Length", "0"))
        request = json.loads(self.rfile.read(length) or b"{}")
        model = request.get("model", "zdc-mock")
        self.write_json(
            200,
            {
                "id": "chatcmpl-zdc-mock",
                "object": "chat.completion",
                "created": int(time.time()),
                "model": model,
                "choices": [
                    {
                        "index": 0,
                        "message": {"role": "assistant", "content": "mock response"},
                        "finish_reason": "stop",
                    }
                ],
                "usage": {"prompt_tokens": 1, "completion_tokens": 2, "total_tokens": 3},
            },
        )

    def log_message(self, format, *args):
        return


ThreadingHTTPServer(("0.0.0.0", 8080), OpenAIHandler).serve_forever()

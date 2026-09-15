from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/metrics":
            self.send_error(404)
            return

        body = b"zdc_scrape_fixture_up 1\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


ThreadingHTTPServer(("0.0.0.0", 5000), MetricsHandler).serve_forever()

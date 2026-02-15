from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = int(os.environ.get("PORT", 8080))


class MyIPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check for forwarded IP (when behind a reverse proxy / load balancer)
        ip = (
            self.headers.get("X-Forwarded-For", "").split(",")[0].strip()
            or self.headers.get("X-Real-IP", "")
            or self.client_address[0]
        )
        body = ip.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"{self.client_address[0]} - {args[0]}")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), MyIPHandler)
    print(f"Listening on port {PORT}")
    server.serve_forever()

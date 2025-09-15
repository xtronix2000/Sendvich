from http.server import HTTPServer, SimpleHTTPRequestHandler
import base64, secrets, os, sys

HOST = "0.0.0.0"
DEFAULT_PORT = 17032

USERNAME = "srv_" + secrets.token_hex(4)
PASSWORD = secrets.token_urlsafe(24)
AUTH_B64 = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()

class AuthHandler(SimpleHTTPRequestHandler):
    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Sendvich authorization"')
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        auth_header = self.headers.get("Authorization")
        if auth_header == f"Basic {AUTH_B64}":
            super().do_GET()
        else:
            self.do_AUTHHEAD()
            self.wfile.write(b"Authentication required.")

if __name__ == "__main__":
    PORT = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print("Invalid port argument, using default", DEFAULT_PORT)

    print("=== Minimal GET-only server ===")
    print(f"Serving on port {PORT} with basic auth...")
    print("Serve dir:", os.getcwd())
    print("USER:", USERNAME)
    print("PASS:", PASSWORD)
    print("\nWARNING: INSECURE over networks. Use only on localhost/host-only interfaces")

    httpd = HTTPServer((HOST, PORT), AuthHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")

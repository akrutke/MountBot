import http.server
import socketserver
import requests
import random
import string
import webbrowser


# OAuth credentials
CLIENT_ID = 'b3bb0ce94dfb433b9265c458deabb736'
CLIENT_SECRET = 'Yrkrv2wviRmZwla9hgURwkNi8bZfR1SZ'

# OAuth endpoints
AUTH_URL = 'https://us.battle.net/oauth/authorize'
TOKEN_URL = 'https://us.battle.net/oauth/token'

# Redirect URI you provided during application registration
REDIRECT_URI = 'https://localhost:8080'

# Generate a random state parameter
def generate_state():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

state = generate_state()

# Step 1: Get Authorization Code
auth_params = {
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'response_type': 'code',
    'scope': 'wow.profile ',  # e.g., "wow.profile"
    'state': state,
}
auth_url = f"{AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in auth_params.items()])}"

print("Visit the following URL in your browser to authorize your application:")
print(auth_url)
authorization_code = input("Enter the authorization code from the redirected URL: ")

# Verify the received state parameter
#received_state = input("Enter the received 'state' parameter: ")
#if received_state != state:
#    print("State parameter mismatch. Exiting...")
#    exit()

class CallbackHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/callback'):
            params = dict(kv.split('=') for kv in self.path.split('?')[1].split('&'))
            received_state = params.get('state', None)
            if received_state != state:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'State parameter mismatch')
                return

            authorization_code = params.get('code', None)
            if authorization_code:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Authorization code received, you can close this window.')
                self.server.authorization_code = authorization_code
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Authorization code not received')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

# Start local server
with socketserver.TCPServer(("", LOCAL_PORT), CallbackHandler) as httpd:
    print(f"Serving at port {LOCAL_PORT}")
    httpd.handle_request()

authorization_code = httpd.authorization_code

# Step 2: Exchange Authorization Code for Access Token
token_params = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'code': authorization_code,
    'redirect_uri': REDIRECT_URI,
    'grant_type': 'authorization_code',
}
response = requests.post(TOKEN_URL, data=token_params)
access_token = response.json()['access_token']
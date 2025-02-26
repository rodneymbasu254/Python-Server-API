import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/get_random_color':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                color = data.get('color' , None)
                if color is None:
                    self.send_response(400)
                    self.send_header('Content-types', '/application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"Error": "Color is missing"}).encode())
                    return
                #elif color != '':
                    #self.send_response(400)
                    #self.send_header('Content-type', '/application/json')
                    #self.end_headers()
                    #self.wfile.write(json.dumps({"error": "Value should be a str"}).encode())
                    #return
                def GetRandomColor():
                    color = ['Blue', 'Green', 'Yellow']
                    return random.choice(color)
                    
                random_color = GetRandomColor()
                user_color = color
                def CheckAnswer():
                    if color == random_color:
                        print("You win")
                    else:
                        print("you lose,  the color is: ", random_color)
                    return
                    
                response = {CheckAnswer()}
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            except (json.JSONDecodeError, ValueError):
                self.send_response(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Invalid Input"}).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

def run(server_class = HTTPServer, handler_class = SimpleHTTPRequestHandler, port = 8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}....")
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=5000)
                    
                
                
        
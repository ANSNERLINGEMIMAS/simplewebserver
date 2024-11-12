from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
   <body>
<h1>
Configuration(ANS NERLING EMIMA S 24900105)</h1>
   <ol>
<li> Device name      Emima(249001)</li>
<li> Processor	       11th Gen Intel(R) Core(TM) i7-1195G7 @ 2.90GHz  2.92GHz</li>
<li> Installed RAM    32.0GB(31.7 GB usable)</li>
<li>Device ID	       2EAA22B3-40F6-462E-88F1-903281</li>
 <li>Product ID        oo842 4Q709-00768-AAORM</li> 
 <li>System Type       64-bit operating system,x61-based processor</li>
 <li> Pen and Touch    No pen or touch input is availqble for this display</li>
 </ol>
</body>
</html>
 """  
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
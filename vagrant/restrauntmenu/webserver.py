from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restraunts"):
                restraunts = session.query(Restraunt).all()
                message = ""
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                message ="</body></html>"
                for restraunt in restraunts:
                    message += restraunt.name
                    message += "</br></br></br>"

                message ="</body></html>"
                self.wfile.write(message)
                return
        except IOError: 
            self.send_error(404, 'File Not Found: %s' % self.path)
    

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()


if __name__ == '__main__':
    main()
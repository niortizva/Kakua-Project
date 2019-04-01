import waitress
from kakuaa.wsgi import application
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            port = float(sys.argv[1])
        except Exception:
            port = 8000			
    else:
        port = 8000
        
waitress.serve(application, port=port, url_scheme='http')

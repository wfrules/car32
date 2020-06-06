from microWebSrv import MicroWebSrv
mws = MicroWebSrv()      # TCP port 80 and files in /flash/www
mws.Start(threaded=True) # Starts server in a new thread
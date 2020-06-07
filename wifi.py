class WifiTool:
    def buildConn()
      import network
      wlan = network.WLAN(network.STA_IF) # create station interface
      wlan.active(True)       # activate the interface
      wlan.scan()             # scan for access points
      wlan.isconnected()      # check if the station is connected to an AP
      wlan.connect('Wfhome', '15980936465') # connect to an AP
      wlan.config('mac')      # get the interface's MAC address
      wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses

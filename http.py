
import json
from microWebSrv import MicroWebSrv

class Ht:
    
  
  
  
  def handlerFuncGet(httpClient, httpResponse):
    print("In GET-TEST HTTP")  
   
  def getParams(self, httpClient, key):
      formData  = httpClient.ReadRequestPostedFormData()
      parms = json.loads(formData['parms'])
      return parms;
      
  def start(self):    
    @MicroWebSrv.route('/cmd', 'POST')
    def httpHandlerCmd(httpClient, httpResponse) :
      sCmd = self.getParams(httpClient, 'cmd');
      print(sCmd) 
    
    @MicroWebSrv.route('/sync', 'POST')
    def httpHandlerSync(httpClient, httpResponse) :
      print('sync')     
    
    mws = MicroWebSrv()
    mws.Start()











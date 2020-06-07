from microWebSrv import MicroWebSrv
mws = MicroWebSrv()
mws.SetNotFoundPageUrl('http://www.baidu.com')

routeHandlers = [
  ( "et-test", "METHOD", handlerFuncGet ),
]

@MicroWebSrv.route('/get-test')
def handlerFuncGet(httpClient, httpResponse) :
  print("In GET-TEST HTTP")

mws.Start()

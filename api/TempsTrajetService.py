from spyne import Application, rpc, ServiceBase
from spyne import Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import math

class TempsTrajetService(ServiceBase):
    
    @rpc(Array(Array(float)),float, _returns=float)
    def tempsMoy(ctx, bornes, vitMoy):
        ctx.transport.resp_headers['Access-Control-Allow-Origin'] = '*'
        res = 0
        last = bornes[0]
        for i in bornes:
            res += math.sqrt((i[0] - last[0]) ** 2 + (i[1] - last[1]) ** 2)
        return res / 1000 / vitMoy

application = Application([TempsTrajetService], 'spyne.examples.trajet.soap',
in_protocol=Soap11(validator='lxml'),
out_protocol=Soap11())
app = WsgiApplication(application)

#if __name__ == '__main__':
#    server = make_server('127.0.0.1', 8000, wsgi_application)
#    server.serve_forever()
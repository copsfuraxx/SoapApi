from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class TempsTrajetService(ServiceBase):
    
    @rpc(float,float,float,int, _returns=float)
    def tempsMoy(ctx, distKm, vitMoyKMH, rechargeH, nb_recharge):
        ctx.transport.resp_headers['Access-Control-Allow-Origin'] = '*'
        temps = distKm / vitMoyKMH
        temps += rechargeH * nb_recharge
        return temps

application = Application([TempsTrajetService], 'spyne.examples.trajet.soap',
in_protocol=Soap11(validator='lxml'),
out_protocol=Soap11())
app = WsgiApplication(application)
#server = make_server('localhost', 8000, app)
#server.serve_forever()
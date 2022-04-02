from twisted.internet import endpoints, reactor
from twisted.web.server import Site
from twisted.web.static import File

resource = File('tmp')
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
endpoint.listen(factory)
reactor.run()

# curl localhost:8888

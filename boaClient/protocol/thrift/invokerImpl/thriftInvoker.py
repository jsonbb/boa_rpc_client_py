#encoding:utf-8

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from boaClient.protocol.thrift import  BoarpcService
from boaClient.protocol.invoker import Invoker
from common.utils.netUtils import NetUtils
from common.util_Log.logger import logging
logger = logging.getLogger(__name__)

class ThriftInvoker(Invoker):

    def __init__(self,url):
        self.url = url

    def invoke(self,endpointUrl='',params=[]):
        '''
        invoke endpoint
        :return:
        '''
        result = None
        transport =None
        try:
            # Make socket
            transport = TSocket.TSocket(self.url.host, self.url.port)
            # Buffering is critical. Raw sockets are very slow
            transport = TTransport.TBufferedTransport(transport)
            # Wrap in a protocol
            protocol = TCompactProtocol.TCompactProtocolAccelerated(transport)
            # Create a client to use the protocol encoder
            client = BoarpcService.Client(protocol)
            # Connect!
            transport.open()
            endpointMetas = endpointUrl.split('.')
            result  = client.dispatcher(NetUtils.getIp(),endpointMetas[0],endpointMetas[1],endpointMetas[2],params)
        finally:
            if transport is not None:
                transport.close()
        return result




#encoding:utf-8

from common.config.conf import config
from boaClient.exception.exceptions import UnrealizedException

class Invoker:


    def invoke(self,endpointUrl):
        '''
        invoke endpoint
        :return:
        '''
        raise UnrealizedException()


from  boaClient.protocol.thrift.invokerImpl.thriftInvoker import ThriftInvoker
from boaClient.exception.exceptions import FatalError
from boaClient.url import URL
class InvokerFactory:

    @staticmethod
    def createInvoker(protocol):
         url = URL('thrift','192.168.95.100','14917','11732')
         if 'thrift'== protocol:
             return ThriftInvoker(url)
         else:
             raise FatalError('Nonsupport protocol')



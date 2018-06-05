#encoding:utf-8

import sys


from boaClient.protocol.invoker import InvokerFactory
from common.config.conf import config
reload(sys)
sys.setdefaultencoding('utf-8')

class BoaClient:

    # defualt protocol: thrift
    PROTOCOL = config.getConf('rpc','protocol',defult='thrift')
    def invoke(self,endpointUrl,params):
        invoker = InvokerFactory.createInvoker(self.PROTOCOL)
        return invoker.invoke(endpointUrl,params)



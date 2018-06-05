#encoding:utf-8
__author__ = 'js'
from boaClient.client import BoaClient
from common.util_Log.logger import logging
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    c = BoaClient()
    r = c.invoke('demoEndpoint.Demo2.test2',[str({'a':'1234543'})])
    print r
    # r = c.invoke('demoEndpoint.Demo2.test2', [str({'a': '1234543'})])
    # print r
    # r = c.invoke('demoEndpoint.Demo2.test2', [str({'a': '1234543'})])
    # print r
    # r = c.invoke('demoEndpoint.Demo2.test2', [str({'a': '1234543'})])
    # print r
    # for i in xrange(0,100):
    #     r = c.invoke('demoEndpoint.Demo2.test2', [str({'a': '1234543'})])
    #     print r


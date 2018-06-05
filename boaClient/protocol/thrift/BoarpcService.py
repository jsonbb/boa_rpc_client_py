#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def dispatcher(self, client, moduleName, className, functionName, params):
        """
        Parameters:
         - client
         - moduleName
         - className
         - functionName
         - params
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def dispatcher(self, client, moduleName, className, functionName, params):
        """
        Parameters:
         - client
         - moduleName
         - className
         - functionName
         - params
        """
        self.send_dispatcher(client, moduleName, className, functionName, params)
        return self.recv_dispatcher()

    def send_dispatcher(self, client, moduleName, className, functionName, params):
        self._oprot.writeMessageBegin('dispatcher', TMessageType.CALL, self._seqid)
        args = dispatcher_args()
        args.client = client
        args.moduleName = moduleName
        args.className = className
        args.functionName = functionName
        args.params = params
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_dispatcher(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = dispatcher_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "dispatcher failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["dispatcher"] = Processor.process_dispatcher

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_dispatcher(self, seqid, iprot, oprot):
        args = dispatcher_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = dispatcher_result()
        try:
            result.success = self._handler.dispatcher(args.client, args.moduleName, args.className, args.functionName, args.params)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in invokerImpl')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in invokerImpl')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("dispatcher", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class dispatcher_args(object):
    """
    Attributes:
     - client
     - moduleName
     - className
     - functionName
     - params
    """


    def __init__(self, client=None, moduleName=None, className=None, functionName=None, params=None,):
        self.client = client
        self.moduleName = moduleName
        self.className = className
        self.functionName = functionName
        self.params = params

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.client = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.moduleName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.className = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.functionName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.params = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.params.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('dispatcher_args')
        if self.client is not None:
            oprot.writeFieldBegin('client', TType.STRING, 1)
            oprot.writeString(self.client.encode('utf-8') if sys.version_info[0] == 2 else self.client)
            oprot.writeFieldEnd()
        if self.moduleName is not None:
            oprot.writeFieldBegin('moduleName', TType.STRING, 2)
            oprot.writeString(self.moduleName.encode('utf-8') if sys.version_info[0] == 2 else self.moduleName)
            oprot.writeFieldEnd()
        if self.className is not None:
            oprot.writeFieldBegin('className', TType.STRING, 3)
            oprot.writeString(self.className.encode('utf-8') if sys.version_info[0] == 2 else self.className)
            oprot.writeFieldEnd()
        if self.functionName is not None:
            oprot.writeFieldBegin('functionName', TType.STRING, 4)
            oprot.writeString(self.functionName.encode('utf-8') if sys.version_info[0] == 2 else self.functionName)
            oprot.writeFieldEnd()
        if self.params is not None:
            oprot.writeFieldBegin('params', TType.LIST, 5)
            oprot.writeListBegin(TType.STRING, len(self.params))
            for iter6 in self.params:
                oprot.writeString(iter6.encode('utf-8') if sys.version_info[0] == 2 else iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(dispatcher_args)
dispatcher_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'client', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'moduleName', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'className', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'functionName', 'UTF8', None, ),  # 4
    (5, TType.LIST, 'params', (TType.STRING, 'UTF8', False), None, ),  # 5
)


class dispatcher_result(object):
    """
    Attributes:
     - success
    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('dispatcher_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(dispatcher_result)
dispatcher_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
)
fix_spec(all_structs)
del all_structs

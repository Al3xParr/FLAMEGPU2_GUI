import random
import numpy as np


class Message():
    def __init__(self, name, msg_type, vars, var_types):
        self.name = name
        self.msg_type = msg_type
        self.vars = vars
        self.var_types = var_types



def isValidName(name: str):
    name = name.replace("_", "")
    if name.isalnum() and not name[0].isdigit():
        return True
    else:
        return False



def checkVar(val: str, varType: str):

    varType = varType.lower()

    if any(c.isalpha() for c in val):
        outputType = type(eval(val)).__name__ # float/int
        if outputType == "float" and (varType == "float" or varType == "double"):
            return True
        elif outputType == "int":
            if "-" in val and varType[0] == "u":
                return False
            else:
                return True
        else:
            return False
            

    
    if varType == "float":
        try:
            np.single(val)
            return True 
        except ValueError:
            return False

    elif varType == "double":
        try:
            np.double(val)
            return True 
        except ValueError:
            return False

    elif varType == "int8":
        try:
            if int(val) >= -128 and int(val) <= 127:
                return True
            else:
                return False
        except ValueError:
            return False

    elif varType == "int16":
        try:
            if int(val) >= -32768 and int(val) <= 32767:
                return True
            else:
                return False
        except ValueError:
            return False

    elif varType == "int32":
        try:
            if int(val) >= -2147483648 and int(val) <= 2147483647:
                return True
            else:
                return False
        except ValueError:
            return False

    elif varType == "int64":
        try:
            if int(val) >= -9223372036854775808 and int(val) <= 9223372036854775807:
                return True
            else:
                return False
        except ValueError:
            return False

    elif varType == "uint8":
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 255:
                return True
        return False

    elif varType == "uint16":
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 65535:
                return True
        return False

    elif varType == "uint32":
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 4294967295:
                return True
        return False

    elif varType == "uint64":
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 18446744073709551615:
                return True
        return False

    else:
        return False

        
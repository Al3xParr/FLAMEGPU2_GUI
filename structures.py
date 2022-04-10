import random
import numpy as np


class Message():
    def __init__(self, name, msg_type, vars, var_types, params=None):
        self.name = name
        self.msg_type = msg_type
        self.vars = vars
        self.var_types = var_types
        self.params = params if params is not None else {}



def isValidName(name: str):
    name = name.replace("_", "")
    if name.isalnum() and not name[0].isdigit():
        return True
    else:
        return False


#function to return the literal value that will be compiled
#E.g. "5.5" -> 5.5
#     "Radius" -> "Radius"

#try int()
#try float()
#else


#Returns bool depending on if the value is valid:
#includes allowing random python functions and global variables
def checkVar(inpVal: str, varType: str, varList: dict = None, allowRandFuncs = True):
    val = inpVal
    if varList is not None:
        for v in varList.values():
            if v["name"] == val:
                val = v["value"]
                break

    varType = varType.lower()
    if allowRandFuncs:
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
            if val != inpVal:
                return str(val)
            else:
                return float(val) 
        except ValueError:
            return False

    elif varType == "double":
        try:
            np.double(val)
            if val != inpVal:
                return str(val)
            else:
                return float(val) 
        except ValueError:
            return False

    elif varType == "int8":
        try:
            if int(val) >= -128 and int(val) <= 127:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
            else:
                return False
        except ValueError:
            return False

    elif varType == "int16":
        try:
            if int(val) >= -32768 and int(val) <= 32767:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
            else:
                return False
        except ValueError:
            return False

    elif varType == "int32":
        try:
            if int(val) >= -2147483648 and int(val) <= 2147483647:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
            else:
                return False
        except ValueError:
            return False

    elif varType == "int64" or varType == "int":
        try:
            if int(val) >= -9223372036854775808 and int(val) <= 9223372036854775807:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
            else:
                return False
        except ValueError:
            return False

    elif varType == "uint8":
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 255:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
        return False

    elif varType == "uint16":
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 65535:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
        return False

    elif varType == "uint32":
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 4294967295:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
        return False

    elif varType == "uint64" or varType == "id":
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 18446744073709551615:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
        return False

    else:
        return False
import numpy as np
class Message():
    def __init__(self, name, msg_type, vars, var_types, params=None):
        self.name = name
        self.msg_type = msg_type
        self.vars = vars
        self.var_types = var_types
        self.params = params if params is not None else {}


# Returns true or false depending on if given string is valid variable name
def isValidName(name: str):
    name = name.replace("_", "")
    if name.isalnum() and not name[0].isdigit():
        return True
    else:
        return False


#Returns bool depending on if the value is valid:
#includes allowing random python functions and global variables
def checkVar(inpVal: str, varType: str, varList: dict = None, allowRandFuncs = True):
    val = inpVal
    if varList is not None:
        #Loops over variable list given and extracts the numerical val required
        for v in varList.values():
            if v["name"] == val:
                val = str(v["value"])
                break

    varType = varType.lower()
    if allowRandFuncs:
        #Checks if the value is a random function
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
        #Checks if input val is float type
        try:
            np.single(val)
            if val != inpVal:
                return str(val)
            else:
                return float(val) 
        except ValueError:
            return False

    elif varType == "double":
        #Checks if input val is double type
        try:
            np.double(val)
            if val != inpVal:
                return str(val)
            else:
                return float(val) 
        except ValueError:
            return False

    elif varType == "int8":
        #Checks if input val is int8 type
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
        #Checks if input val is int16 type
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
        #Checks if input val is int32 type
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
        #Checks if input val is int type
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
        #Checks if input val is uint8 type
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 255:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
        return False

    elif varType == "uint16":
        #Checks if input val is uint16 type
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 65535:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
        return False

    elif varType == "uint32":
        #Checks if input val is uint32 type
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 4294967295:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
        return False

    elif varType == "uint64" or varType == "id":
        #Checks if input val is uint64 type
        if val.isdigit():
            if int(val) >= 0 and int(val) <= 18446744073709551615:
                if val != inpVal:
                    return str(val)
                else:
                    return int(val) 
        return False

    else:
        return False
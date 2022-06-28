import sine
import cos

def getTan(angle):
    sin_value= sine.getsine(angle)
    cos_value = cos.getCosine(angle)

    if cos_value == 0:
        return "undefined"

    tan_value = sin_value/cos_value
    
    return tan_value
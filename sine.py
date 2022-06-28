def getsine(angle):
    sine = None
    if angle==0:
        sine=0
    elif angle==30:
        sine=1/2
    elif angle==45:
        sine=1/(2**0.5)
    elif angle ==60:
        sine=(3**0.5)/2
    elif angle == 90:
        sine=1
    elif angle == 180:
        sine=0

    return sine if sine!=None else "undefined"
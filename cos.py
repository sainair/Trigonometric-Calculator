def getCosine(angle):
    cosine = None
    if angle==90:
        cosine=0
    elif angle==60:
        cosine=1/2
    elif angle==45:
        cosine=1/(2**0.5)
    elif angle ==30:
        cosine=(3**0.5)/2
    elif angle == 0:
        cosine=1
    elif angle == 180:
        cosine=1

    return cosine if cosine!=None else "undefined"
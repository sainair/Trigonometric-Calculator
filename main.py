import sine
import cos
import tan

angle = int(input("Enter Angle \n"))
function_type = input("What do you want to find?(Enter 'sin', 'cos', 'tan')\n")
func_types = ['sin','cos','tan']
sin_positive = True if angle <= 180 else False
cos_positive = True if angle >=0 and angle<=90 or angle >= 270 and angle <=360 else False
tan_positive = True if angle >0 and angle <=90 or angle >180 or angle <= 270 else False

if function_type not in func_types:
    function_type='undefined'



if function_type=='sin':
    if sin_positive:
        sin_angle = 180-angle if angle>90 else angle
        sin_value = sine.getsine(sin_angle)
        print(f"sine of {angle} is {sin_value}")
    elif not sin_positive:
        sin_angle=angle-180 if angle<270 else 360-angle
        sin_value= -1*(sine.getsine(sin_angle))
        print(f"sine of {angle} is {sin_value}")

elif function_type=='cos':
    if cos_positive:
        cos_angle = 180-angle if angle>90 else angle
        cos_value = cos.getCosine(cos_angle)
        print(f'Cos of {angle} is {cos_value}')
    elif not cos_positive:
        cos_angle = 180-angle if angle<180 else angle-180
        cos_value = -1*(cos.getCosine(cos_angle))
        print(f'Cos of {angle} is {cos_value}')

elif function_type=='tan':
    if tan_positive:
        tan_angle = angle if angle <=90 else angle-180
        tan_value = tan.getTan(tan_angle)
        print(f"Tan of {angle} is {tan_value}")
    elif not tan_positive:
        tan_angle = 180-angle if angle <= 180 else angle-180
        tan_value = -1*(tan.getTan(tan_angle))
        print(f"Tan of {angle} is {tan_value}")
        
print("UNDEFINED TYPE") if function_type=='undefined' else None

    
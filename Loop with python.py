from concurrent.futures import thread
import math
from time import sleep

ascii='.:-=+*#%@'

def circle(rx,ry,x,y,z):
    i = 0
    j=0
    coords = []

    r2 = 50
    while j<2*math.pi:
        while i<2*math.pi:
            circlex = r2+int(rx*math.cos(i))
            circley = y+int( ry*math.sin(i))

            cos = math.cos(j)
            sin = math.sin(j)
            _sin = -math.sin(j)


            coords.append((int((circlex)*cos),int(circley)))
            i+=0.1
        j+=1
    return coords

def map1(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def drawFrame(x,y,graphics):
    screen=""
    for i in range(1,y+1):
        for j in range(1,x+1):
            if((j,i) not in graphics):
                screen+=" "
            else:
                screen+="."
        screen+="\n"
    
    print("\x1b[H")
    print(screen)
i = 0
while(True):
    i+=0.23
    drawFrame(80,12,circle(12,6*math.sin(i),10,6,10*i))
    try:
        sleep(0.12)
    except KeyboardInterrupt:
        pass

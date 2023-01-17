import random, sys, time

WIDTH = 50 
pauseTime = .05

leftWidth = 20
gapWidth = 10 

while True:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
    
    try:
        time.sleep(pauseTime)
    except KeyboardInterrupt:
        sys.exit()

    
    adjustSide = random.randint(1, 6)
    if adjustSide == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif adjustSide == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass

    adjustGap = random.randint(1, 6)
    if adjustGap == 1 and gapWidth > 1:
        gapWidth = gapWidth - 1 
    elif adjustGap == 2 and leftWidth + gapWidth < WIDTH - 1 :
        gapWidth = gapWidth + 1
    else:
        pass
with open("day3.txt") as file:
    engine = []
    parts = []
    lines = file.readlines()
    # split file into individual lines
    for line in lines:
        engine.append(line.strip('\n'))
    width = len(engine[0])
    height = len(engine)
    number = ''
    valid = False
    for y in range(height):
        moreDigits = False
        for x in range(width):
            if engine[y][x].isdigit():
                # here we are checking if this is a new number
                # number is the entire number built up - if there are currently no more digits,
                # this suggests this is a new number so set the first new number digit as the current digit
                if not moreDigits:
                    number = engine[y][x]
                    valid = False
                # else, append the current digit to the already exisiting number as there must have been 
                # digits before this current digit (i.e. moreDigits is True)
                else:
                    number += engine[y][x]
                # here we are checking if this is the last digit
                if (x + 1) < width:
                    if engine[y][x+1].isdigit():
                        moreDigits = True
                    else:
                        moreDigits = False
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if (x + i) >= 0 and (x + i) < width and (y + j) >= 0 and (y + j) < height:
                            if engine[y + j][x + i] != '.' and not (engine[y + j][x + i]).isdigit():
                                valid = True
            if valid and not moreDigits:
                parts.append(number)
                valid = False
    print(parts)
    ans = sum(int(num) for num in parts)
    print(ans)


with open("input.txt") as file:
    possible = []
    lines = file.readlines()

    # split file into individual lines
    for line in lines:
        valid = True
        # split indiviudal line into ['Game X', 'choice 1; choice 2; choice 3;']
        components = line.split(":")
        # split second component i.e. 'choice 1; choice 2; choice 3;' into individual choices
        choices= components[1].split(";")
        for choice in choices:
            # for each choice, split into cube strings e.g. ['X red', 'X blue', 'X green']
            items = choice.split(",")
            for item in items:
                # for each item, check the number of cubes is valid
                if "blue" in item:
                    num = item.split("blue")
                    if int(num[0]) > 14:
                        valid = False
                if "red" in item:
                    num = item.split("red")
                    if int(num[0]) > 12:
                        valid = False
                if "green" in item:
                    num = item.split("green")
                    if int(num[0]) > 13:
                        valid = False
        if valid:
            number = int(components[0].strip("Game "))
            possible.append(number)
    ans = 0
    for number in possible:
        ans += number
    print(ans)


        



    
        




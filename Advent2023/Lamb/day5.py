with open("day5.txt") as file:
    allFile = file.read()
    maps = allFile.split("\n")
    # remove empty strings in maps list
    maps = [x for x in maps if x != '']
    # create seeds list
    seeds = maps[0].strip("seeds: ").split(' ')
    # remove seeds list from maps list
    maps = maps[1:]
    #  allMaps = [seeds, sts, stf, ftw, wtl, ltt, tth, htl]
    allMaps = [seeds, [], [], [], [], [], [], []]
    mapNum = 0
    # append the mappings to the correct map list type
    for item in maps:
        #check if the current list item is a heading
        if item == "seed-to-soil map:":
            mapNum = 1
        elif item == "soil-to-fertilizer map:":
            mapNum = 2
        elif item == "fertilizer-to-water map:":
            mapNum = 3
        elif item == "water-to-light map:":
            mapNum = 4
        elif item == "light-to-temperature map:":
            mapNum = 5
        elif item == "temperature-to-humidity map:":
            mapNum = 6
        elif item == "humidity-to-location map:":
            mapNum = 7
        # if not heading then must be mapping so append to current map list type
        elif mapNum != 0:
            allMaps[mapNum].append(item)
    # build dicitonary of { seed : locatioNValue }
    seedLocation = {}
    for seed in seeds:
        # newStatus tracks the seed's value throughout the various maps
        newStatus = int(seed)
        for map in allMaps:
            # mapped is whether the seed has been mapped in the current map it is looping through already (avoid double counting)
            mapped = False
            if map != seeds:
                for mapping in map:
                    # split the mappings into their indiviudal destination, source, range components 
                    # (all contained together in one list)
                    info = mapping.split(' ')
                    # retreive values for each component
                    destination = int(info[0])
                    source = int(info[1])
                    range = int(info[2])
                    sourceRange = source + range
                    diff = destination - source 
                    # calculate whether the current seedValue is in the range of the current mapping if not already mapped
                    # by this current mapping
                    if newStatus >= source and newStatus < sourceRange and not mapped:
                        newStatus = newStatus + diff
                        mapped = True
        # append location value to the dictionary
        seedLocation[seed] = newStatus
    # calculate min location value in dictionary
    minLocationValue = seedLocation[min(seedLocation, key=seedLocation.get)]
    print(minLocationValue)

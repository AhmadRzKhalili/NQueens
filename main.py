def count_guarding_pairs(ground):
    pairs = 0

    for queen in ground:
        if ground.count(queen) > 1:
            pairs += 1

    N = len(ground)
    for i in range(N):
        queen1 = ground[i]

        for j in range(N):
            if j != i:
                queen2 = ground[j]
                if queen1 - queen2 == i - j or queen2 - queen1 == i - j:
                    pairs += 1
                    
                    
    return pairs // 2

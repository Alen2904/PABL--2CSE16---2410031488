def min_swaps(s1, s2):
    count_A = 0
    count_B = 0
    
    for i in range(len(s1)):
        if s1[i] == '1' and s2[i] == '0':
            count_A += 1
        elif s1[i] == '0' and s2[i] == '1':
            count_B += 1
    
    if (count_A + count_B) % 2 != 0:
        return -1
    
    return (count_A // 2) + (count_B // 2)


print(min_swaps("1100", "1111"))
print(min_swaps("00011", "11001"))
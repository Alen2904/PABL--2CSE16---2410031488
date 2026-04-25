from collections import Counter

def sort_by_frequency(s):
    freq = Counter(s)
    
    chars = sorted(freq.keys(), key=lambda x: (freq[x], x))
    
    result = ""
    for ch in chars:
        result += ch * freq[ch]
    
    return result


print(sort_by_frequency("geeksforgeeks"))
print(sort_by_frequency("abc"))
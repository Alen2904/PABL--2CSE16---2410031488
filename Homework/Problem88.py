from collections import Counter

def winner(arr):
    freq = Counter(arr)
    
    max_votes = max(freq.values())
    
    candidates = [name for name in freq if freq[name] == max_votes]
    
    winner_name = min(candidates)
    
    return [winner_name, str(max_votes)]


print(winner(["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie",
              "john", "johnny", "jamie", "johnny", "john"]))

print(winner(["andy", "blake", "clark"]))
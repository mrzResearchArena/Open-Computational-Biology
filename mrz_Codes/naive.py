def naive(text, pattern):
    occurrences = []
    
    for i in range(len(text) - len(pattern) + 1):
        match = True
        
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                match = False
                break
                
        if match:
            occurrences.append(i)
            
    return occurrences



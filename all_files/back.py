a='python is very easy very easy'
wordss = a.split()
counts = {}
for i in wordss:
    if i in counts:
        counts[i] += 1  # increase count
    else:
        counts[i] = 1   # first occurrence

print(counts)

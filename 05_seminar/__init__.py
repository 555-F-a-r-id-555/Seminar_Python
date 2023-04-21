numbers = [1, 4, 5, 2, 3, 9, 8, 11, 0]
sort = sorted(set(numbers))
ranges = []
start = sort[0]
end = start

for i in range(1, len(sort)):
    if sort[i] == end + 1:
        end = sort[i]
    else:
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}-{end}")
        start = end = sort[i]

if start == end:
    ranges.append(str(start))
else:
    ranges.append(f"{start}-{end}")

print(".".join(ranges))

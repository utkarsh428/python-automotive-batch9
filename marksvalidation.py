mark = [] #empty set
i = 0
while i < 5:
    m = int(input("Enter marks (0-100):"))
    if 0 <= m <= 100:
        mark.append(m)
        i += 1
    else:
        print("Invalid marks,")
    total = sum(mark)
    avg = total / 5
    print("Total:", total, "Average:", avg)
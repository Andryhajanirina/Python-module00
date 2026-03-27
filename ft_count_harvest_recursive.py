def ft_count_harvest_recursive(i=1, days=None):
    if days == None:
        days = int(input("Days until harvest: "))
    print(f"Days {i}")
    if 1 in range(1, days + 1):
        ft_count_harvest_recursive(i, days)
        i += 1
    else:
        print("Harvest time!")

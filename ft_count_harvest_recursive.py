# def ft_count_harvest_recursive(i=1, days=None):
#     if days == None:
#         days = int(input("Days until harvest: "))
#     print(f"Days {i}")
#     if 1 in range(1, days + 1):
#         ft_count_harvest_recursive(i, days)
#         i += 1
#     else:
#         print("Harvest time!")
def ft_count_harvest_recursive(current_day=1, total_days=None):
    if total_days == None:
        total_days = int(input("Days until harvest: "))
    if current_day > total_days:
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    ft_count_harvest_recursive(current_day + 1, total_days)

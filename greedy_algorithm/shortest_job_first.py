def solve(bt):
    bt.sort()
    wait_time=0
    time=0
    for i in bt:
        wait_time+=time
        time+=i
    return wait_time//len(bt)
print(solve([1,2,3,4,5]))
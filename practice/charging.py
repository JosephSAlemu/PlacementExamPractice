def charge(docks: list[int], robots: list[int]) -> list[int]:
    """
    Simulate robot charging process as described in problem statement.

    Parameters:
        docks - List of integers representing dock charge capacity.
        robots - List of integers representing robot charge demand.

    Returns:
        List of integers representing new charge capacity of each dock.
    """
    ret = [x for x in docks]
    for i in range(len(robots)):
        if ret[i] - robots[i] < 0:
            remaining = robots[i] - ret[i]
            ret[i] = 0
            start = i+1
            stop = len(robots)-1
            while start <= stop:
                if ret[start] - remaining < 0:
                    remaining = remaining - ret[start]
                    ret[start] = 0
                else:
                    ret[start] = ret[start] - remaining
                    remaining = 0
                    break
                start+=1

            if remaining > 0:
                start = 0
                stop = i
                while start < stop:
                    if ret[start] - remaining < 0:
                        remaining = remaining - ret[start]
                        ret[start] = 0
                    else:
                        ret[start] = ret[start] - remaining
                        remaining = 0
                        break
                    start +=1
        else:
            ret[i] = ret[i] - robots[i] 
    return ret
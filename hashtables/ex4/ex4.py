def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    temp = []
    # for num in a:
    #     if -num in a:
    #         cache[num] = -num
    #     print(cache)
    # # print(cache)
    # for num in cache:
    #     if cache[num] > 0:
    #         result.append(cache[num])
    # # print(cache)
    for num in a:
        if num < 0:
            cache[num] = -num
    for num in cache:
        if cache[num] in a:
            result.append(cache[num])
    print(cache)
    # print(result)

        
    # # print(cache)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

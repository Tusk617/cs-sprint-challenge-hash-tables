def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    index = -1

    for num in weights:
        index += 1
        cache[index] = num
    print(cache)

    if len(cache) <= 1:
        return None
    if 

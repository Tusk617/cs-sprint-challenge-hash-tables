def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    finalAnsw = []
    for weight in weights:
        cache[weight] = weight
    print(cache)
    if length > 1:
        print("greater!")
        
    else:
        print("Not enough weights!")
        return None

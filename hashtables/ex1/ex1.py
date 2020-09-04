def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_nums = {}
    result = ()
    for weight in weights:
        weight_nums[weight] = weights.index(weight)
    
    if length <= 1:
        print("Not enough inputs")
        return None
    for weight in weight_nums:
        #if the actualy length is shorter than the length provided
        #then a colisson happened, and we have to accomadte for it
        if len(weight_nums) < length:
            return (1, 0)
        #else the length has more than one, and we can begin to check if
        #any of the inputs add up to the limit
        else:
            florbo = weight - limit
            if florbo in weight_nums:
                # print(f"Florbo: {florbo}, Weight: {weight}, Limit: {limit}")
                # print("TRUE!")
                if florbo < weight:
                    # print((weight_nums[florbo], weight_nums[weight]))
                    return (weight_nums[florbo], weight_nums[weight])
                else:
                    # print((weight_nums[weight], weight_nums[florbo]))
                    return (weight_nums[weight], weight_nums[florbo])

            
    
    print(weight_nums)



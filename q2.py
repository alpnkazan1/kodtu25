def q2():
    n = int(input())
    w = list(map(int, input().split()))

    possible_values = set()
    
    def generate_weights(index, current_weight):
        if index == n:
            if current_weight > 0:
                possible_values.add(current_weight)
            return
        
        generate_weights(index + 1, current_weight)
        
        generate_weights(index + 1, current_weight + w[index])
        
        generate_weights(index + 1, current_weight - w[index])

    generate_weights(0, 0)
    
    possible_values = sorted(list(possible_values))
    
    if not possible_values:
        return 1
    
    if possible_values[0] != 1:
        return 1
    
    for i in range(len(possible_values) - 1):
        if possible_values[i+1] - possible_values[i] > 1:
            return possible_values[i] + 1
            
    return possible_values[-1] + 1

def get_statistics(input_list):
    mean = sum(input_list)/len(input_list)
    n = len(input_list)
    sorted_list = sorted(input_list.copy())
    
    mid = int(n/2)
    if n % 2 == 0:
        median = (sorted_list[mid-1] + sorted_list[mid]) / 2
    else:
        median = sorted_list[mid]

    map = {}
    mode = input_list[0]
    sample_variance = 0

    
    max_count = 0
    calculate_sum = 0
    for i in input_list:
        calculate_sum += (i - mean)**2
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
        if max_count < map[i]:
            max_count = map[i]
            mode = i
    
    sample_variance = calculate_sum / (n - 1)

    standard_deviation = sample_variance ** (1/2)

    standard_error = standard_deviation / (n**(1/2))
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": standard_deviation,
        "mean_confidence_interval": [mean-(1.96*standard_error), mean+(1.96*standard_error)]
    }
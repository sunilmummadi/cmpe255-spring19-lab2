import statistics as stat

def mean_num_friends(x):
    # TODO
    mean_friends = stat.mean(x)
    return mean_friends

def median_num_friends(x):
    # TODO
    median_friends = stat.median(x)
    return median_friends

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

print("mean = {}".format(mean_num_friends(num_friends)))

print("median = {}".format(median_num_friends(num_friends)))
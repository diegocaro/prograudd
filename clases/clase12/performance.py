import timeit

def find(data, elem):
    return elem in data

number_trials = 10
    
for size in [100000, 10**6, 10**7, 10**8]:
    x = size - 1
        
    dataset = dict()
    dataset['list'] = list(range(size))
    dataset['tuple'] = tuple(range(size))
    dataset['set'] = set(range(size))
    dataset['frozenset'] = frozenset(range(size))
        
    for (datatype, datavalue) in dataset.items():
        code = "find(dataset['{}'], x)".format(datatype)
        avg_time = timeit.timeit(code, number=number_trials, globals=globals()) / number_trials
        print('Average time for {} elements using {}: {:.3f}s'.format(size, datatype, avg_time))

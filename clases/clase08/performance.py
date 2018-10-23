def testlist():
    return x in L

def testtuple():
    return x in T
    
def testset():
    return x in S

def testfrozenset():
    return x in F

if __name__ == '__main__':
    import timeit
    trials = 20
    
    for f in ['testlist','testtuple','testset','testfrozenset']:
        for m in [100000, 10**6, 10**7, 10**8]:
            x = m - 1
            L = list(range(m))
            T = tuple(L)
            S = set(L)
            F = frozenset(L)
            
            avg_time = timeit.timeit("{}()".format(f), number=trials, globals=globals())/trials
            print('Checking {} with {} elements: {:.3f}s'.format(f,m, avg_time))

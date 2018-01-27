

def parallel_dataframe(dframe, func):
    from multiprocessing import Pool
    import numpy as np
    #redundant
    import pandas as pd
    #4 CPUs with 10 partitions
    dframe_split = np.array_split(dframe, 10)
    pool = Pool(4)
    poolmap = pool.map(func, dframe_split)
    dframe = pd.concat(poolmap)
    pool.close()
    pool.join()
    return dframe

def parse_args():
    import sys
    if len(sys.argv) > 1:
        infile = sys.argv[1]
    else:
        print "Usage:   python " + sys.argv[0] +" infile.csv"
        sys.exit()
        
def outfile_name():
    pass

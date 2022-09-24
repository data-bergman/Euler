
import pandas as pd
import numpy as np
import rpy2
from rpy2 import robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()

def load_large_dta(fname):
    import sys

    reader = pd.read_stata(fname, iterator=True)
    df = pd.DataFrame()

    try:
        chunk = reader.get_chunk(100*1000)
        while len(chunk) > 0:
            df = df.append(chunk, ignore_index=True)
            chunk = reader.get_chunk(100*1000)
            print('.'),
            sys.stdout.flush()
    except (StopIteration, KeyboardInterrupt):
        pass

    print('\nloaded {} rows'.format(len(df)))

    return df
airq=load_large_dta("D:\LSE\preperation 2020\EC221\LT\Lecture notes\irq.dta")


#airq.to_csv("airq", sep='\t')
def save_rdata_file(df, filename):
    r_data = pandas2ri.py2ri(df)
    robjects.r.assign("my_df", r_data)
    robjects.r("save(my_df, file='{}')".format(filename))
    os.chmod(filename, 0o777)
save_rdata_file

save_rdata_file(airq, "airq")
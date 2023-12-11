import pandas as pd

accidents = pd.read_hdf('dataset.h5', key='accidents')
reference = pd.read_hdf('dataset.h5', key='reference')
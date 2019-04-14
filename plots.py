#%%
import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

print("Python version:\n{}\n".format(sys.version))
print("matplotlib version: {}".format(matplotlib.__version__))
print("pandas version: {}".format(pd.__version__))
print("numpy version: {}".format(np.__version__))
print(f"seaborn version: {sns.__version__}")


#%% [markdown]
# ## Plots needed
# - bar plot (summary)
#   - *x*: # of females in breeding group
#   - *y*: avg clutch size
#   - grouped by species
# - line plot
#   - x: clutch sizes
#   - y: clutch count
#   - grouped by species
# - regression plots
#   - x: age of femailes in breeding group at time of clutch
#   - y: avg clutch size
#   - grouped by species
# - line plots
#   - x: age
#   - y: clutch sizes
#   - grouped by individuals


#%%
filename = "example"
df = pd.read_csv(f"data/{filename}.csv", index_col=False)
df

#%%
plt.figure(figsize=(8, 5))
sns.scatterplot(x="x", y="y", data=df, s=100)
plt.savefig(f"output/{filename}.png", transparent=True)


import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

rhymet = 20.59
tacot = 17.77

x = ["Rhyme", "TACO"]
y_time = [rhymet, tacot]

plt.figure(figsize=(8, 6))
ind = np.arange(len(x))
plt.bar(x, y_time)
for i in range(len(x)):
  plt.text(i, y_time[i] + 0.2, y_time[i], ha = 'center')


plt.xlabel('Language', fontsize=16)#, fontweight='bold'
plt.ylabel('Execution Time (ms)', fontsize=16)

plt.title('Comparison of the generated code for Rhyme and TACO', fontsize=16, pad=20)

plt.savefig("evaluation.pdf")
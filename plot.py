import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

density_array = [10, 25, 50, 75]

rhymet = {}
tacot = {}
y_time = []

for density in density_array:
    with open(f"rhyme_{density}.log", 'r') as file:
        rhymeTime = file.read()

    with open(f"taco_{density}.log", 'r') as file:
        tacoTime = file.read()

    print(f"{density}% density\n")

    pattern = r"res:\s*(-?\d+)\s+Iterations:\s*(\d+)\s+Time taken\s*:\s*(-?\d+\.\d+|-?\d+)\s+microseconds"

    match = re.search(pattern, rhymeTime)

    if match:
        r_res_value = int(match.group(1))
        r_iterations = int(match.group(2))
        r_time_taken = float(match.group(3))

        print(f"Iterations: {r_iterations}")
        print(f"Time taken: {r_time_taken} microseconds")

        rhymet[density] = round((r_time_taken / float(r_iterations)) / 1000, 2)
        print(f"Average Rhyme time: {rhymet} ms")
    else:
        print(f"Rhyme time un match.")

    match = re.search(pattern, tacoTime)

    if match:
        t_res_value = int(match.group(1))
        t_iterations = int(match.group(2))
        t_time_taken = float(match.group(3))

        print(f"Iterations: {t_iterations}")
        print(f"Time taken: {t_time_taken} microseconds")

        tacot[density] = round((t_time_taken / float(t_iterations)) / 1000, 2)
        print(f"Average TACO time: {tacot} ms")
    else:
        print(f"Rhyme time un match.")

    if r_res_value != t_res_value:
        print(f"\nRhyme and TACO result not match\n\n")
    else:
        print(f"\nRhyme and TACO result match\n\n")

    y_time.append((density, [rhymet[density], tacot[density]]))

x = ["Rhyme", "TACO"]
#print(y_time)

fig, axs = plt.subplots(1, len(y_time), sharex=False, sharey=False, figsize=(8, 4))
ind = np.arange(len(x))

for idx in range(len(y_time)):
    density = y_time[idx][0]
    y_vals = y_time[idx][1]
    axs[idx].bar(x, y_vals)
    for i in range(len(x)):
      axs[idx].text(i, y_vals[i] * 1.01, y_vals[i], ha = 'center')
    axs[idx].set(xlabel=f"{density}% sparsity", ylabel='Execution Time (ms)')

fig.suptitle('Comparison of the generated code for Rhyme and TACO under different sparsity')

plt.tight_layout()

plt.savefig("evaluation.pdf")

#x = ["Rhyme", "TACO"]
#y_time = [rhymet, tacot]
#
#plt.figure(figsize=(8, 6))
#ind = np.arange(len(x))
#plt.bar(x, y_time)
#for i in range(len(x)):
#  plt.text(i, y_time[i] + 0.2, y_time[i], ha = 'center')
#
#
#plt.xlabel('Language', fontsize=16)#, fontweight='bold'
#plt.ylabel('Execution Time (ms)', fontsize=16)
#
#plt.title('Comparison of the generated code for Rhyme and TACO', fontsize=16, pad=20)
#
#plt.savefig("evaluation.pdf")
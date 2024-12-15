import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

with open('rhyme.log', 'r') as file:
    rhymeTime = file.read()

with open('taco.log', 'r') as file:
    tacoTime = file.read()

pattern = r"res:\s*(-?\d+)\s+Iterations:\s*(\d+)\s+Time taken\s*:\s*(-?\d+\.\d+|-?\d+)\s+microseconds"

match = re.search(pattern, rhymeTime)

if match:
    r_res_value = int(match.group(1))
    r_iterations = int(match.group(2))
    r_time_taken = float(match.group(3))

    print(f"Iterations: {r_iterations}")
    print(f"Time taken: {r_time_taken} microseconds")

    rhymet = round((r_time_taken / float(r_iterations)) / 1000, 2)
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

    tacot = round((t_time_taken / float(t_iterations)) / 1000, 2)
    print(f"Average TACO time: {tacot} ms")
else:
    print(f"Rhyme time un match.")

if r_res_value != t_res_value:
    print(f"\nRhyme and TACO result not match")
else:
    print(f"\nRhyme and TACO result match")

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
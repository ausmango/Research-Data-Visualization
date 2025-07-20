import csv
import matplotlib.pyplot as plt
from collections import Counter

with open(r'C:\Users\austi\Downloads\collegeresearchdataupdated2.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    option_counter = Counter()

    for row in csv_reader:
        responses = row['Question 5'].split(',')
        for response in responses:
            option_counter.update([response.strip()])

options = []
popularity = []

for item in option_counter.most_common(5):
    options.append(item[0])
    popularity.append(item[1])

# reverse to preserve original logic (optional)
options.reverse()
popularity.reverse()

font_options = {'fontname': 'serif', 'fontsize': 12, 'color': 'black'}
fontlabelwhite = {'fontname': 'serif', 'fontsize': 9, 'color': 'white'}
fontlabelblack = {'fontname': 'serif', 'fontsize': 9, 'color': 'black'}

plt.figure(figsize=(10, 5))

plt.yticks(fontname='serif')

bars = plt.bar(options, popularity, color='#238b45')

plt.title("How satisfied were you with your results of ChatGPT for writing?", fontdict=font_options)
plt.ylabel("Amount Chosen", fontdict=font_options)

for i, bar in enumerate(bars): 
    height = bar.get_height()
    percentage = (height / 44) * 100

    plt.text(bar.get_x() + bar.get_width() / 2, height / 2,
             f'{percentage:.2f}%', va='center', ha='center', fontdict=fontlabelwhite)
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
             f'{height:.0f}', va='bottom', ha='center', fontdict=fontlabelblack)

plt.yticks(range(0, max(popularity) + 3, 3))

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.gcf().patch.set_facecolor('white')
plt.gca().patch.set_facecolor('white')

plt.show()

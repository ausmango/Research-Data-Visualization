import csv
import matplotlib.pyplot as plt
from collections import Counter

'''reads through csv file containing response data; splits into 
each response to get exact amount of each answer; not of keys containing answers'''

with open(r'C:\Users\austi\Downloads\conleyresearchdataupdated2.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    option_counter = Counter()

    for row in csv_reader:
        responses = row['Question 3'].split(',')
        for response in responses:
            option_counter.update([response.strip()])

options = []
popularity = []

#counts through each iteration of any answer and labels it into counter
for item in option_counter.most_common(5):
    options.append(item[0])
    popularity.append(item[1])
    
options.reverse()
popularity.reverse()

#declaring various font style and color throughout figure into variables
font_options = fontdict= {'fontname': 'serif', 'fontsize': 12, 'color': 'black'}
fontlabelwhite = fontdict = {'fontname': 'serif', 'fontsize': 9, 'color': 'white'}
fontlabelblack = fontdict= {'fontname': 'serif', 'fontsize': 12, 'color': 'black'}

#hides original y-value label and creates new one with desired font style (font_options)
plt.gca().set_yticklabels([])

for i in range(len(options)):
    plt.text(-0.5, i, options[i], va= 'center', ha= 'right', fontdict= font_options)

plt.xticks(fontname= 'serif')

bars = plt.barh(options, popularity, color='#238b45')

plt.title("Potential Most Used Options", fontdict= font_options)
plt.xlabel("Amount Chosen", fontdict= font_options)

#adds center label onto bars; showing percentage out of total amount of respondees, and then total amount selections on the right of the bars
for i, bar in enumerate(bars):
    width = bar.get_width()
    percentage = (width/44) * 100
    
    plt.text(width/2, bar.get_y() + bar.get_height() / 2, 
             f'{percentage:.2f}%', va='center', ha='center', fontdict=fontlabelwhite)
    plt.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width:.0f}', va= 'center', ha= 'left', fontdict= fontlabelblack)

plt.show()

import matplotlib.pyplot as plt


#Pie Chart for High School demographic data. Color code hues based on 4 values


plt.style.use('fivethirtyeight')

slices = [13.6, 4.6,  31.8, 2.3, 47.4 ]
labels = ['Allowed, but with restrictions; 13.6%', 'Discouraged, but not forbidden; 4.6%', 'Neutral; 31.8%', 'Fully alowed; 2.3', 'Not at all: 47.7%']
colors = ['#238b45', '#66c2a4', '#b2e2e2', '#edf8fb', '#06402B']

plt.pie(slices, labels=labels, colors=colors, wedgeprops= {'edgecolor': 'black'}, 
        textprops= {'fontname': 'serif', 'fontsize': 12, 'color': 'black'})
plt.title("Is ChatGPT allowed for writing assistance with your English teachers?", fontdict= 
          {'fontname': 'serif', 'fontsize': 12, 'color': 'black'})

plt.gcf().patch.set_facecolor('white')
plt.gca().patch.set_facecolor('white')

plt.show()
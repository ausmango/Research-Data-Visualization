import matplotlib.pyplot as plt


#Pie Chart for High School demographic data. Color code hues based on 4 values


plt.style.use('fivethirtyeight')

slices = [13.6, 25, 36.4, 25]
labels = ['Freshman; 13.6%', 'Sophomore; 25%', 'Junior; 36.4%', 'Senior: 25%']
colors = ['#238b45', '#66c2a4', '#b2e2e2', '#edf8fb']

plt.pie(slices, labels=labels, colors=colors, wedgeprops= {'edgecolor': 'black'}, 
        textprops= {'fontname': 'serif', 'fontsize': 12, 'color': 'black'})
plt.title("What is your grade level?", fontdict= 
          {'fontname': 'serif', 'fontsize': 12, 'color': 'black'})

plt.gcf().patch.set_facecolor('white')
plt.gca().patch.set_facecolor('white')

plt.show()
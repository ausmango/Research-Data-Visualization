import matplotlib.pyplot as plt


#Pie Chart for UNC Charlotte demographic data. Color code hues based on 4 values


plt.style.use('fivethirtyeight')

slices = [64.3, 32.1, 3.6]
labels = ['Freshman; 64.3%', 'Sophomore; 32.1%', 'Junior; 3.6%']
colors = ['#238b45', '#66c2a4', '#b2e2e2']

plt.pie(slices, labels=labels, colors=colors, wedgeprops= {'edgecolor': 'black'}, 
        textprops= {'fontname': 'serif', 'fontsize': 12, 'color': 'black'})
plt.title("What is your grade level?", fontdict= 
          {'fontname': 'serif', 'fontsize': 12, 'color': 'black'})

plt.gcf().patch.set_facecolor('white')
plt.gca().patch.set_facecolor('white')

plt.show()
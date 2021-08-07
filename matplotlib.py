import matplotlib.pyplot as plt 

## plotting line chart similarly
plt.plot  
## labelling x and y axis respectively
plt.xlabel, plt.ylabel 
## labelling x and y axis observation tick points respectively
plt.xticks, plt.yticks 
## signifying observation variables
plt.legend() 
## set title of the plot
plt.title() 
## displaying the plot
plt.show() 

## plt.plot(sample_data.column_a, sample_data.column_b)
plt.show()

## To show more than 2 lines in a graph:
## graph is in line
plt.plot(sample_data.column_a, sample_data.column_b) 
#plotgraph
plt.plot(sample_data.column_a, sample_data.column_b,'o') 
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()

plt.plot(us.year, us.population / 10**6)
plt.show()
## x-axis:year
## y-axis:populationnumber

## Add a legend and title to let the graph easier to read
plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()

## To visualize it in percentage:
plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population growth (first year = 100)')
plt.show()

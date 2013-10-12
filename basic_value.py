import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# where we import matplotlib
print "Welcome to value calculation!"

# now we look at some apple stock values
aapl = open("/repos/python_trading/reference_data/aapl.csv", "r")

output_file = open("/repos/python_trading/reference_data/out_aapl.csv","w")

temp_data = None
line_depth = 0

x_vars = []
y_vars = []

for line in aapl:
	if line_depth > 2:

		split_line = line.split(",")
		split_old_line = temp_data.split(",")
		
		today = split_old_line[0]
		today_close = float(split_old_line[-1])
		yesterday_close = float(split_line[-1])
		
		# calculate some value
		final_value = (today_close - yesterday_close)/yesterday_close

		x_vars.append(today)
		y_vars.append(final_value)
		
		# calculate against the risk free rate
		risk_free_final_value = (final_value - 0.04)/252

		print today + " -- " + str(final_value) + " -- " + str(risk_free_final_value)

		output_file.write(today + ", " + str(split_old_line[-1].strip()) + ", "+ str(final_value) + ", " + str(risk_free_final_value) + "\n")

	temp_data = line
	line_depth += 1
	
	

	
# set up	
plt.plot_date(x=days, y=impressions)
plt.show()
	
output_file.close()
aapl.close()

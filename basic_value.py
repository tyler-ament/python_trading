# where we import matplotlib
print "Welcome to value calculation!"

# now we look at some apple stock values
aapl = open("./reference_data/aapl.csv", "r")

output_file = open("./reference_data/out_aapl.csv","w")

temp_data = None
line_depth = 0

for line in aapl:
	if line_depth > 2:

		split_line = line.split(",")
		split_old_line = temp_data.split(",")
		
		today = split_old_line[0]
		today_close = float(split_old_line[-1])
		yesterday_close = float(split_line[-1])
		
		# calculate some value
		final_value = (today_close - yesterday_close)/yesterday_close

		# calculate against the risk free rate
		risk_free_final_value = (final_value - 0.04)/252

		print today + " -- " + str(final_value) + " -- " + str(risk_free_final_value)

		output_file.write(today + ", " + str(split_old_line[-1].strip()) + ", "+ str(final_value) + ", " + str(risk_free_final_value) + "\n")

	temp_data = line
	line_depth += 1
output_file.close()
aapl.close()

import numpy as np
import matplotlib.cbook as cbook
import matplotlib.dates as dates
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt



def process_returns(return_file):
    temp_data = None
    line_depth = 0
    
    x_vars = []
    y_vars = []
    risk_y_vars = []
    
    breakout = 252
    
    for line in return_file:
        if line_depth > 2:
            split_line = line.split(",")
            split_old_line = temp_data.split(",")
            
            today = split_old_line[0]
            today_date = datetime.date(int(today.split("-")[0]), int(today.split("-")[1]), int(today.split("-")[2]))
    
            today_close = float(split_old_line[-1])
            yesterday_close = float(split_line[-1])
    
            
            # calculate some value
            final_value = (today_close - yesterday_close)/yesterday_close
    
    
            x_vars.append(today_date)
            y_vars.append(final_value)
            
            # calculate against the risk free rate
            risk_free_final_value = (final_value - 0.04)/252
            risk_y_vars.append(risk_free_final_value)
    
            #print today + " -- " + str(final_value) + " -- " + str(risk_free_final_value)
    
            #output_file.write(today + ", " + str(split_old_line[-1].strip()) + ", "+ str(final_value) + ", " + str(risk_free_final_value) + "\n")
    
            if breakout == 0:
                break
            breakout -= 1
    
        temp_data = line
        line_depth += 1
        
    return([x_vars, y_vars])
 



# where we import matplotlib
print "Welcome to value calculation!"

# now we look at some apple stock values


aapl = open("/repos/python_trading/reference_data/aapl.csv", "r")
amzn = open("/repos/python_trading/reference_data/amzn.csv", "r")


return_files = [aapl, amzn]
#output_file = open("/repos/python_trading/reference_data/out_aapl.csv","w")

fig, ax = plt.subplots()

for stock_file in return_files:
    new_return = process_returns(stock_file)

    ax.plot(new_return[0], new_return[1])


#ax.plot(x_vars, risk_y_vars)


ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=15))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
#ax.set_xlabel(str(r.date[imid].year))
plt.grid(True)
plt.show()


#output_file.close()
aapl.close()

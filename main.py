import function as f

"""
This contains the main page for the Smart Power Prediction and Monitoring
"""


print("-"*80)
print("-"*80)
print("Welcome to the Main Page of Smart Power Prediction and Monitoring \n")
print("Smart Power Prediction And Monitoring is a power consumpton monitoring \nand prediction software , keep this is still a prototype\n")

#To print the accuracy of the model
f.accuracy()

n = int(input("Enter the week number [from 1 to 104] : "))
print("\n")
volt = float(input("Enter the consumption of the metioned week : "))
z = f.make_pred(n)

#To warn user incase he/she crosses the recommended consumption levels
if volt >  z :
    print("\nWarning!!! you are crossing recommended consumption levels by " + str(volt-z[0]) + " Watts\n")
    
print("Your mentioned consumption is : " + str(volt))
print("\nRecommended voltage consumption is : " + str(z[0]))



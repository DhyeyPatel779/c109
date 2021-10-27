import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result=[]

for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean=sum(dice_result)/len(dice_result)    
sd=statistics.stdev(dice_result)
mode=statistics.mode(dice_result)
median=statistics.median(dice_result)

print("mode= ",mode)
print("median= ",median)
print("mean= ",mean)
print("Standard Deviation= ",sd)

first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

figure=ff.create_distplot([dice_result],["Result"],show_hist=False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))

figure.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="StandardDeviation1"))
figure.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="StandardDeviation1"))

figure.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode="lines",name="StandardDeviation2"))
figure.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="StandardDeviation2"))

figure.show()

data_sd_1=[result for result in dice_result if result > first_sd_start and result < first_sd_end]

data_sd_2=[result for result in dice_result if result > second_sd_start and result < second_sd_end]

data_sd_3=[result for result in dice_result if result > third_sd_start and result < third_sd_end]

print("{}% of data lie between first standard deviation".format(len(data_sd_1)*100/len(dice_result)))
print("{}% of data lie between second standard deviation".format(len(data_sd_2)*100/len(dice_result)))
print("{}% of data lie between third standard deviation".format(len(data_sd_3)*100/len(dice_result)))
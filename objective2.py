#                                                      objective Plot user instrests using matplotlib  pie chart



#import the required files
import matplotlib.pyplot as plt
import re
#function defination
def pichart():

        #opens the file caption.txt

        file=open("caption.txt",'r')
        text=file.read()
        read=re.sub(r'#'," ",text)
        #results in result variable
        result=read.split()

        size=str(result.count("instapic"))+'0'
        size1=str(result.count("widfrnds"))+'0'
        size2=str(result.count("widfrnd"))+'0'


        #Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels="Instagra_pic","weekend_enjoy","movie with friends"
        sizes = [size,size1,size2]
        explode = (0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()


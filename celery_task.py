from celery import Celery
from get_tweets import get_tweets
import json
import re
import os

broker_url = 'pyamqp://guest@localhost//'

app = Celery('celery_task',backend='rpc://', broker= broker_url)

#@app.task
#def function():
 #       final_count = [0,0,0,0,0,0,0,0]
  #      number_of_files = 0
   #     for filename in os.listdir('/mnt/volume/data/'):
    #            number_of_files +=1
     #           try:
      #                  temp = get_tweets('/mnt/volume/data/'+filename)
       #                 for i in range(len(final_count)):
        #                        final_count[i] += temp[i]

         #       except:
          #              print(filename)

       # return final_count

@app.task
def fun(filename):
	count = [0,0,0,0,0,0,0,0]
	try:
        	count = get_tweets('/mnt/volume/data/'+filename)

	except:
        	print(filename)


        return count

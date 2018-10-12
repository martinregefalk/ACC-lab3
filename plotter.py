import matplotlib; matplotlib.rcdefaults()
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

#plt2.use('Agg')
pronouns = ("han", "hon", "hen", "den", "det", "denne", "denna")
y_pos = np.arange(len(pronouns))
result_data = [100524, 33362, 3125, 175994, 75609, 730, 2921]
#result_data2 = [100524, 33362, 3125, 175994, 75609, 730, 2921]

Unique_tweets = 307935.0
#result_data2 = [x / Unique_tweets for x in result_data]
result_data2 = np.array(result_data)/Unique_tweets
#result_data2 = 
print(result_data2)
plt.ioff()
#fig = plt.figure() 
plt.bar(y_pos, result_data2, align='center', alpha=0.5)
plt.xticks(y_pos, pronouns)
#plt.ylabel('Amount')
plt.ylabel('Ratio of unique tweets')
plt.title('Pronoun usage in tweets')
 
plt.show()
#pylab.savefig('plot_of_something.png')
#plt.plot([1,2,3])
plt.savefig('test1a1.png')
#plt.close(fig)

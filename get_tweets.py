import json
import re
import os




def get_tweets(adress):
	json_file = open(adress)
	json_str = json_file.read()
	json_str_split = json_str.split('\n\n')
	result = [0,0,0,0,0,0,0,0]
    	json_str_split.pop()
    	retweets = 0
    	for i in json_str_split:
        	tweet = json.loads(i)

        	if not tweet['text'].split()[0] =="RT":
                	result[7] +=1

                	for word in tweet['text'].lower().split():
                        	word = word.replace(",","")
                        	word = word.replace("!","")
                        	word = word.replace("?","")
                        	word = word.replace(".","")
                        	word = word.replace(":","")
                        	word = word.replace(";","")

                        	if word == "han":
                                	result[0] += 1
                        	elif word == "hon":
                                	result[1] += 1
                        	elif word == "hen":
                                	result[2] += 1
                        	elif word == "den":
                                	result[3] += 1
                        	elif word == "det":
                                	result[4] += 1
                        	elif word == "denne":
                                	result[5] += 1
                        	elif word == "denna":
                                	result[6] += 1
        	else:
                	retweets+=1

    	return(result)



def all_tweets():
	final_count = [0,0,0,0,0,0,0,0]
	number_of_files = 0
	for filename in os.listdir('/mnt/volume/data/'):
		number_of_files +=1
		print(number_of_files)
		try:
			temp = get_tweets('/mnt/volume/data/'+filename)
			for i in range(len(final_count)):
				final_count[i] += temp[i]

		except:
			print(filename)

	return final_count



if __name__ == "__main__":
	#temp = get_tweets()
	temp = all_tweets()

	print("Han:"+ str(temp[0]))
    	print("Hon:"+ str(temp[1]))
    	print("Hen:"+ str(temp[2]))
    	print("Den:"+ str(temp[3]))
    	print("Det:"+ str(temp[4]))
    	print("Denne:"+ str(temp[5]))
    	print("Denna:"+ str(temp[6]))
    	print("Unika Tweets:"+ str(temp[7]))


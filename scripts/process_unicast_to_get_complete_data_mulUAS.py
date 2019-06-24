from netaddr import IPNetwork,IPAddress
from random import shuffle
import re
import numpy as np


def get_number_of_second_last_AS(data):
	lines=data.split('\n')
	for i in lines:
		if 'second' in i and 'AS' in i:
			record=i
			lastsecond=record.split("second")[1]
			return len(lastsecond.split(","))

def get_number_of_last_AS(data):
        lines=data.split('\n')
        for i in lines:
                if 'second' in i and 'AS' in i:
                        record=i
                        lastsecond=record.split("and")[0]
                        return len(lastsecond.split(","))

def get_origin_AS(data):
        lines=data.split('\n')
        for i in lines:
                if  'AS' in i:
                        record=i
                        lastsecond=record.split("and")[0]
                        num_ori=len(lastsecond.split(","))
	if num_ori==1:
		ori_AS=record.split(' ')[4]
		return ori_AS
	elif num_ori>1:
		list_last_AS=re.findall(r'\'(.*?)\'',record.split('and')[0])
		ori_AS=''
		for j in list_last_AS:
			ori_AS+=j+' '
		return ori_AS

def get_list_of_distance(data):
	lines=data.split('\n')
	list_of_distance=[0 for i in range(12)]
	for i in lines:
		if 'distance' in i:
			distance=int(i.split(': ')[1].strip('\n'))
			list_of_distance[distance-1]+=1
	sum_number=sum(list_of_distance)
	if sum_number==0:
		return 0
	else:
		list_of_percentage=[round(i/(sum_number*1.0),3) for i in list_of_distance]
		return list_of_distance,list_of_percentage

def get_stats_of_distance(data):
	lines=data.split('\n')
	list_of_distance=[0 for i in range(12)]
	dist_list=[]
	for i in lines:
		if 'distance' in i:
			distance=int(i.split(': ')[1].strip('\n'))
			list_of_distance[distance-1]+=1
			dist_list.append(distance)
	sum_number=sum(list_of_distance)
	if sum_number==0:
		return 0
	else:
		list_of_percentage=[round(i/(sum_number*1.0),2) for i in list_of_distance]
		num_pairs=sum(list_of_distance)
		num_pairs_1=sum(list_of_distance[1:])
		num_pairs_2=sum(list_of_distance[2:])
		per_pairs_1=sum(list_of_percentage[1:])
		per_pairs_2=sum(list_of_percentage[2:])
		max_d=max(dist_list)
		min_d=min(dist_list)
		array_d=np.array(dist_list)
		mean_d=round(np.mean(array_d),3)
		std_d=round(np.std(array_d),3)
		return num_pairs,num_pairs_1,num_pairs_2,per_pairs_1,per_pairs_2,max_d,min_d,mean_d,std_d

def get_stats_length_ASpath(data):
	lines=data.split('\n')
	pathlen_list=[]
	for i in lines:
		if '|' in i:
			pathlen_list.append(len((i.split('|')[2]).split(' ')))
	max_len=max(pathlen_list)
	min_len=min(pathlen_list)
	array_len=np.array(pathlen_list)
	mean_len=round(np.mean(array_len),3)
	std_len=round(np.std(array_len),3)
	return max_len,min_len,mean_len,std_len



def get_prefix(data):
	prefixes=(data.split('|')[0]).split('\n\n')
	if len(prefixes)>=2:
		prefix_france=prefixes[0]
		prefix_BGP=prefixes[1]
		return prefix_france,prefix_BGP
	else:
		return 0

def get_num_collector(data):
	lines=data.split('\n')
	list_col=[]
        for i in lines:
		if '|' in i:
			list_col.append(i.split('|')[1])
	list_col_final=list(set(list_col))
	return len(list_col_final)

def process_in_block(data):
	results=''
	prefix_france,prefix_BGP=get_prefix(data)
	ori_AS=get_origin_AS(data)
	num_LAS=get_number_of_last_AS(data)
	num_SAS=get_number_of_second_last_AS(data)
	num_collecter=get_num_collector(data)
	check_pairs=get_stats_of_distance(data)
	if check_pairs==0:
		num_pairs=0
		num_pairs_1=0
		num_pairs_2=0
		per_pairs_1=0
		per_pairs_2=0
		max_d=0
		min_d=0
		mean_d=0
		std_d=0
	else:
		num_pairs,num_pairs_1,num_pairs_2,per_pairs_1,per_pairs_2,max_d,min_d,mean_d,std_d=get_stats_of_distance(data)
	max_len,min_len,mean_len,std_len=get_stats_length_ASpath(data)
	#print(prefix_france,prefix_BGP,ori_AS,num_LAS,num_SAS,num_collecter,check_pairs,get_stats_length_ASpath(data))
	results=prefix_france+'|'+prefix_BGP+'|'+ori_AS+'|'+str(num_LAS)+'|'+str(num_SAS)+'|'+str(num_collecter)+'|'+str(num_pairs)+'|'+str(num_pairs_1)+'|'+str(num_pairs_2)+'|'+str(per_pairs_1)+'|'+str(per_pairs_2)+'|'+str(max_d)+'|'+str(min_d)+'|'+str(mean_d)+'|'+str(std_d)+'|'+str(max_len)+'|'+str(min_len)+'|'+str(mean_len)+'|'+str(std_len)
	return results

text=''
index_all=0

start=0
end=10000
block=''
with open('unicast_MulSAS_24prefix.txt') as g:
    for line in g:
        if '*' in line:
            block+=line
            index_all+=1
            #print index_all,' ',round(float((index_all-start)*100)/(end-start),3)
            if start < index_all <=end:
                res=process_in_block(block)
                text+=res+'\n'
                print(res)
                block=''
            elif index_all > end:
                break
            else:
                block=''

        else:
            block+=line

with open('full_results_unicast_MulSAS.txt','w') as haha:
	haha.write(text)

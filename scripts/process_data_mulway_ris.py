# Process raw BGP data, get origin AS and upstream AS, and list the distance of upstream AS for each prefix
# input: raw BGP data,  AS distance files
# output BGP data with origin AS number, upstream AS number, and distance of upstream AS number

from collections import OrderedDict
#from find_distance_of_as_new import distance_of_as
import itertools

filename1 ='ris_asrelation_distance_1_uniq.txt'
filename2 ='ris_asrelation_distance_2_uniq.txt'
filename3 ='ris_asrelation_distance_3_uniq.txt'
filename4 ='ris_asrelation_distance_4_uniq.txt'
filename5 ='ris_asrelation_distance_5_uniq.txt'
filename6 ='ris_asrelation_distance_6_uniq.txt'
filename7 ='ris_asrelation_distance_7_uniq.txt'
filename8 ='ris_asrelation_distance_8_uniq.txt'
filename9 ='ris_asrelation_distance_9_uniq.txt'
filename10='ris_asrelation_distance_10_uniq.txt'
filename11='ris_asrelation_distance_11_uniq.txt'

def distance_of_as1(AS1,AS2):
	rela1=AS1+'>'+AS2
    	rela2=AS2+'>'+AS1
	distance=None
	with open(filename1) as f:
        	for line in f:

			if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=1
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance

def distance_of_as2(AS1,AS2):
	rela1=AS1+'>'+AS2
    	rela2=AS2+'>'+AS1
    	distance=None
    	with open(filename2) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=2
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance

def distance_of_as3(AS1,AS2):
	rela1=AS1+'>'+AS2
	rela2=AS2+'>'+AS1
    	distance=None
    	with open(filename3) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=3
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance

def distance_of_as4(AS1,AS2):
	rela1=AS1+'>'+AS2
    	rela2=AS2+'>'+AS1
    	distance=None
    	with open(filename4) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=4
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
				return distance

def distance_of_as5(AS1,AS2):
	rela1=AS1+'>'+AS2
    	rela2=AS2+'>'+AS1
    	distance=None
    	with open(filename5) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=5
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance

def distance_of_as6(AS1,AS2):
	rela1=AS1+'>'+AS2
    	rela2=AS2+'>'+AS1
    	distance=None
    	with open(filename6) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=6
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance


def distance_of_as7(AS1,AS2):
	rela1=AS1+'>'+AS2
	rela2=AS2+'>'+AS1
	distance=None
    	with open(filename7) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=7
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance

def distance_of_as8(AS1,AS2):
	rela1=AS1+'>'+AS2
    	rela2=AS2+'>'+AS1
    	distance=None
    	with open(filename8) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=8
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance
                                   


def distance_of_as9(AS1,AS2):
	rela1=AS1+'>'+AS2
    	rela2=AS2+'>'+AS1
    	distance=None
    	with open(filename9) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=9
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance

def distance_of_as10(AS1,AS2):
	rela1=AS1+'>'+AS2
    	rela2=AS2+'>'+AS1
    	distance=None
    	with open(filename10) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=10
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance

def distance_of_as11(AS1,AS2):
	rela1=AS1+'>'+AS2
    	rela2=AS2+'>'+AS1
    	distance=None
    	with open(filename11) as f:
        	for line in f:
            		if rela1==line.strip('\n') or rela2==line.strip('\n'):
                		distance=11
                		return distance
            		elif line[0:2]> rela1[0:2] and line[0:2]>rela2[0:2]:
                		distance=None
                		return distance

def distance_from_known(AS1,AS2,list_distance):
	if len(list_distance)<1:
		return 0
	else:
		for i in list_distance:
			#print i
			if AS1==i[0] and AS2==i[1]:			
				return i[2]
			elif AS1==i[1] and AS2==i[0]:
				return i[2]
	return 0


def distance_of_as(AS1,AS2,list_distance):
	distance=distance_from_known(AS1,AS2,list_distance)
	if distance != 0:
		return distance
	else:
		distance=distance_of_as1(AS1,AS2)
    		if distance==1:
        		return distance
    		else:
        		distance=distance_of_as2(AS1,AS2)
        		if distance==2:
            			return distance
        		else:
            			distance=distance_of_as3(AS1,AS2)
            			if distance==3:
                			return distance
            			else:
                			distance=distance_of_as4(AS1,AS2)
                			if distance==4:
                    				return distance
                			else:
                    				distance=distance_of_as5(AS1,AS2)
                    				if distance==5:
                        				return distance
                    				else:
                        				distance=distance_of_as6(AS1,AS2)
                        				if distance==6:
                            					return distance
                        				else:
                            					distance=distance_of_as7(AS1,AS2)
                            					if distance==7:
                                					return distance
                            					else:
                                					distance=distance_of_as8(AS1,AS2)
                                					if distance==8:
                                    						return distance
                                					else:
                                    						distance=distance_of_as9(AS1,AS2)
                                    						if distance==9:
                                        						return distance
                                    						else:
                                        						distance=distance_of_as10(AS1,AS2)
                                        						if distance==10:
                                            							return distance
                                        						else:
                                            							distance=distance_of_as11(AS1,AS2)
                                            							if distance==11:
                                                							return distance
                                            							else:
                                                							return 12





def process_block(data,list_distance_set):
	results=''
    	data_one_coltr=[]
    	last_collector='start'
    	data_of_collectors=[]
	list_distance_found=[]
    	for i in data:
        	collector=i.split('|')[1]
        	if collector==last_collector:
            		data_one_coltr.append(i)
        	else:
            		#process data in one collector
            		if len(data_one_coltr)>=1:
                		#results=results+process_data_in_one_collector(data_one_coltr)
                		data_of_collectors.append(data_one_coltr)
            		data_one_coltr=[]
            		data_one_coltr.append(i)
            		last_collector=collector    
    #results=results+process_data_in_one_collector(data_one_coltr)
    	list_of_last2rdas_within=[]
    	data_of_collectors.append(data_one_coltr)
    	for k in data_of_collectors:
        	list_of_last2rdas=[]
        	for p in k:
            		path=p.split('|')[2].split(' ')
	    		if len(path)>1:
            			list_of_last2rdas.append(path[-2])
        	if len(set(list_of_last2rdas))>1:    
            		list_pair_one=list(itertools.combinations(list_of_last2rdas,2))
            		list_of_last2rdas_within+=list_pair_one
    	list_lastAS=[]
    	list_lastSecondAS=[]
    	raw_data='*'*20+'\n'
    	for i in data:
        	raw_data=raw_data+i+'\n'
        	aspath=i.split('|')[2].split(' ')
        	list_lastAS.append(aspath[-1].strip('\n'))
		if len(aspath)>1:
            		list_lastSecondAS.append(aspath[-2])
    	list_last_AS=list(set(list_lastAS))
    	list_last_second_AS=list(set(list_lastSecondAS))
    	if len(list_last_second_AS)>1:
        	list_pair_last_second_AS=list(itertools.combinations(list_last_second_AS,2))
    	
	if len(list_last_AS)==1 and len(list_last_second_AS)==1:
        	results=raw_data+'Only have one last AS: '+list_last_AS[0]+' and one second last AS:'+list_last_second_AS[0]+'\n'
    	elif len(list_last_AS)>1 and len(list_last_second_AS)==1:
        	results=raw_data+'have mutiple last AS: '+str(list_last_AS)+' and one second last AS:'+list_last_second_AS[0]+'\n'
	elif len(list_last_second_AS)==0:
		results=raw_data+'Only have one last AS: '+list_last_AS[0]+'\n'
    	elif len(list_last_AS)==1 and len(list_last_second_AS)>1:
        	results=raw_data+'have one last AS: '+list_last_AS[0]+' and multiple second last AS:'+str(list_last_second_AS)+'\n'
        	list_of_pair=list(set(list_pair_last_second_AS)-set(list_of_last2rdas_within))
        	for pair in list_of_pair:
        		distance=distance_of_as(pair[0],pair[1],list_distance_dataset)
			list_distance_found.append((pair[0],pair[1],distance))
        		results+='distance of '+pair[0]+' and '+pair[1]+' : '+str(distance)+'\n'
        elif len(list_last_AS)>1 and len(list_last_second_AS)>1:
        	results=raw_data+'have mutiple last AS: '+str(list_last_AS)+' and multiple second last AS:'+str(list_last_second_AS)+'\n'
        	list_of_pair=list(set(list_pair_last_second_AS)-set(list_of_last2rdas_within))
        	for pair in list_of_pair:
        		distance=distance_of_as(pair[0],pair[1],list_distance_dataset)
        		results+='distance of '+pair[0]+' and '+pair[1]+' : '+str(distance)+'\n'
			list_distance_found.append((pair[0],pair[1],distance))
    
	return results,list_distance_found

data_block=[]

start,end=raw_input('please enter two numbers: start and end\n').split()

print start,end

start_int=int(start)
end_int=int(end)
#start=0
#end=10000


last_prefix='0.0.0.0/0'
 

with open('ris_raw_data.txt') as file1:
	results=''
	list_distance_dataset=[]
	index=0
	#index1=0
	for line in file1:
        	#index1+=1
		#print index1, index1
        	if index%10==0:
			print start,' - ', index#, 'prefix',prefix
			with open('mulway_ris_accum_'+start+'_'+end+'.txt','a') as g:
				g.write(results)
			results=''
			#list_distance_sort=list(set(list_distance_dataset))
			#list_distance_dataset=list_distance_sort
		if len(list_distance_dataset)>10000:
			list_distance_dataset=[]
        	

		prefix=line.split('|')[0]
		
        	if prefix==last_prefix:
            		data_block.append(line.strip('\n'))
        	else:
			index+=1
			if start_int< index <= end_int:
				results_processing,list_distance_data=process_block(data_block,list_distance_dataset)
            			results=results+results_processing
				list_distance_dataset+=list_distance_data
			#	list_distance_sort=list(set(list_distance_dataset))
			#	list_distance_dataset=list_distance_sort
				print last_prefix
            		#print process_block(data_block)
            			data_block=[]
            			data_block.append(line.strip('\n'))
            			last_prefix=prefix
			elif index <= start_int:
				last_prefix=prefix
				data_block=[]
				data_block.append(line.strip('\n'))
				continue
			else:
				break
        results_processing,list_distance_data=process_block(data_block,list_distance_dataset)  
    	results=results+results_processing   


with open('mulway_ris_accum_'+start+'_'+end+'.txt','a') as lala:
	lala.write(results)



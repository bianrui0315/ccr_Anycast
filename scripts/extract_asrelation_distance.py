# process raw BGP file, get the distance of AS
# input: raw BGP data
# output: AS distance files from 1 to 11

filename='raw_BGP.txt'

def get_asrelation(data,n):
	path=data.strip('\n')
	ASes=path.split(' ')
	as_rela=''
	if len(ASes)<n+1:
		return 0
	else:
		for i in range(len(ASes)-n):
			if ASes[i]!='' and ASes[i+n]!='':
				as_rela+=ASes[i]+'>'+ASes[i+n]+'\n'
	return as_rela

for k in range(1,12):
	print('distance: '+str(k))
	AS_relations=''
	with open(filename,'r') as f:
		i=0
		for line in f:
			i+=1
			AS_relation=get_asrelation(line,k)
			if AS_relation!=0:
				AS_relations+=AS_relation
			
			if i%100000==0:
				#AS_relations_new=list(set(AS_relations))
				#AS_relations_new.sort()
				#AS_relations=AS_relations_new
				print(str(i))
				with open('/home/rui/BGP/raw_data/ris_asrelation_distance_'+str(k)+'.txt','a') as f1:
					f1.write(AS_relations)
				AS_relations=''
	#AS_relations_new=list(set(AS_relations))
	#AS_relations_new.sort()
	#AS_relations=AS_relations_new
#	print(k)
	with open('/home/rui/BGP/raw_data/ris_asrelation_distance_'+str(k)+'.txt','a') as g:
		g.write(AS_relations)

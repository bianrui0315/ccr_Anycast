# construct datasets for classification
# input: unicast and anycast feature data
# output：datasets with features N1, P1, P2, MD, ML


def make_datasets(para):
	
	datasets=''
	with open('full_results_unicast.txt') as f:
		for line in f:
			data=line.strip('\n').split('|')
			datasets+='U,'
			for i in para[:-1]:
				datasets+=data[i]+','
			datasets+=data[para[-1]]+'\n'
	

	with open('full_results_anycast.txt') as k:
		for line1 in k:
			data1=line1.strip('\n').split('|')
			datasets+='A,'
			for s in para[:-1]:
				datasets+=data1[s]+','
			datasets+=data1[para[-1]]+'\n'

	return datasets
	
parasets=[0,4,9,11,15]
res=make_datasets(parasets)
for j in parasets:
	print(parasets.index(j),j)

with open('datasets_prefix_N_P1_MD_ML.txt','w') as g:
	g.write(res)

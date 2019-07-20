# Passive Analysis of Anycast Routing and the Impact of Remote Peering


> **Towards Passive Analysis of Anycast in Global Routing: Unintended Impact of Remote Peering**,<br>
> Rui Bian, Shuai Hao, Haining Wang, Amogh Dhamdere, Alberto Dainotti, and Chase Cotton.<br>
> ACM SIGCOMM Computer Communication Review (CCR), Volume 49 Issue 3, July 2019.


We developed a passive method to study IP anycast by utilizing BGP data.
We proposed a set of BGP-related features to classify anycast/unicast prefixes by using the BGP data (RouteViews and RIPE RIS) and evaluated the effectiveness of our approach by using the active measurement results as a near-ground-truth. The results show that 
our approach achieves high classification accuracy, about 90\% for anycast and 99\% for unicast. 

While further delving into the causes of inaccuracy, we found that remote peering has an unintended impact on anycast routing, due to its invisibility at layer-3, breaking the assumption that the peered autonomous systems are physically close and provide a short path. In our study, 19.2\% of anycast prefixes are sensitive to remote peering and around 40\% of such prefixes are further confirmed to be impacted by remote peering via traceroute measurements. [[paper](https://github.com/bianrui0315/ccr_Anycast/blob/master/paper/acmdl19-306.pdf)]

## scripts
- `construct_datasets.py`: construct datasets for classification from `full_results_anycast.txt` and `full_results_unicast.txt`  and datasets contain five features ```N, P1, P2, MD, ML```, details in [paper](https://github.com/bianrui0315/ccr_Anycast/blob/master/paper/acmdl19-306.pdf) §3.2
- `extract_asrelation_distance.py`: process raw BGP file (BGP data from RouteViews and RIPE RIS from June 1st 00:00 UTC to June 1st 23:59 UTC) and extract the distance of ASes
- `process_anycast_to_get_complete_data.py`: process BGP data (BGP data from RouteViews and RIPE RIS from June 1st 00:00 UTC to June 1st 23:59 UTC) and extract BGP features
- `process_data_mulway_ris.py`: process raw BGP data, extract origin/upstream ASes, and the distance of upstream ASes for each prefix
- `process_unicast_to_get_complete_data.py`: process unicast prefix BGP data (BGP data from RouteViews and RIPE RIS from June 1st 00:00 UTC to June 1st 23:59 UTC) and extract BGP features
- `decision_tree_save_results.py`: classification using decision tree algorithm
- `randomforest_save_results`: classification using random forest algorithm

## data
### Passive Anycast Detection
- `anycast_2017_uniq.txt`: (near-)Ground truth of [anycast prefixes](https://anycast.telecom-paristech.fr/dataset/) from [Anycast enumeration](https://anycast.telecom-paristech.fr/) ([CoNEXT'15 paper](https://conferences2.sigcomm.org/co-next/2015/img/papers/conext15-final100.pdf))
- `as_distance`: AS distance from RIPE RIS and RouteViews data
- `datasets_prefix_N_P1_P2_MD_ML.txt`: feature data for classification
- `full_results_anycast.txt`: anycast prefix feature data, the format is  
```
prefix in groundtruth|prefix in BGP|origin AS|number of orgin AS|number of upstream AS (N)|number of collectors|number of upstream AS pairs|number of upstream AS pairs whose distance above 1|number of upstream AS pairs whose distance above 2| Percentage of upstream AS pairs whose distance is more than 1 (P1)|Percentage of upstream AS pairs whose distance is more than 2 (P2)|maximum distance between upstream ASes (MD)| minimum of distance between upstream ASes| mean of distance| standard deviation of distance|maximum length of AS paths (ML)|minimum of length of AS paths|mean of length of AS paths| standard deviation of length of AS paths
```
- `full_results_unicast.txt`: unicast prefixes' feature data, format is same as `full_results_anycast.txt`
- `full_results_all.txt`: all prefixes' feature data constructed from raw BGP data (BGP data from RouteViews and RIPE RIS from June 1st 00:00 UTC to June 1st 23:59 UTC), format is same as `full_results_anycast.txt` (except no groundtruth prefixes, because they are constructed from Raw BGP data)
- `res_DT_5.txt`: results of decision tree classification
- `res_RF_5.txt`: results of random forest classification

### Remote Peering Data/Experiments
- `Anycast-data-UMD`: Anycast experiment data from University of Maryland's [D-Root Nameserver](http://www.cs.umd.edu/projects/droot/) ([SIGCOMM'18 paper](http://www.cs.umd.edu/projects/droot/anycast_sigcomm18.pdf))
- `asn_ixp`: IXP member ASNs and remote peering ASes (IXP member ASN collected from IXP websites; remote peering AS data from [IMC'18 remote peering paper](https://www.inspire.edu.gr/wp-content/pdfs/uncovering_remote_peering_interconnections_v1.pdf))
- `aspair_ixp`: AS pair of IXP member and remote peering IP (constructed from `IXP_members` and `asn_ixp`)
- `rp_in_ixp`: BGP searching results of remote peering (using AS pairs to search in anycast prefix BGP records)
- `anycast_2017_uniq.txt`: (near-)Ground truth of anycast prefixes from [Anycast enumeration](https://anycast.telecom-paristech.fr/)
- `atlas_exp_prefix_msmid.txt`: Measurement ID of [RIPE Atlas](https://atlas.ripe.net/)
- `inferences_all.txt`: information including local and remote peering from IMC'18 remote peering paper
- `inferences_remote.txt`: remote peering information from IMC'18 remote peering paper
- `traceroute_prefix_ip_path.txt`: traceroute results (IP paths) from RIPE Atlas experiments
- `traceroute_prefix_asn_pyasn.txt`: ASN paths from RIPE Atlas experiments
- `path collection`: path collection (details in [paper](https://github.com/bianrui0315/ccr_Anycast/blob/master/paper/acmdl19-306.pdf) §5.2) results from RIPE Atlas traceroute experiments

Due to limit of size, we didn't include large files like BGP data, which can be downloaded from RouteView/RIPE NCC, or retrieved from CAIDA's [BGPStream](https://bgpstream.caida.org/). If you need those files to reproduce your results, we have included the method in our paper and feel free to contact us by email (bianrui@udel.edu).

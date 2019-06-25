# Towards Passive Analysis of Anycast in Global Routing: Unintended Impact of Remote Peering


> **Towards Passive Analysis of Anycast in Global Routing: Unintended Impact of Remote Peering**,<br>
> Rui Bian, Shuai Hao, Haining Wang, Amogh Dhamdere, Alberto Dainotti, and Chase Cotton.<br>
> ACM SIGCOMM Computer Communication Review (CCR), Volume 49 Issue 3, July 2019.


We developed a passive method to study IP anycast by utilizing BGP data.
We proposed a set of BGP-related features to classify anycast and unicast prefixes. Using the datasets collected from RouteViews and RIPE RIS, we evaluated the effectiveness of our proposed approach. The evaluation results show that 
our approach achieves high classification accuracy, about 90\% for anycast and 99\% for unicast. While further delving into the causes of inaccuracy, we found that remote peering has an unintended impact on anycast routing.  In our study, 19.2\% of anycast prefixes are sensitive to remote peering and around 40\% of such prefixes are further confirmed to be impacted by remote peering via traceroute measurements. 



## scripts
- `construct_datasets.py`: construct datasets for classification
- `decision_tree_save_results.py`: classification using decision tree algorithm
- `extract_asrelation_distance.py`: process raw BGP file, get the distance of AS
- `process_anycast_to_get_complete_data.py`: process BGP data get BGP features
- `process_data_mulway_ris.py`: Process raw BGP data, get origin AS and upstream AS, and list the distance of upstream AS for each prefix
- `process_unicast_to_get_complete_data.py`: process unicast prefix BGP data get BGP features
- `randomforest_save_results`: classification using random forest algorithm

## data
### Passive Anycast Detection
- `anycast_2017_uniq.txt`: (near-)Ground truth of anycast prefix (coNEXT paper)
- `as_distance`: AS distance from RIS and RoutViews
- `datasets`: datasets  using features N, P1, P2, MD, MLfor classification
- `full_results_anycast.txt`: anycast prefix feature data, the format is  
```
prefix in groundtruth|prefix in BGP|origin AS|number of orgin AS|number of upstream AS (N)|number of collectors|number of upstream AS pairs|number of upstream AS pairs whose distance above 1|number of upstream AS pairs whose distance above 2| Percentage of upstream AS pairs whose distance is more than 1 (P1)|Percentage of upstream AS pairs whose distance is more than 2 (P2)|maximum distance between upstream ASes (MD)| minimum of distance between upstream ASes| mean of distance| standard deviation of distance|maximum length of AS paths (ML)|minimum of length of AS paths|mean of length of AS paths| standard deviation of length of AS paths
```
- `full_results_unicast.txt`: unicast prefixes' feature data, format is same as full_results_anycast.txt
- `full_results_all.txt`: all prefixes' feature data, format is same as full_results_anycast.txt expect no prefix in groundtruth column
- `res_DT_5.txt`: results of decision tree classification
- `res_RF_5.txt`: results of random forest classification

### Remote Peering Data/Experiments
- `Anycast-data-UMD`: Anycast experiment data from University of Maryland (SIGCOMM'18 paper)
- `asn_ixp`: IXP member ASN and remote peering AS(IXP member ASN from IXP websites, remote peering AS provided by the author of IMC'18 remote peering paper)
- `aspair_ixp`: AS pair of IXP member and remote peering IP(made based on the last file)
- `IXP_members`: IXP member ASN(from IXP websites)
- `rp_in_ixp`: BGP searching results of remote peering(using AS pairs to search in anycast prefix BGP records)
- `anycast_2017_uniq.txt`: (near-)Ground truth of anycast prefix (coNEXT paper)
- `atlas_exp_prefix_msmid.txt`: measurement ID of RIPE Atlas(from atlas experiments)
- `find_rp_ip_in_traceroute_stat.txt`: searching remote ip in ip path of atlas exp and show the number of ixp that remote ip belong with(from Altas experiments and data provided by the author of IMC'18 remote peering paper)
- `find_rp_ip_in_traceroute.txt`: searching remote ip in ip path of atlas exp and show the ixp that remote ip belong with(from Altas experiments and data provided by the author of IMC'18 remote peering paper)
- `inferences_all.txt`: information including local and remote peering(provided by the author of IMC'18 remote peering paper)
- `inferences_remote.txt`: remote peering information(provided by the author of IMC'18 remote peering paper)
- `traceroute_prefix_ip_path.txt`: atlas exp results IP path(results of atlas experiments)
- `traceroute_prefix_asn_pyasn.txt`: atlas exp results ASN path(AS mapping the results of last file)

Due to limit of size, we didn't include large files like BGP data, which can be downloaded from RouteView/RIPE NCC, or retrieved from CAIDA's [BGPStream](https://bgpstream.caida.org/). If you need those files to reproduce your results, we have included the method in our paper and feel free to contact us by email (bianrui@udel.edu).

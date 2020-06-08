# Homework 6

Following are the files that were created as well as performance information for running BERT on v100 and p100

<b> v100 </b><br>
Ran 1M training dataset and 500k validation dataset on v100

Following is the filename and performance observed for EPOCH=1.  
<i> BERT_classifying_toxicity_v100.ipynb </i>

Tokenizer<br>
33724<br>
CPU times: user 25min 46s, sys: 7.69 s, total: 25min 53s<br>
Wall time: 25min 48s<br>
<br>
Train<br>
CPU times: user 1h 18min 2s, sys: 31min 43s, total: 1h 49min 46s<br>
Wall time: 1h 49min 43s<br>


Following is the filename and performance observed for EPOCH=2.  <br>
<i> BERT_classifying_toxicity_v100_2epochs.ipynb </i>

Tokenizer<br>
33724<br>
CPU times: user 25min 18s, sys: 7.92 s, total: 25min 26s<br>
Wall time: 25min 22s<br>
<br>
Train<br>
CPU times: user 2h 36min 51s, sys: 1h 3min 19s, total: 3h 40min 11s<br>
Wall time: 3h 40min 5s<br>


<b> p100 </b><br>
Ran for 10k / 1M training dataset and 5k / 500k validation dataset on p100<br>


Following is the filename and performance observed for EPOCH=1 on 10k training dataset and 5k validation dataset  
<i>BERT_classifying_toxicity.ipynb</i>
Tokenizer<br>
358<br>
CPU times: user 34.3 s, sys: 2.02 s, total: 36.3 s<br>
Wall time: 37.5 s<br>
<br>
Train<br>
CPU times: user 2min 15s, sys: 1min 24s, total: 3min 39s<br>
Wall time: 3min 39s<br>


<i>BERT_classifying_toxicity_p100.ipynb</i>
Tokenizer<br>
33724<br>
CPU times: user 34min 4s, sys: 11.1 s, total: 34min 15s<br>
Wall time: 34min 3s<br>
<br>
Train<br>
CPU times: user 3h 52min 4s, sys: 2h 18min 51s, total: 6h 10min 56s<br>
Wall time: 6h 10min 43s<br>

<br>
Since it took 6 hours to run for 1M training dataset for EPOCH=1, did not run it again for EPOCH=2 for p100 as it would have ran for 12+ hrs
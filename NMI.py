from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn import metrics
import pandas as pd
pred = pd.read_csv('lifejournal/outputCom.csv')
true = pd.read_csv('lifejournal/labels.csv')
true = true['communities']
pred = pred['communities']
true = pd.array(true)
pred = pd.array(pred)
finaltrue = []
finalpred = []
for i in range(len(true)):
    if(true[i] != 0):
        finaltrue.append(true[i])
        finalpred.append(pred[i])
print('Final number of nodes:'+str(len(finalpred)))
unique_list = []
for x in finalpred:
    if x not in unique_list:
        unique_list.append(x)
print('Unique communities in the predicted data:'+str(len(unique_list)))
unique_list = []
for x in finaltrue:
    if x not in unique_list:
        unique_list.append(x)
print('Unique communities in the labeled data:'+str(len(unique_list)))
print('NMI:'+str(normalized_mutual_info_score(finaltrue,finalpred)))
print('Rand index:'+str(metrics.adjusted_rand_score(finaltrue,finalpred)))
print("...."
      "orkut"
      "----")
pred = pd.read_csv('orkut/outputCom.csv')
true = pd.read_csv('orkut/labels.csv')
true = true['communities']
pred = pred['communities']
true = pd.array(true)
pred = pd.array(pred)
finaltrue = []
finalpred = []
for i in range(len(true)):
    if(true[i] != 0 and pred[i] != 0):
        finaltrue.append(true[i])
        finalpred.append(pred[i])
print('Final number of nodes:'+str(len(finalpred)))
unique_list = []
for x in finalpred:
    if x not in unique_list:
        unique_list.append(x)
print('Unique communities in the predicted data:'+str(len(unique_list)))
unique_list = []
for x in finaltrue:
    if x not in unique_list:
        unique_list.append(x)
print('Unique communities in the labeled data:'+str(len(unique_list)))
print('NMI:'+str(normalized_mutual_info_score(finaltrue,finalpred)))
print('Rand index:'+str(metrics.adjusted_rand_score(finaltrue,finalpred)))
print("...."
      "Youtube"
      "----")
pred = pd.read_csv('youtube/outputCom.csv')
true = pd.read_csv('youtube/labels.csv')
true = true['communities']
pred = pred['communities']
true = pd.array(true)
pred = pd.array(pred)
finaltrue = []
finalpred = []
for i in range(len(true)):
    if(true[i] != 0):
        finaltrue.append(true[i])
        finalpred.append(pred[i])
print('Final number of nodes:'+str(len(finalpred)))
unique_list = []
for x in finalpred:
    if x not in unique_list:
        unique_list.append(x)
print('Unique communities in the predicted data:'+str(len(unique_list)))
unique_list = []
for x in finaltrue:
    if x not in unique_list:
        unique_list.append(x)
print('Unique communities in the labeled data:'+str(len(unique_list)))
print('NMI:'+str(normalized_mutual_info_score(finaltrue,finalpred)))
print('Rand index:'+str(metrics.adjusted_rand_score(finaltrue,finalpred)))

# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

print(data)
 
# Code starts here


#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
count_deliveries=0
for deliv in (data["innings"][0]["1st innings"]["deliveries"]):
    for delivery_num,delivery_info,in deliv.items():
        if(delivery_info["batsman"]=="SC Ganguly"):
           count_deliveries==1
print("the of deliveries faced by SC Ganguly is",count_deliveries)


#  Who was man of the match and how many runs did he scored ?
man_of_match=data["info"]["player_of_match"]
print("the man of the match", man_of_match)


run_scored=0
for deliv in data["innings"][0]["1st innings"]["deliveries"]:
    for delivery_num,delivery_info,in deliv.items():
        if(delivery_info["batsman"]==man_of_match[0]):
           run_scored +=delivery_info["runs"]["batsman"]
print("the number of runs scored by the man of the match",run_scored)        




#  Which batsman played in the first inning?
batsman_list=[]
for deliv in (data["innings"][0]["1st innings"]["deliveries"]):
     for delivery_num,delivery_info,in deliv.items():
          bats_name=delivery_info["batsman"]
          if bats_name not in batsman_list:
             batsman_list.append(bats_name)

print("the batsman playing in first inning are",batsman_list)


# Which batsman had the most no. of sixes in first inning ?

most_sixes_batsman=[]
for deliv in (data["innings"][0]["1st innings"]["deliveries"]):
     for delivery_num,delivery_info,in deliv.items():
          if(delivery_info["batsman"]==6):
              most_sixes_batsman.append(delivery_info["batsman"])
batsman_sixes=Counter(most_sixes_batsman)
print(batsman_sixes)

# Find the names of all players that got bowled out in the second innings.
list_out=[]
for deliv in (data["innings"][1]["2nd innings"]["deliveries"]):
    for delivery_num,delivery_info in deliv.items():
         if "wicket" in delivery_info and delivery_info["wicket"]["kind"]=="bowled":
             list_out.append(delivery_info["wicket"]["player_out"])
print(list_out)


         




# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extra_2nd_inning=[]
for deliv in (data["innings"][1]["2nd innings"]["deliveries"]):
    for delivery_num,delivery_info in deliv.items():
        if "extras" in delivery_info:
            extra_2nd_inning.append(delivery_info["extras"])


extra_1st_inning=[]
for deliv in (data["innings"][0]["1st innings"]["deliveries"]):
    for delivery_num,delivery_info in deliv.items():
        if "extras" in delivery_info:
            extra_1st_inning.append(delivery_info["extras"])

print("no of extras more in 2nd innings",len(extra_2nd_inning)-len(extra_1st_inning))




# Code ends here



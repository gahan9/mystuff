#!/bin/sh

PROJECT_ROOT="/f/Projects"
cd $PROJECT_ROOT

CLG_ROOT="/f/Projects/LAB_nirmauniv/"
for i in "CD_lab" "DPS_lab" "DWM_lab" "MachineLearning" "ML_lab" "ResearchSeminar" "RTS_lab"
do
   cd $CLG_ROOT$i
   echo "running git pull for $i.. from: "
   pwd
   git pull
done

read -n1 -r -p "Press any key to exit..." key

# for i in "mystuff" "inventory_management" "meta_fetcher" "hr_mgmt" "AIview" "profile_test_automation"
# do
#    cd $PROJECT_ROOT'/'$i
#    echo "running git pull for $i.. from: "
#    pwd
#    git pull origin master
# done

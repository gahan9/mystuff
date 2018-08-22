#!/bin/sh

PROJECT_ROOT="/home/jarvis/Projects"
cd $PROJECT_ROOT

CLG_ROOT="/home/jarvis/Projects/LAB_nirmauni/"
for i in "ACN_lab" "DSA_lab" "DBS_lab" "CA_lab" "SE_lab"
do
   cd $CLG_ROOT$i
   echo "running git pull for $i.. from: "
   pwd
   git pull
done


for i in "mystuff" "inventory_management" "meta_fetcher" "hr_mgmt" "AIview" "profile_test_automation"
do
   cd $PROJECT_ROOT'/'$i
   echo "running git pull for $i.. from: "
   pwd
   git pull origin master
done

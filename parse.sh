alt=2000
echo "date,pilot,parapente,heure,total,start 2 exit,takeoff 2 start" > exits_${alt}.csv

for i in ../traces/* ; do
  python igc_lib_demo.py $i $alt >> exits_${alt}.csv
done

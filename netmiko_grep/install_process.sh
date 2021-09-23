
OF=/home/kbyers/pynet_articles/
echo $OF

# cd /home/kbyers/pynet_articles/
# rm -r /home/kbyers/pynet_articles/.test_venv
# /usr/local/bin/python3.9 -m venv .test_venv

# if [ -d "/path/to/dir" ] 
#then
#    echo "Directory /path/to/dir exists." 

#$ pip install git+https://github.com/ktbyers/netmiko.git@develop
#$ pip install pyyaml
#
## Verify Netmiko 4.X code is being used
#$ pip list | grep netmiko
#netmiko       4.0.0a4
#
## Verify netmiko-grep is on your path
#$ which netmiko-grep
#~/VENV/netmiko_test/bin/netmiko-grep
#
## Create your .netmiko.yml inventory
#$ vi ~/.netmiko.yml 
#
## Test that it works
#$ netmiko-grep 'vlan' cisco3
#vlan internal allocation policy ascending 

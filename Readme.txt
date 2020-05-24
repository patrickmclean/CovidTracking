# Run with Anaconda 3.6.1
# Package manager conda

To update covid data, in terminal:
git fetch CovidData
then update endData in readData.py

To Run
Start server/webserver2.py
goto localhost:8080

Connect to ec2 instance:
Goto config folder
run launch.sh
make sure instance is running first...

Setting up the server on ec2
Check python 3 is installed
yum list installed | grep -i python3
latest pip 
pip install pip --upgrade
this didn't work so:
paths are missing
export PATH=$PATH:/usr/local/bin

install cherrypy and pandas with
python3 -m pip install some_module

if pip insn't working
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user

Get new covid CovidData
goto Covid-Data directory
git pull origin master



## Tickets to come ##
5. Update the covid data daily
8. Clean up graph presentation - legends, colors etc
9. Make it responsive
10. Script for deployment. ftp, stop and restart server etc
11. Divide by population
12. Add Counties
13. Compare regions
14. Show daily plus 7 day overlay




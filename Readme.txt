# Run with Anaconda 3.6.1
# Package manager conda

# Run locally
Launch webserver from root directory: python3 ./server/webserver2.py
Launch http://localhost:8080/

# Updating data
Should be working automatically as cronjob
Job is in Scripts/.crontab (or .crontabsvr)
Update with vi (i for insert, esc, then :wq to write out)
Update new script with: crontab ./.crontabsvr
Logs are written to cron.log
Running every day at 12 - pulls from github

# Access the server
Goto Scripts and run: ./sshaws.sh 
This assumes instance is running. 
If instance is stopped and restarted then IP address will need to be updated in this script

# Running the webserver
Login via SSH above
cd CovidTracking
python3 Server/webserver2.py

Application is running on X.X.X.X:8080


# Setting up a new server on ec2
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


## Tickets to come ##
9. Make it responsive
10. Script for deployment. ftp, stop and restart server etc
11. Divide by population
12. Add Counties
13. Compare regions
14. Show daily plus 7 day overlay




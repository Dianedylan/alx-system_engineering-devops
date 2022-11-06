0x19. Postmortem
[When things go sideway, make sure to learn from failure](https://www.youtube.com/watch?v=rp5cVMNmbro)


Project issue started on 1st November 2022, at 2200h EAT and ended on 2nd November 2022, at 1900h EAT after i had gone back to mysql project to rectify things in database replication.
The impact this issue had was that the project was not able to be tested on. Data in my web server 1 and SQL database were not able to be accessed.
The root cause of this issue was that the MySQL service was not running and installed and that upon firewall activation and allowing port 22, i exited the server and was not able to join server again with the error:
ssh: connect to host port 22 : connection refused
ssh: connect to host port 22 : connection timed out
 
This issue was found by running the command:
Ssh -i ~/.ssh/id_rsa ubuntu@myIPAddress 
This issue was resolved by hard rebooting the server which still did not seem to get me connected until about a day was over.
This may be prevented in the future by checking if the ufw service is running and port 22 allowed on servers one wishes to connect prior to the replication and also mysql installed on both servers. 
Timeline
Issue occurred after running a ufw command to allow all incoming traffic through port 22.
Issue detected when error message appeared.
Actions taken included investigating how to connect back through ssh.
Misleading investigation on checking the ssh_config file to change port to 22 which was not necessary as the issue wasn't there.
Incident escalated to asking fellow cohort 5 peer Ben Oketch to take a look at the error message and advise as I thought I'd never be able to join the server via ssh again.
Resolution
Ben advised me to give the hard reboot process time, so that I didn't have to generate a new ssh key and server and start over. He also advised me to install mysql service in server 2 and have it started before being able to interact with it once ssh connection to the servers was back up.
   Prevention
Remember to always read the error messages and to not panic! The initial panic caused me to not rationally think and simply Google what was wrong if I could not figure it out from the line ssh: connect to host port 22 : connection refused/ timed out.

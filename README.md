# Kill-Process

Python = 2.7 
Kill the program without searching for its pid if that process got hanged or taking long time.

Have set the alias as "die" to call this program.

Have opened a very big file in geditor and it got hanged.
i dont need to search pid for gedit process.
just give the program name.
aks@aks:~/workspace/sample$ die gedit
[sudo] password for aks: 
Found proces : 20836 pts/0    00:00:00 gedit
found ['20836', '0', '00', '00', '00']
Going to kill process having pid: 20836
Status:0

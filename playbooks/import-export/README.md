# README

## AAP Backup_and_Restore 

- Standalone cli 

- Uses surveys
  - what is host1 IP
  - host1 login 
  - host1 password 
  - what is host2 IP
  - host2 login
  - host2 password

- Creates  working directory /var/lib/awx/projects/Backup on host1 if it doesnt exist
- Exports ALL controller artifacts to file in  /var/lib/awx/projects/Backup/ on host1 
- Creates /var/lib/awx/projects/Backup on host2 if it doesn't exist
- Sends the backup file to host2 /var/lib/awx/projects/Backup
- Imports the Artifact JSON 

> NOTE: Survey questions can be removed or # out  and replaced by template survey in Controller 
>
> Taken from Shadd G AAP Backup and Restore script

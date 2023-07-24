## AWS Backup Guide
This is a guide on setting up a AWS Backup. The AWS Backup service allows you to create backups of your resources in AWS and even create failover of your resources to a different AWS region.

### Objective
Once set up, we should have a good understanding of how to set up regular backups of our resources and how to resource our resources from the snapshots.

### Create Vault
First, you need to set up a vault where your snapshots are going to be stored.

1. Go to Create Vault and click "Create backup vault".
2. Give the vault a name:
```
Backup vault name = "mydb-1d-snapshots"
```
Optional: Select an encryption key

3. If you want the backup to failover to another region, repeat the above steps in the destination region.

### Create Backup Plan
Next, you need to create a backup plan which tells AWS Backups how you want it to take the snapshots and what the retention will be.

1. Go to Backup Plans and click "Create Plan".

2. Give the plan a name.
```
Backup plan name = "mydb-backup-plan"
```

3. Create the rule.
```
Backup rule name = "mydb-1d-snap-1mo-retain"
Backup vault = "mydb-1d-snapshots"
Backup frequency = "Weekly"
Enable PITR = False
Backup window = "Use backup window defaults"
Transition to cold storage = "Never"
Retention period = "1 Month"
```

4. If you want the backup to failover, then select the desination region under "Copy to destination", select the vault you created in that region, and then select a desired transition and retention period.


5. If you are backing up EC2 instances and require application consisent, select "Windows VSS" under Advanced backup settings.
```
Windows VSS = True
```

6. Once configured, click "Create plan".

### Assign Resources
Lastly, you need assign the resources that you want to backup to the backup plan.

1. Give your resource assignment a name.
```
mydb_dynamodb
```

2. Leave IAM role as default.

3. Define how you want to select the resources. Then select your resources.
```
Define resource selection = "Include specific resource types"
```

Note: if you want to use tags to select your resources then select "Include all resource types", and define the key value pair. See example below.
```
Key = "Name"
Condition = "Begins with"
Value = "mydb"
```

4. Once configured, click "Assign resources".

Now you have created your backup plan and AWS should start doing your backups.

### Restoring Your Backup
After AWS Backups has created backup snapshots, you can now restore your resources.

1. Navigate to the vault you created, "mydb-1d-snapshots". Then click "Restore backups".

2. Give the table a name, leave the other settings as blank, and click "Restore backup".
```
Table name = "mydb"
```

### Conclusion
Now you are setup and connect to your Lightsail instance.
```
ssh -i /Users/user/Keys/LightsailDefaultKey-us-east-1.pem ubuntu@192.0.1.0
```


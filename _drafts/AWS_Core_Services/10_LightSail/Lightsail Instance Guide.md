## Lightsail Instance Guide
This is a guide on setting up a Lightsail instance. A Lightsail instance is basically a virtualized computer. It's a very powerful tool that can be used in many applications such as hosting your own website, running your own server, and much more.

### Objective
Once set up, we should have two accounts where a resource from the source account can read, write, access, etc the resources of the destination account.

Once set up, we should be able to SSH into our Lightsail instance with the following command (Linux, MAC):
```
ssh -i /Users/user/Keys/LightsailDefaultKey-us-east-1.pem ubuntu@192.0.1.0
```
For windows, we should be able to connect through PuTTY (see PuTTY guide for details).

### Create Instance
To create the instance, do the following:
1. Go to the AWS console, search and click on Lightsail to access the Lightsail Console.
2. Click on the Instances tab and click the "Create Instance" button.
3. Under instance location, you can select which region you want your instance to be located. Choose the location that best fits your needs or closest to you. If you don't have a preference, then go with Virginia us-east-1.
```
Select a Region = "us-east-1"
```
4. Select a Platform, for our purposes go with Linux/Unix:
```
Select a platform = "Linux/Unix"
```
5. Select a blueprint. Here is where you can choose from different specialized machine setups depending on your use case. For general use cases, click on OS Only, and it's recommended that you use the latest Amazon Linux or the latest version of Ubuntu. For this guide, let's go with Ubuntu.
```
Select a blueprint = "Ubuntu"
```
6. On Change SSH Key pair, this is where you can create a new SSH key or use a custom SSH key. We can just use the default key. More on this later. For this step, just make sure the default key is selected.
```
Default key = True
```
7. Next, choose and instance plan. This gives you an idea of the pricing and the specs of your instance. Choose a plan that fits your use case. 
8. Next, give your instance a name under the identify your instance section.
```
Identify your instance = "My_First_Instance"
```
9. Leave all other settings as default and click create.

### Attach a Static IP
Oftentimes, it's good to have a static ip address for our instance. Static ip addresses don't change when you take the instance offline for maintenance for example. This is important especially if you are using it to host a website or server.

To attach a Static IP address to our server:
1. In the home page of the Lightsail console click on Networking, then click "Create static IP".
2. For the Static IP location, make sure you select the same region in which you created your instance.
3. Under Attach to an instance, select the instance.
```
Attach to an instance = "My_First_Instance"
```
4. Leave all other settings as default and click create.

### Editing Firewall Rules
In order to allow connections, we will need to open up some ports to our instance.

1. Click on our instance and click the Networking tab.
2. Scroll down to IPv4 Firewall and make sure it is configured with the following rules. Note that, SSH port 22 and HTTP port 80 should be open by default. HTTPS is often also needed for many use cases.
```
Allow Rule 1: SSH TCP 22
Allow Rule 2: HTTP TCP 80
Allow Rule 3: HTTPS TCP 443
```
3. Do the same for IPv6 Firewall.
```
Allow Rule 1: SSH TCP 22
Allow Rule 2: HTTP TCP 80
Allow Rule 3: HTTPS TCP 443
```

### Connecting to Instance
In order to connect, we need to download our SSH key.
1. Go to the AWS console and click on Account and click the SSH keys tab.
2. Depending on which key you used, find the key and download it. Since we used the default key for us-east-1, you can find the key under Default keys and store it in a SAFE place.
```
Default keys = "us-east-1"
```

Now we can connect to our instance using SSH. If you're using Linux/Mac:
1. Open a terminal window on your local machine.
2. Use the following command to make the private key of the key pair readable and writable only by you. This is a security best practice required by some operating systems.
```
sudo chmod 400 /Users/user/Keys/LightsailDefaultKey-us-east-1.pem
```
3. Finally, use the following command to connect to your instance. Replace the ip address with the public ip address of your instance. If you attached a static ip then this is your static ip.
```
ssh -i /Users/user/Keys/LightsailDefaultKey-us-east-1.pem ubuntu@192.0.1.0
```
See this guide for more details:
* https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-ssh-using-terminal

If you're using Windows, see PuTTY guide for details or refer to this detailed guide:
* https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-connecting-to-linux-unix-amazon-ec2-instances

### Conclusion
Now you are setup and connect to your Lightsail instance.
```
ssh -i /Users/user/Keys/LightsailDefaultKey-us-east-1.pem ubuntu@192.0.1.0
```


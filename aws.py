import pyttsx3
import speech_recognition as sr
import os
import getpass
import time
os.system("cls")

print("------------------------------------|||||||||||||||||||||||||||||||||||||||------------------------------------------")
print("\t\t\t\t     WELCOME TO THE AMAZON WEBSERVER WORLD")
print("---------------------------------------------------------------------------------------------------------------------")
pyttsx3.speak("Welcome to the amazon web server   world")
print("\n")
time.sleep(2)
pyttsx3.speak("Hi..! i am your personal assistant savvy..please identify yourself before accessing aws because your security is our first priority ........! Enter your password")

#w=input("Press ENTER to Enter Your Password")
w="pass"

for w in "pass":
	password=getpass.getpass("\nEnter your Password -")
	if password == "Arth@2020":
		time.sleep(2)
		

		print("\t\t\t\t\tHow can i help you..! please tell me")
		pyttsx3.speak("How can i help you..! please tell me")
		time.sleep(2)
		#pyttsx3.speak("you have set shortcuts in aws")
		print("\n")
		print("\t\t\t\t\t|1.Create Key-Pair              |")
		time.sleep(1)
		print("\t\t\t\t\t|2.Create Security Group        |") 
		time.sleep(1)
		print("\t\t\t\t\t|3.Launch ec2 Instance          |")
		time.sleep(1)
		print("\t\t\t\t\t|4.Create an EBS Volume         |")
		time.sleep(1)
		print("\t\t\t\t\t|5.Attach Volume With Instances |\n\n")
		time.sleep(1)

		while True:
	
			r = sr.Recognizer()	
			with sr.Microphone() as source:
	 			print("\nWhat's Your Requirements Please Tell Me : -  ")
	 			audio = r.listen(source)

			ch = r.recognize_google(audio)
			print(ch)
	    
			if ("create" in ch) and ("key" in ch) and ("pair" in ch):
				pyttsx3.speak("Please Provide a Key Name")
				i=input("Key Name :- ")
				pyttsx3.speak("creating key pair in aws with name {} ".format(i))
				os.system("aws ec2 create-key-pair --key-name {} ".format(i))
		
                
			elif  ("create" in ch) and ("security" in ch) and ("group" in ch):
				pyttsx3.speak("Please Provide a security group Name")
				i=input("Security Group Name :- ")
				j=input("\nSecurity Description:- ")
				os.system("aws ec2 create-security-group --group-name {} --description {}".format(i,j))
				pyttsx3.speak("successfully created Security group with name {}".format(i))

			elif ("Launch" in ch) or ("launch" in ch) and ("instance" in ch) or ("for me" in ch):
				pyttsx3.speak("Here is the list of instances.....!!! Choose an Amazon Machine Image ")
				print("\n\t\t\t\t\t1.Red Hat Enterprise Linux 8 ")
				time.sleep(0.5)
				print("\t\t\t\t\t2.Amazon Linux 2 AMI")
				time.sleep(0.5)
				print("\t\t\t\t\t3.Amazon Linux AMI ")
				time.sleep(0.5)
				print("\t\t\t\t\t4.SUSE Linux Enterprise Server 15 SP2 ")
				time.sleep(0.5)
				print("\t\t\t\t\t5.Microsoft Windows Server 2019 Base")
				time.sleep(0.5)
		
				a=input("\n\nEnter Your Choice :- ")
		

				if int(a)==1:
					b="ami-0e306788ff2473ccb"
					
					i=input("\nKey Name :- ")
					sec=input("Enter your security group id -  ")
					pyttsx3.speak("launching instances and the name of instance is Red Hat Enterprise Linux 8 ")
					os.system("aws ec2 run-instances  --image-id {}  --instance-type    t2.micro --count 1 --subnet-id subnet-fc7b7294 --security-group-ids {}  --key-name {}".format(b,sec,i))

				elif int(a)==2:
					b="ami-0e306788ff2473ccb"
					i=input("Key Name :- ")
					pyttsx3.speak("launching instances and the name of instance is Amazon Linux 2 AMI")
					os.system("aws ec2 run-instances  --image-id {}  --instance-type    t2.micro --count 1 --subnet-id subnet-74e09f38 --security-group-ids sg-0722c1ae22f865f76  --key-name {} ".format(b,i))

		
				elif int(a)==3:
					b="ami-03cfb5e1fb4fac428"
					i=input("Key Name :- ")
					pyttsx3.speak("launching instances and the name of instance is Amazon Linux AMI")
					os.system("aws ec2 run-instances  --image-id {}  --instance-type    t2.micro --count 1 --subnet-id subnet-74e09f38 --security-group-ids sg-0722c1ae22f865f76  --key-name {} ".format(b,i))
		
				elif int(a)==4:
					b="ami-0d0522ed4db1debd6"
					i=input("Key Name :- ")
					pyttsx3.speak("launching instances and the name of instance is S U S E Linux Enterprise Server 15 S P 2 ")
					os.system("(aws ec2 run-instances  --image-id {}  --instance-type    t2.micro --count 1 --subnet-id subnet-74e09f38 --security-group-ids sg-0722c1ae22f865f76  --key-name {} ".format(b,i))

				elif int(a)==5:
					b="ami-0b2f6494ff0b07a0e"
					i=input("Key Pair Name :- ")
					pyttsx3.speak("launching instances and the name of instance is Microsoft Windows Server 2019 Base")
					os.system("aws ec2 run-instances  --image-id {}  --instance-type    t2.micro --count 1 --subnet-id subnet-74e09f38 --security-group-ids sg-0722c1ae22f865f76  --key-name {} ".format(b,i))

				else:
					pyttsx3.speak("ops..! please Choose form given Amazon images list")
					print("ops..! please Choose form given Amazon images list")
					continue


			elif ("create ebs volume" in ch) or ("Create EBS volume " in ch) or ("create volume" in ch) or ("Create Volume" in ch) or  ("Create EBS volume " in ch) :
				pyttsx3.speak("Please Provide a volume Name")
				i=input("EBS Volume Name :- ")
				j=input("Size of Volume(in GB) : -")
				pyttsx3.speak("Please...! choose any specific availability zone ")
				print("\n\t\tAvailabilty Zones -")
				print("\n\t\t1. ap-south-1a")
				print("\n\t\t2. ap-south-1b")
				print("\n\t\t3. ap-south-1c\n\n")
				s=input("\n\nSelect Availability Zone:-")
				if int(s)==1:
					b="ap-south-1a"
					pyttsx3.speak("Creating Ebs Volume in aws and the name of ebs volume is My Volume and size is one giga byte")
					time.sleep(2)
					pyttsx3.speak("Successfully created EBS volume")
					os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1a --tag-specifications ResourceType=volume,Tags=[{Key=Name,Value=Myvolume}]")
				elif int(s)==2:
					b="ap-south-1b"
					pyttsx3.speak("Creating Ebs Volume in aws and the name of ebs volume is My Volume and size is one giga byte")
					time.sleep(2)
					pyttsx3.speak("Creating Ebs Volume in aws and the name of ebs volume is My Volume and size is one giga byte".format(i))
					os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1b --tag-specifications ResourceType=volume,Tags=[{Key=Name,Value=Myvolume}]")

				elif int(s)==3:
					b="ap-south-1c"
					pyttsx3.speak("Creating Ebs Volume in aws and the name of ebs volume is My Volume and size is one giga byte")
					time.sleep(2)
					pyttsx3.speak("Creating Ebs Volume in aws and the name of ebs volume is My Volume and size is one giga byte".format(i))
					os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1c --tag-specifications ResourceType=volume,Tags=[{Key=Name,Value=Myvolume}]")		


			elif (("attach volume" in ch) or ("Attach Volume" in ch) or ("Attach EBS Volume" in ch)) or ("attach ebs volume" in ch):
				pyttsx3.speak("Which instance do you want to attach the volume")
				i=input("Instance Id :- ")
				pyttsx3.speak("give me volume id")
				j=input("volume id:- ")
				pyttsx3.speak("Attaching the volume with given instance id")
				time.sleep(2)
				pyttsx3.speak("Successfully attachted volume with your instance")
				os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf ".format(j,i))
			elif ("exit" in ch) or ("thank you" in ch) or ("Thank You" in ch) :
				exit()
 
			else:
				print("It is out of the aws ... ")

	else:
		pyttsx3.speak("You have entered wrong password please renter your password")
		continue

  

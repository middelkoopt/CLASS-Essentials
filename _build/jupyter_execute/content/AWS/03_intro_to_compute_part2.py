#!/usr/bin/env python
# coding: utf-8

# # Instance Storage, Tags & Security Groups
# 
# 
# ```{admonition} Overview
# :class: tip
# 
# **Teaching:** 45 mins
# 
# **Exercises:** 10 mins
# 
# **Questions:**
# * What is an EC2 instance?
# * When would I use an EC2 instance?
# * How do I launch an EC2 instance?
# 
# **Objectives:**
# * Understand the concept of virtual servers.
# * Understand what an Elastic Cloud Compute (EC2) instance is.
# 
# ```

# Recall that the two fundamental components of cloud computing is compute and storage. On AWS, a "virtual server" or "virtual computer" is known as an **Elastic Cloud Compute (EC2) instance**; sometimes it's called "EC2", sometimes it's called an "instance" to denote that the ability to build and terminate this server instantaneously, but they all mean the same thing. An EC2 instance is no different from a server that sits under your desk, or your local departmental cluster, or even your local HPC cluster. You even boot up an EC2 instance through the web console, install software and then shut down your instance just like you would a real computer, except that Amazon takes care of the physical machinery while you are in charge of process of creating the computer. In some sense, you can think of utilizing an EC2 instance as renting a server or computer from Amazon! 
# 
# In cloud jargon, the term **elasticity** denotes the ability to quickly expand or decrease computer processing, memory, and storage resources to meet changing demands. In that way, you can expand the size of your CPU, RAM and disk size on your EC2 instance almost instantenously. Since EC2 forms the backbone of most of AWS's core infrastructure, it is an important part of your cloud journey.  
#  
# 
# Let's walk through some of the steps on getting an EC2 instance up and running. 
# 

# We begin with the AWS console again. Under the "Build a Solution" panel, select `Launch a Virtual Machine`
# 
# <img src="./images/console_ec2.png" width=720 align="center">
# 
# <div align="center">Figure 1: Start page for the AWS console</div><br/>
# 
# This will then lead you through a series of steps to get a **Free Tier** EC2 instance up and running. 
# 
# ```{admonition} Note
# :class: note
# 
# AWS Free Tier refers to several of the services that AWS offers to help users gain more hands on experience on the AWS platform without being charged. [Click here](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all) for more info about the AWS Free Tier [external link] . 
# ```
# 
# There are 7 steps to walk through to create a new EC2 instance; we will go through each in detail: 
# 1. Select an AMI
# 2. Choose Instance Type
# 3. Configure Instance 
# 4. Add Storage
# 5. Add Tags
# 6. Configure Security Group
# 7. Review/Launch

# ## 1. Select an AMI
# 
# An Amazon Machine Image (AMI) is a template that Amazon uses to describe the operating system, disk type and all the software configuration that is needed to make sure a computer runs smoothly. Imagine that you are purchasing a new laptop; fresh out of the box, the laptop is pre-configured with an operating system (e.g. Windows, Mac OS, Ubuntu etc.), configuration files that tells the laptop what peripherals are attached, and pre-installed software like Adobe PDF reader. An AMI contains all this information so that your EC2 instance runs exactly like it would a new laptop out of the box! There is much more to learn about AMIs and how they can used for collaboration and data sharing but that is not within the scope of CLASS Essentials. 
# 
# As you scroll through the AMI list (Figure 2) you will notice that the list contains offerings from various vendors (e.g. Amazon, RedHat, Windows, etc.). We will be choosing the Ubuntu operating system for flexibility and versatility (can be used outside of the AWS ecosystem). 
# 
# To list all the Free Tier AMIs, check the box on the right that says ```Free tier only```.
# 
# <img src="./images/ec2-ami.png" width=720 align="center">
# 
# <div align="center">Figure 2: Step 1 - Select an AMI - Free Tier Only </div><br/>
# 
# Scroll to ```Ubuntu Server 20.04 LTS(HVM), SSD Volume Type``` (Figure 3). Select ```64-bit(x86)```. 
# 
# <img src="./images/ec2-ubuntu.png" width=720 align="center">
# 
# <div align="center">Figure 3: Step 1 - Select an AMI - Operating System Selection </div><br/>

# ## Step 2: Choose an Instance Type
# 
# Choosing an instance type is choosing the hardware for your computing system: you get to pick the number of CPUs and memory size for your instance. 
# 
# Instance types are group by [**families**](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) and denotes whether, for example, an instance is optimized for batch processing (compute-optimized, C-family), optimized for databases (memory-optimized, R-family) or has accelerated hardware (GPUs) for AI or Machine Learning pipelines. 
# 
# When you choose an Instance Type (Figure 3), the screen show additional information about the selected instance type including the number of CPUs, the memory size, the type of storage and information about networking. 
# 
# In the Instance Storage (GB) column, you will notice a term called **EBS**. EBS is the acronym for **Elastic Block Storage** and is analogous to the hard disk or boot drive on your personal computer or laptop. More details about EBS and different kinds of disk storage on EC2 instances are beyond the scope of CLASS Essentials. 
# 
# ```{admonition} Note
# :class: note
# The four most common types of storage you will encounter on AWS are: Elastic Block Storage (EBS), Elastic File Storage (EFS), Simple Storage Service (s3) and s3 Glacier. In the simplest terms, EBS is analogous to a computer hard drive and EFS is analogous to a network file system (NFS) or shared file system. s3 is AWS's object storage which is discussed [here](./intro_to_s3). s3 Glacier is a cost-effective way of storing s3 files that you do not need to access frequently. 
# ```
# 

# <img src="./images/ec2-type.png" width=720 align="center">
# 
# <div align="center">Figure 3: Step 2 - Choose an Instance Type</div><br/>
# 
# Select ```Next: Configure Instance Details``` and we'll move on to the next chapter. 

#!/usr/bin/env python
# coding: utf-8

# # Introduction to the AWS Console
# 
# 
# ```{admonition} Overview
# :class: tip
# 
# **Teaching:** 15 mins
# 
# **Exercises:** 5 mins
# 
# **Questions:**
# * How do I navigate the web console?
# 
# **Objectives:**
# * Log in to the AWS web console
# * Navigate the AWS web console
# * Recognize important information about your cloud environment
# 
# ```

# 

# ### Setup
# 
# The console is the point of entry where you will start your AWS journey. If you are participating in the CLASS Essentials Workshop, you will have received a csv file via email. This csv file contains your **username**, **temporary password** and **console login link**. 
# 
# ```{admonition} Be Aware
# :class: danger
# If you are doing self-paced learning, your login information may be different!
# ```
# 
# ### Logging in to the console
# Paste your console login link into your web browser. You will see the AWS site requesting you to sign in as an IAM user. Fill in your username and password that was assigned to you in the csv file. You will be asked to change your password the first time you sign in to the console. Fill in your old password and then choose a new password that you can remember! 
# 
# You are now logged on. Welcome to the first step of your cloud journey! 
# 
# Figure 1 is what your screen should look like when you log in to the AWS console for the first time. If you encounter any pop up boxes, you can exit them. Next, let's take a closer look at some key concepts and components of the AWS console. 
# 
# <img src="./images/intro_to_cloud_console/console_start.png" width=720 align="center">
# 
# <div align="center">Figure 1: First time logging in to the AWS console</div><br/>

# ### Key concepts and components of the AWS console
# <img src="./images/intro_to_cloud_console/console_start_labeled.png" width=720 align="center">
# 
# <div align="center">Figure 2: Basic but important components of the AWS Console</div><br/>
# 

# Figure 2 lists the basic components you will see when you first log in to the AWS console. 
# 
# **1. Services**
# : If you click on the dropdown menu labeled "Services" you will see the entire list of services that is offered by AWS. Currently, AWS has over 200 services ranging from compute to machine learning to networking to data storage. The list grows frequently!
# 
# **2. Search bar**
# : You can also use the search bar to find a particular service or offering that you are interested in. Cloud vendors have proprietary vocabulary or jargon, so it is often useful to be aware of those as you start exploring more in your cloud adoption journey. [Internet2's CLASS Core documentation](https://github.internet2.edu/pages/CLASS/CLASS-Essentials-AWS/vendor_vocabulary.html) provides a basic list of vendor specific cloud terminology. For example, if you wanted to provision or utilize a "virtual server", you can try using the search bar to search for "EC2" which stands for "Elastic Cloud Compute" and is the AWS vocabulary for virtual computers.
# 
# **3. IAM Username and Account**
# : The menu bar on the console also lists your IAM username and account number. IAM is short for Identity and Access Management. Identity is a mechanism to authenticate users (e.g. password) and Access is a mechanism for authorizing what kinds of services users have access to. For example, in this scenario, student1 is an IAM user on the account "4414-3982-1395". In the creation of the IAM user "student1", the administrator (overlord) of the account assigned a particular permission scope (in AWS this is known as roles) to ensure that student1 only has access to a particular set of services and also assigned a password to authenticate user login. IAM is a key component in managing security on the cloud.
# 
# **4. Region**
# : AWS (and most cloud providers) uses the term region to denote the physical location of the data center(s) you are building your cloud service(s) in. Here we see that the region is "Ohio". This literally means that as you develop some of your AWS components like compute and storage, the physical location of your server and data is in the state of Ohio! Regions are important to know and understand for two major reasons: costs and latency. Transferring data between regions in AWS incurs what is known as a inter-region data fee (roughly $0.16/GB as of 2021). If you work with larger datasets, you may find that data transfer speeds (e.g. downloading, processing data, etc.) in different regions can occur more slowly due to something called latency. For the sake of optimizing costs and minimizing latency, you are encouraged to choose a region that is closest to you and your cloud data.  For the CLASS Essentials Workshop, we will use "Ohio" as the region. 
# 
# **5. Quick links** 
# : As you work more frequently on the console, your frequently used services will pop up on your console, and you can also access the entire suite of AWS services via the All Services drop down. 
# 

# ```{admonition} Exercise
# :class: attention
# 
# * What is your IAM username? 
# * Why is IAM important?
# * What are the three ways you can find an AWS service on the console?
# ````

# In[ ]:





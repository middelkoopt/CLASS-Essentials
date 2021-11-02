#!/usr/bin/env python
# coding: utf-8

# # Cloud Computing for Research
# 
# 
# ```{admonition} Overview
# :class: tip
# 
# **Teaching:** 5 mins
# 
# **Exercises:** 0 mins
# 
# **Questions:**
# * What is cloud computing for research?
# 
# **Objectives:**
# * Understand the basics of what the cloud is.
# * Understand the benefits of utilizing the cloud for research.
# 
# ```

# ## Background
# 
# Cloud computing is an on-demand computing resource that is scalable and follows a pay-as-you-go model. Instead of a singular data center or super-computing center, large cloud providers have data centers spanning multiple locations. The largest cloud computing providers are [Microsoft (Azure)](https://azure.microsoft.com/), [Amazon (Amazon Web Services, AWS)](https://aws.amazon.com/) and [Google (Google Cloud Platform, GCP)](https://cloud.google.com/). Together, they are often referred to as “public” or “commercial” cloud providers.
# 
# In contrast to buying your own desktop or laptop computer, a cluster of machines, or with buying external storage devices (such as a RAID, redundant array of independent disks), cloud computing allows you to provision computing and storage on machines that only available to you through an intermediated interface (such as a web-browser or through ssh). Simply put, cloud computing is a delivery of computing services over the Internet. 
# 
# ## Benefits of the Cloud for Research
# 
# Many researchers move to the commercial cloud simply because their local compute resources (local HPC clusters, or departmental clusters) are insufficient to deal with the volume of data and type of computation. With the cloud, there is no wait time to obtain the computing resources you need. With sufficient funds, you may even be able to obtain a near infinite number of CPUs, RAM and GPUs and compute can start as soon as you want it!
# 
# With cloud computing, you do not need to purchase or maintain and update hardware, operating systems and a slew of dependencies. For the most part, providers maintain their hardware. Further, cloud providers just keep making new services to keep up with demands the rapidly expanding community building cloud-native workflows. Cloud providers are constantly evolving their tools and resources with a focus on storage, reliability, and security.
# 
# ## A Change in Paradigm
# Working on the cloud involves a paradigm shift: researchers are no longer bringing their data to the compute (i.e. downloading data) but are instead bring their compute to the data. Cloud computing constitutes a learning curve including knowing cloud vocabulary and understanding the best practices to accelerate your research workflow, optimize costs and ensure security of your cloud architecture.
# 
# ## Drew's Pipeline
# Drew Anders is an ecologist who works on understanding how much [boreal Arctic lakes are greening](https://www.pnas.org/content/118/15/e2021219118) under current climate conditions. To assess this, Drew needs to process 158.6TB (150 scenes) of satellite imagery from a cloud-hosted storage bucket and extract [Normalized Difference Vegetation Index (NDVI)](https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index) values.  Drew is currently using the departmental computing server to download and process the data using a Python script, `process_sat.py` and is uploading the processed data to an FTP server to share with collaborators. 
# 
# Unfortunately, the departmental server is running out of storage space and the processing units have insufficient memory to process the data. Drew has calculated that with the departmental server, the wall clock time to download, process and analyze the data would take 48 days. Drew has to publish a paper by the end of the month for a special issue of "Ecology Outsphere Today". Further, Drew needs to make processed data available to reviewers of the publication and to collaborators. 
# 
# After speaking with the deparmental IT administrator, Drew has decided to explore cloud computing as a means for scalability (increasing computational power), data storage, and to reduce the time to publication. Drew's PI has a approved a small amount of money to be spent on a prototype, with potential for turning a successful cloud-based workflow into a grant proposal. 
# 
# Over the next few lessons in the CLASS Essentials course, Drew will learn how to:
# 1. Utilize cloud compute to increase processing speed and memory and reduce wall clock time
# 2. Utilize cloud storage buckets to store and retrieve data
# 3. Run `process_sat.py` on cloud compute and retrieve data directly from cloud storage
# 4. Monitor costs and understand best practices for working on the cloud
# 

# In[ ]:





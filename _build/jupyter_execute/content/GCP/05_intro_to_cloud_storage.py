#!/usr/bin/env python
# coding: utf-8

# ## Introduction to Google Cloud Storage
# 
# Learner Questions
#  * How do I store data in the cloud?
# 
# Learning Objectives:
#  * Navigate the Google Cloud Storage service and terminology
#  * Understand the roles and permissions needed to use Google Cloud Storage in projects
#  * Allocate storage in Google Cloud Storage
#  * Find the cost estimator for Google Cloud Storage
#  * Recognize that resources have a "location"
#  * Recognize danger of public access
#  * De-allocate Google Cloud Storage storage

# Drew, after working with a Research Computing and Data (RCD) facilitator, has decided to start their cloud journey with storage. Data is usually the center of a research project and it makes sense to start here.
# 
# One of the most common and economic ways to store data in the cloud is to use object storage.  In GCP object storage is called *Google Cloud Storage*, which is similar to the Simple Storage Service, also known as S3, on Amazon Web Services (AWS).  For object storage, information is stored as a collection of key-value pairs.

# ### Google Cloud Storage
# 
# To learn more about the Google Cloud Storage service we will use the web console to create, explore, and destroy a Bucket.  The ability to quickly create, explore, and then discard resources in the web-console is a powerful tool to explore a service.  After an initial exploration with the web-console, programmatic access using scripts and programming languages should be used.
# 
# Unfortunately, the terminology used for object storage differs from one commercial cloud provider to another.  Google Cloud Storage uses the terms Bucket and Object.  Data is stored in Objects and Objects are stored in Buckets.  Objects (data) are stored as a key-value pair, which is similar to a Python dictionary but persistent.  Values are stored and retrieved using a unique key and the value can contain any information (more on this later).
# 
# We now take Drew through the process of creating a Google Cloud Storage bucket.

# ### Security
# 
# Everything in the cloud requires permission (authorization).  Let's first verify that we have the permissions to create a bucket.  A Bucket (a resource) is created within a project and inheres permissions from it.
# 
# We are interested in what permissions that *your* account has for *your* project. To do this navigate to the IAM page (**Navigation Menu -> IAM & Admin -> IAM -> Permissions -> View By: Principals**).  This shows the permissions for the project.
# 
# *Note: There is a powerful filter box to limit the permissions shown.*
# 
# You should see a row with your account shown in the Principal column.  Here you should see the "Owner" Role in the Role column.  A *role* is a collection of permissions managed by Google or someone else.  The **Owner** or the **Storage Admin** role for a project will *allow* *you* to create, access, and delete Buckets *in* the project.
# 
# There are three important pieces of information that work together to form the **IAM policy**. The permission (role), the identity (principal or member), and the resource (project).

# ### Allocate Google Cloud Storage
# 
# Now that we have verified the permissions we can now create a bucket. Buckets are where objects are stored and have a globally unique name.
# 
# To create a bucket we do the following:
#   * Click **Navigation Menu** -> **Cloud Storage** (under Storage) -> **Browser** -> **+Create Bucket** (just under the blue bar) to open the *Create a bucket* page.
#   * In *Name your bucket*:
#      * For **Name**, enter a globally unique name for the bucket (example "essentials-test-myname-2021-01-01")
#      * Click **Continue**
#   * In *Choose where to store your data*:
#      * For *Location Type* select **Region** (cheapest and fastest)
#      * For *Location* leave the default or select your "home" region.  The region is the physical location where your data will reside.  Your "home" region should be close to your work and the region you use most often.
#      * Click **Continue**
#   * In *Choose a default storage class for your data*:
#      * Select **Standard** (default). The other options are for long-term storage.
#      * Click **Continue**
#   * In *Choose how to control access to objects*:
#      * Under *Prevent Public Access* check "**Enforce public access prevention on this bucket**".  This will try to prevent others from accessing your data. 
#      * Under *Access Control* Select **Uniform** (default).  *Uniform* permissions are on the entire Bucket.  *Fine-grained* permissions are on the objects.
#      * Select **Continue**
#   * Note the **monthly cost estimate** in the right side panel. This is only for reading, writing, and storing data and does not include networking, compute, and other charges that may occur by using the data.
#      * *Storage size* is the total amount of data stored.
#      * *Data Retrieval* is only used for for long-term, non *standard*, storage.
#      * *Operations* is the number of "operations" performed on an object, for example reading and writing an object.  Storing and accessing many objects require many operations.
#   * Finally, click **Create** to create the bucket (allocate the resource).
#    

# ### Follow the Storage Allocation
# 
# Just as with security, we will audit (follow) the bucket creation by examining at the project *activity*.
# 
# To view the project activity we do the following:
# 
#   * Navigate to the project **Dashboard** by clicking on "Google Cloud Platform" on the left side of the top blue bar.
#     * Select **Activity** tab just below the top blue bar.
#     * Look for the row with **Create Bucket** on the top of the table.  This shows that the bucket was created.
#     * Expand the detail by clicking the **down arrow** on the right side of the row.  You can see what identity created the bucket and the name.  The rest of the information details the initial settings that you configured when creating the bucket. The details are not really important at this time, just know they exist.
# 
# Note that the activity is on the project, not the account.
# 

# ### Enumerate the Buckets
# 
# Now lets find and examine the bucket.  To view a bucket we do the following:
# 
#   * Navigate to the Google Storage page by clicking **Navigation Menu** -> **Cloud Storage** (under Storage) -> **Browser**.  
#   * **Find** the bucket you just created.  You can use the filter to find a bucket if there are a lot of them.
#   * Click on the bucket name to open the **bucket details** (it will display as a hyperlink when you hover over the bucket name).
# 
# Navigate to the **dashboard** and you will now see at least **1 bucket** in the *resources* card under storage.

# ### Review what is Important
# 
# It is always important to review what is important to you.  It may be cost, or keeping the data secure. Later on we will show how to monitor overall costs.
# 
# For Drew, we will review that the bucket **public access** is *not public* by doing the following:
#   * Go to **Navigation Menu -> Cloud Storage -> Browser**
#   * Select the bucket of interest by **checking the box** next to the Bucket name.
#   * In the Right Side Bar (open if necessary) in the **Permissions** tab in the **Public Access** card you should see **Not Public**.  This means that public access prevention is turned on.
#   * You can also see the **permissions** for the bucket in the bottom of the bar.

# ### Delete the Storage - Exercise 
# 
# We will now complete the resource life-cycle by deleting the bucket we just created. Think about the process we did for creating the bucket and follow a similar one.  
# 
# Did you "Follow" the bucket by looking at the **activity** page?
# 
# Since we care about paying for resources we are not using we **review** by visiting the **dashboard** and reviewing that we no longer have any buckets, if this was our only bucket. 

# ### Discussion
# 
# * What does the words "Secure", "Allocate", "Follow", and "Enumerate" Spell?
# * Why do you think we use this framework?

# ### Resources in Google Cloud Platform - Optional
# 
# Even though we only covered the Google Cloud Storage service in this episode, this process can be used for other *resources* allocated in the cloud.  The term *resource* is used for the "things" that live in a Project, such as compute, storage, and networking and other services.  Resources have the following characteristics:
# 
#  * Resources are like "objects" and usually have their own product/service page in the navigation menu.  
#  * Resources have many properties (how it is configured), costs, permissions, and almost always belong to a Project.
#  * Resource creation permission is at the parent (Project).
#  * Resources live in a machine somewhere, and usually specify a location (Region and Zone).
#  * Resource creation has limits (Quota) that can be changed (up or down).
#  * Resources usually have multiple charges associated with it (even if they are `$0.00`).
#  * Resources have a beginning, middle, and an end.  Don't forget the end. Have a plan!

# 
# ### References
#   * API reference https://cloud.google.com/storage/docs/reference/libraries
#   * Permissions (IAM): https://cloud.google.com/storage/docs/access-control/iam-permissions

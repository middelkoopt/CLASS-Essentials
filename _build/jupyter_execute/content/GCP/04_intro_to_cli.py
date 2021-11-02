#!/usr/bin/env python
# coding: utf-8

# ## Introduction to the gcloud CLI
# 
# Learner Questions
#  * How do I use the Cloud CLI?
#  * How do I use `gcloud`?
# 
# Learning Objectives
#  * Find and use the "Cloud Shell" in the web console.
#  * Use basic cloud CLI commands (`gcloud` and `gsutil`).
#  * Verify basic settings.
#  * Use environment variables for configuration.
#  * Understand the importance of using variables for configuration.
#  * Recognize the value of reproducibility and automation.
#  
# Resources
#  * `gcloud` documentation: https://cloud.google.com/sdk/gcloud
#  * `gsutil` documentation: https://cloud.google.com/storage/docs/gsutil
#  * Instructions to install `gcloud` and `gsutil` on your local machine: https://cloud.google.com/sdk/docs/install

# ### Cloud Automation
# 
# Now that Drew can create a bucket in the web console they wish to learn how to use tools to automate the process. Drew noticed that the web console could be used to upload and share objects but wishes to learn the command line so that they can automate the and document the process (it is much easier to document commands then describing and showing mouse clicks).
# 
# The cloud can be controlled using a Command Line Interface (CLI) or a programming language such as Python.  Collectively these tools interact with the cloud over a Application Programming Interface (API) and this capability forms the basis of the cloud, the ability to control infrastructure programmatically.
# 
# Just as with navigating the web console it is important to know the **who**, **what**, and **where** of CLI access to reduce the possibility of access mistakes.  We will first verify the tools are installed and configured correctly.  Next we get the Account being used (who) and the Project ID of the active project (where) using the `gcloud` command.  We will then use the `gcloud` and `gsutil` commands to list some public Buckets (what).
# 
# The `gcloud` command is used to control most aspects of GCP and the `gsutil` command is used to control Google Cloud Storage Buckets.  To access the manual pages for a command just add `--help` to the end of the command or run `gcloud help` for more information.
# 
# When running CLI commands you may get a dialog box to authorize the command.  You should "Authorize" the request to allow the Cloud Shell to access the Project using your (Google) Account.
# 

# ### Open a Cloud Shell
# 
# The Cloud Shell is an easy way to access Comand Line Interface (CLI) commands in a web browser.  Under the hood Cloud Shell is Debian running in a container with 5GB of no-charge persistent storage with most of the Google uti and a lot of other useful tools (git, docker, jq, Docker, etc.) installed by default.
# 
# To use the Cloud Shell:
#   * Open up a Cloud Shell by clicking on the **Activate Cloud Shell** icon in the right side of the top blue bar. If a "Authorize Cloud Shell" dialog appears click "Authorize" to allow the Cloud Shell to access the project.
#   * Click the **Maximize** icon on the right side of the Cloud Shell bar. You can find the correct icon by hovering over the icons to see their names.
#   * If a shell is associated with a project it will show it in the tab and in **yellow text** in round parenthesis in the shell prompt.  **Verify the Project ID**.
#   * To open up a shell with a specific project click the "down arrow" icon next to the plus(+) to open a new tab with a specific project.  Selecting the plus (+) will usually open up a shell with the default project.
#   * Note: You can open the Cloud Shell in a new tab by clicking on icon **Open in a New Window** on the far right of the Cloud Shell bar.
# 
# 
# #### Opening Cloud Shell in a Tab - Optional
# 
#  * Click the **Open in a New Window** icon on the far left of the "Cloud Shell" tab on the bottom to open up in a separate tab.  Hover the mouse over the icons to see their name/function.  **Note:** you may need to allow popups or enable popups for this website depending on the browser you use.  You can also pull up the tab to increase the shell screen size.
#  * Click the **"Close editor"** button (the pencil icon in the top right of the window).
# 
# #### Advanced call-out
# You can access the cloud shell from your laptop via `gcloud cloud-shell ssh` if you have the [Google Cloud SDK installed](https://cloud.google.com/sdk/docs/install).  Installing the Google Cloud SDK will also allow you to run `gcloud` and `gsutil` commands directly from your laptop, workstation, or cluster. *Pro-tip, you cannot use a service account to access the cloud shell.*

# ### Verify the Configuration (Who, What, Where)

# First, let's verify that the Account being used for access (who) is what we expect.

# In[1]:


gcloud config get-value account


# Next, show verify the active project (where).

# In[2]:


gcloud config get-value project


# Now we will use `gcloud` to list a well known public bucket (what).  

# In[3]:


gcloud alpha storage ls gs://gcp-public-data-landsat


# *Advanced Callout: The `alpha` (and `beta`) command allows us to access commands that have not been released for production and care should be taken when using these in a production environment.  At this time this is not the recommended way to access storage buckets, but it does help verify that everything is working correctly.*

# Finally, we will verify that the separate and preferred `gsutil` command is installed and working by listing the same well known public bucket.  

# In[4]:


gsutil ls gs://gcp-public-data-landsat


# ### Environment Variables
# 
# When using the CLI you quickly notice that you have to enter many of the details, such as the Project ID, many times (Drew is also Dyslexic, which makes it even harder for them).  Not only is this tedious, it also makes moving to another project or using another bucket difficult making reusability and collaboration painful.  We will demonstrate the use environment variables to address this issue.  Most cloud environments and tools rely heavily on this technique.
# 
# *To make the point even clearer, we use environment variables in the Cloud Essentials notebooks instead of hard coding them, which makes it easy for anyone to run, use, and edit and thus collaborate and contribute to them!*
# 
# We now demonstrate the basic use environment variables. As a reminder, environment variables are used to store configuration information that can be easily passed between programs and programming languages.

# In[1]:


TEST=1


# In[3]:


echo $TEST


# Although we do not always need to, we should always enclose shell variables in double quotes and enclose the variable name in curly braces (funny things may happen otherwise).  In most cases it is easier to do this every time than try to figure out when it is possible to use the short form.  We only use the short form (`$TEST`) when it is used frequently and known to always work, in our case it is `$PROJECT` and `$BUCKET`.  When in doubt, use the explicit form.
# 
# There are a number of environment variables already set that contain useful information, for example:

# In[7]:


echo "${USER}"


# In[8]:


echo "${HOSTNAME}"


# We can also use the output of commands to set values.

# In[9]:


date


# In[10]:


echo "Date: $(date)"


# Now lets combine all this to set the `PROJECT` environment variable to the default project so we do not need to use the actual value in future commands.

# In[11]:


gcloud config get-value project


# In[12]:


PROJECT="$(gcloud config get-value project)"


# In[13]:


echo $PROJECT


# Note the "Your active configuration is: ..." line is a "warning" and not actually part of the output of the program.

# Now use the `PROJECT` envrionment variable to get more information about the active project.

# In[14]:


gcloud projects describe $PROJECT


# Note the extraneous message about the active configuration produced by the `gcloud config get-value project` command. A slightly different way to access the data can be used to remove the extraneous message by using the following command:

# In[15]:


gcloud config list


# We can now use the `--format='value()'` option to get specific values.  The following command returns the project number without the extraneous message.

# In[16]:


gcloud config list --format='value(core.project)'


# Note where the `core` part comes in the output of the `gcloud config list` command.

# In[17]:


PROJECT="$(gcloud config list --format='value(core.project)')"
echo $PROJECT


# We will use this form from now on.  Since we know the Project ID only contains numbers, letters, and dashes with no spaces there is no need to use quotes.

# ### Exercise
#  * What command shows the project number? (hint: we used it already)
#  * What is the name of this variable? (hint: it is case sensitive)
#  * What command shows *just* the Project Number (hint: use `--format`)
#  * Set the `PROJECT_NUMBER` environment variable with the correct value. (hint: be careful with punctuation (single and double quotes) and matching brackets and punctuation)

# ### Advanced Call-Out: Formating Output.
# 
# The following example shows how to output the configuration as `JSON`.  The command `jq` can also be used to parse the JSON data.

# In[4]:


gcloud config list --format=json |jq


# In[5]:


gcloud config list --format=json |jq -r .core.project


# In[ ]:





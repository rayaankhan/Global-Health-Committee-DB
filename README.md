## CS4.301 : Data and Applications  
## PROJECT PHASE 4

# Global Health Committee 
# Database Designed to Manage the Operations in GHC 


* Prerequisites: https://blog.rajnath.dev/mysql/ to install mysql in WSL.
* Main code is to change the password back of mysql:
*
```
  ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```
* When you will be running my sql by the below code password is the one you have set on your mysql and that password is the one that will be used when you will run GHC.py and the username is root.

```
mysql -u root -p
```

* Copy and paste entire GHC.sql in your mysql.

```
python3 GHC.py
```

## 1. Queries
### • Selection
#### i. Retrieve complete data regarding all the diseases
#### ii. Finding the entire data about the world’s health
#### stats
#### iii. Finding all the offices along with their data
### • Aggregate
#### i. Maximum duration of a health policy/program
#### ii. Sum of all the deaths caused by all diseases
#### iii. Sum of all local organizations of all branches
### • Search
#### i. List of all the countries whose name starts with
#### ‘Ans’
#### ii. Number of all representatives with name ending
#### with ‘an’
#### iii. List of all diseases having ‘ler’ between their name
### • Projection
#### i. List of all Bio-Medical researches with status of
#### completion >= 90%
#### ii. List of all the branches in a particular country with
#### more than 30 local organizations
#### iii. List of all Disease IDs with more than 0.6 mortality
#### rate
### 2. Analysis
#### i. R0 value of the disease with maximum number of recoveries
#### ii. Mortality rate of the country with minimum number of
#### doctors/nurses
### 3. Modification
#### • Insertion
#### i. Adding any new policy being deployed by some country
#### ii. Adding any new members who wants to join GHC
#### iii. Inserting any new disease being found
#### iv. Adding new branches and infrastructures formed.
#### • Update
#### i. Change in representative of any country
#### ii. Change in location of any branch
#### iii. Change in status of completion of any Bio-Medical research
#### iv. Updating the percentage of vaccination status of a disease
#### • Deletion
#### i. Deleting any policy after its expiry
#### ii. Removing any country who wants to leave GHC group

---
#### *Video demo included*
---

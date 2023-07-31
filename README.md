# CS4.301: Data and Applications - PROJECT PHASE 4

## Global Health Committee Database - Managing Operations in GHC

**Prerequisites:** Follow the instructions in [this blog post](https://blog.rajnath.dev/mysql/) to install MySQL in WSL (Windows Subsystem for Linux).

**Main Code:** To change the MySQL password back, use the following command:
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

**MySQL Setup:** Run MySQL with the following command (replace 'password' with your MySQL password):
```
mysql -u root -p
```

**Database Import:** Copy and paste the entire content of `GHC.sql` into your MySQL.

**GHC.py Execution:** Run GHC.py using Python3:
```
python3 GHC.py
```

## 1. Queries
### • Selection
1. Retrieve complete data regarding all diseases.
2. Find the entire data about the world’s health stats.
3. Find all the offices along with their data.

### • Aggregate
1. Find the maximum duration of a health policy/program.
2. Calculate the sum of all deaths caused by all diseases.
3. Sum up all local organizations of all branches.

### • Search
1. List all the countries whose names start with 'Ans'.
2. Count the number of all representatives with names ending with 'an'.
3. List all diseases having 'ler' between their names.

### • Projection
1. List all Bio-Medical researches with a completion status >= 90%.
2. List all branches in a particular country with more than 30 local organizations.
3. List all Disease IDs with a mortality rate greater than 0.6.

## 2. Analysis
1. Find the R0 value of the disease with the maximum number of recoveries.
2. Calculate the mortality rate of the country with the minimum number of doctors/nurses.

## 3. Modification
### • Insertion
1. Add any new policy being deployed by some country.
2. Add any new members who want to join GHC.
3. Insert any new disease being found.
4. Add new branches and infrastructures formed.

### • Update
1. Change the representative of any country.
2. Change the location of any branch.
3. Change the status of completion of any Bio-Medical research.
4. Update the percentage of vaccination status of a disease.

### • Deletion
1. Delete any policy after its expiry.
2. Remove any country that wants to leave the GHC group.

---

**Video Demo Included**

---

Output in .md format

Note: The above information is provided for the Global Health Committee's database and the operations it supports. Ensure you follow the prerequisites and execute the given code responsibly.

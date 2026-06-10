# Northwind Database



1. What does a value in this column represent? What values might you see here?
2. Is this column a part of the primary key to this table?
3. &#x20;Is this column a part of a foreign key that points to a record in another table?
4. &#x20;Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?
5. &#x20;Do you believe this column is appropriately named for Data Analysis purposes?
6. &#x20;If not, what might be a more appropriate name?
7. &#x20;What might be the data type and format for this column in a Power BI Model?
8. Can you think of any calculations where this column data might be used?





#### Categories Table



###### Category ID:

Column: Category ID



Represents: The ID number for each category in the table.

Example Values: 1

Primary Key: ***Yes*** / No

Foreign Key: ***Yes*** / No

Related Table: Products

Include in Power BI: ***Yes*** / No

Reason: It tells what the table is exactly. What you can look for in the table.

Good Name: ***Yes*** / No

Better Name: None

Data Type: Whole Numbers

Calculations: The type of calculations where this column might be used is when joining two tables to get information on one particular category.







###### CategoryName:

Column: CategoryName



Represents: The values in this column represent the names of each category.

Example Values: Beverages

Primary Key: Yes / ***No***

Foreign Key: Yes / ***No***

Related Table: None

Include in Power BI: ***Yes*** / No

Reason: It is part of the descriptive information of the categories.

Good Name: Yes / ***No***

Better Name: Category

Data Type: Text

Calculations: Knowing which category has the highest revenue or in demand.







###### Description:



1. This gives the types of objects in each category. The types of values that will be there are text-based values.

Column: Description



Represents: The types of objects in each category.

Example Values: Soft drinks, teas, beers, and ales

Primary Key: Yes / ***No***

Foreign Key: Yes / ***No***

Related Table: None

Include in Power BI: Yes / ***No***

Reason: Having the CategoryName column would be more important, and no need for the descriptions

Good Name: ***Yes*** / No

Better Name: Specifics

Data Type: Text

Calculations: If you would like to know which is in demand the most in the Beverage category.





###### Picture:

Column: Picture



Represents: This primarily should give a picture of the category. A visualization. Though in the database it isn't shown and instead is replaced with the word "BLOB".

Example Values: Blob

Primary Key: Yes / ***No***

Foreign Key: Yes / ***No***

Related Table: None

Include in Power BI: Yes / ***No***

Reason: I don't see a reason for why it should be added into the analysis

Good Name: Yes / ***No***

Better Name: NullPicture

Data Type: Text

Calculations: None





### Customers Table:

&#x20;

###### CustomerID:

Column: customers



Represents: The customer ID number which connects to the customer name.

Example Values: ALFKI

Primary Key: ***Yes*** / No

Foreign Key: ***Yes*** / No

Related Table: orders

Include in Power BI: ***Yes*** / No

Reason: Each customer ID is unique. Even if customers have the same name, their ID is different.

Good Name: ***Yes*** / No

Better Name: Customer ID

Data Type: Text

Calculations: For when you want to compare customers.

##### 

###### CompanyName:

Column: CompanyName



Represents: The name of each company

Example Values: Alfreds Futterkiste

Primary Key: Yes / ***No***

Foreign Key: ***Yes*** / No

Related Table: shippers and suppliers

Include in Power BI: ***Yes*** / No

Reason: Having this column would help with knowing the companies each result is coming from or comparing companies.

Good Name: ***Yes*** / No

Better Name: Company Name

Data Type: Text

Calculations: If you want to compare certain companies.





###### ContactName:

Column: ContactName



Represents: The name of the person to contact for that company

Example Values: Maria Anders

Primary Key: Yes / ***No***

Foreign Key: Yes / No

Related Table: suppliers

Include in Power BI: Yes / ***No***

Reason: I don't see the reason for adding this into our report; only the company itself matters.

Good Name: ***Yes*** / No

Better Name: None

Data Type: Text

Calculations: Filtering





###### ContactTitle:

Column: ContactTitle



Represents: The position of the person you're contacting

Example Values: Sales Representative

Primary Key: Yes / ***No***

Foreign Key: Yes / No

Related Table: suppliers

Include in Power BI: Yes / ***No***

Reason: Without the contact name, I don't see why this is needed.

Good Name: ***Yes*** / No

Better Name: None

Data Type: Text

Calculations: If you want to compare the number of people in a certain position





###### Address:

Column: Address



Represents: The address of each company

Example Values: Obere Str. 57

Primary Key: Yes / ***No***

Foreign Key: ***Yes*** / No

Related Table: Address

Include in Power BI: Yes / ***No***

Reason: I don't see why the address of a company would be relevant to the analysis report except if trying to figure out why orders aren't being delivered.

Good Name: Yes / ***No***

Better Name: Company Address

Data Type: Text

Calculations: None



###### City:

Column: City



Represents: The city the company is in.

Example Values: Berlin

Primary Key: Yes / ***No***

Foreign Key: ***Yes*** / No

Related Table: employees and suppliers

Include in Power BI: ***Yes*** / No

Reason: Helps know the location of the company in that region

Good Name: ***Yes*** / No

Better Name: None

Data Type: Text

Calculations: Filtering the cities



###### Region:

Column: Region

Represents: The region the company is in. A NULL value.

Example Values: NULL

Primary Key: Yes / ***No***

Foreign Key: Yes / No

Related Table: employees

Include in Power BI: Yes / ***No***

Reason: The values are NULL/UNKNOWN

Good Name: ***Yes*** / No

Data Type: Text

Calculations: Filtering



###### PostalCode:

Column: PostalCode



Represents: The Postal code for the company

Example Values: 12209

Primary Key: Yes / ***No***

Foreign Key: Yes / No

Related Table: employees and suppliers

Include in Power BI: Yes / ***No***

Reason: I don't see any need for it

Good Name: ***Yes*** / No

Better Name: None

Data Type: Whole numbers

Calculations: None



###### Country:

Column: Country



Represents: The country the company belongs to

Example Values: Germany

Primary Key: Yes / ***No***

Foreign Key: ***Yes*** / No

Related Table: suppliers

Include in Power BI: ***Yes*** / No

Reason: Helps to know where in the region

Good Name: ***Yes*** / No

Data Type: Text

Calculations: Filtering or comparing countries



###### Phone:

Column: Phone



Represents: The number of the company

Example Values: 030-0074321

Primary Key: Yes / ***No***

Foreign Key: ***Yes*** / No

Related Table: shippers and suppliers

Include in Power BI: Yes / ***No***

Reason: Isn't relevant to the analysis

Good Name: ***Yes*** / No

Data Type: Whole Number

Calculations: None



###### Fax:

Column: Fax



Represents: Gives the fax number for each company

Example Values: 030-0076545

Primary Key: Yes / ***No***

Foreign Key: Yes / No

Related Table: suppliers

Include in Power BI: Yes / ***No***

Reason: Not relevant

Good Name: ***Yes*** / No

Data Type: Whole Numbers

Calculations: None





### Employees Table:



##### EmployeeID:

Column: EmployeeID



Represents: Each employee is given a number ID to identify them

Example Values: 1

Primary Key: ***Yes*** / No

Foreign Key: ***Yes*** / No

Related Table: employeeterritories and orders

Include in Power BI: ***Yes*** / No

Reason: Each employee is unique; this helps to identify them in case they may have the same first or last name

Good Name: ***Yes*** / No

Better Name: None

Data Type: Whole Number

Calculations: Finding out which employee has the most orders





##### LastName:

Column: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



Represents: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Example Values: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

Primary Key: Yes / No

Foreign Key: Yes / No

Related Table: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Include in Power BI: Yes / No

Reason: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Good Name: Yes / No

Better Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Data Type: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Calculations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

##### 

##### FirstName:

Column: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



Represents: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Example Values: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

Primary Key: Yes / No

Foreign Key: Yes / No

Related Table: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Include in Power BI: Yes / No

Reason: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Good Name: Yes / No

Better Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Data Type: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Calculations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

##### 

##### Title:

Column: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



Represents: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Example Values: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

Primary Key: Yes / No

Foreign Key: Yes / No

Related Table: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Include in Power BI: Yes / No

Reason: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Good Name: Yes / No

Better Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Data Type: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Calculations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

##### 

##### TitleOfCourtesy:

Column: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



Represents: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Example Values: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

Primary Key: Yes / No

Foreign Key: Yes / No

Related Table: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Include in Power BI: Yes / No

Reason: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Good Name: Yes / No

Better Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Data Type: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Calculations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



##### BirthDate:

##### 

##### 

##### HireDate:

##### 

##### 

##### Address:

##### 

##### 

##### City:

##### 

##### 

##### Region:

##### 

##### 

##### PostalCode:

##### 

##### 

##### Country:

##### 

##### 

##### HomePhone:

##### 

##### 

##### Extension:

##### 

##### 

##### Photo:

##### 

##### 

##### Notes:

##### 

##### 

##### ReportsTo:

##### 

##### 

##### PhotoPath:

##### 

##### 

##### Salary:


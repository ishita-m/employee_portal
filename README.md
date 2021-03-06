# employee_portal

The employee portal is a Django based web application that performs basic CRUD operations on employee database.

end points:

home page: shows all employee details in alphabetical order with a "search employee" functionality at the top. It also has the functionality to order Employees based on their joining date and last date. We can also access employee details by selecting employee name from the list and update/delete employee from the same list using dedicated buttons.

/enroll/employee/ : allows to add details of a new employee, ID is autogenerated. All details are validated and invalid data is not saved at the database.

/employee/<id>/ : used to retrieve employee details of any employee using thier ID
  
/update_employee_details/<id> : used to update employee details. ID can't be updated and updated details are validated before adding them to database
  
/admin : admin page where we could make changes in the database and handle access permissions

Features:
1. Enroll an employee
2. Delete an employee
3. Update an employee
4. Order employee details list by name, joining date and last date
5.Search for an employee in database

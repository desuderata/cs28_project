# Usage Guide

Please read this guide **thoroughly** for the application to work as intended. If you have any questions regarding the usage of the application, please [contact us](README.md#authors-and-contact).

##### Table of Contents
[General Features](#general-features)  
[User Hierarchy](#user-hierarchy)  
[Upload](#upload)  
[Course Grades](#course-grades)  
[Manage and Export CSV](#manage-and-export-csv)  
[Graphs](#graphs)


## General Features

### Search

The search bar allows users to search for a student by first name, last name, matriculation number, academic plan or graduation year. The search results will show the student in card form and will directly link to the [course grade](#course-grades) page or the [manage](#manage-and-export-csv) page with the appropriate filters for the student in the case of the latter (academic plan and graduation year with matriculation number in the table search)

### Sidebar
The sidebar allows users to quickly navigate between pages. The menu icon [&#8801;] expands the sidebar to view the page names for each icon. When expanded the icon will change to the cross icon [&#x2715;] which collapses the sidebar for more
space to work with.

### Footer Links
Quick links in the footer lets the user navigate between pages. It is functionally similar to the sidebar. When it is used by a user without the admin or staff status, a mailto link allows the user to contact the system administrator for elevated permissions.

### Password Reset
The password reset link is available at the login screen. Simply click on the Forgot Password link and enter a valid email. A mail will be sent to the registered email with a link to reset the password.

### Logo
The logo is specially created for the School of Chemistry database. Clicking on it leads the user back to the home page.


## User Hierarchy

### Admin
As part of the setup process, an admin (superuser) account should have been created. An admin user is able to manage all other users (by adding or removing permissions for each of the hierarchy groups) in addition to data stored in the database.

### Staff
By default, a staff is able to access the admin page albeit not being able to access anything else. An admin should assign permissions to the user as required.

### User
A user in the User group is not able to edit anything on the webpage, upload grades and will not be able to access the admin site. They will still be able to view data and generate graphs.

## Upload
Data could be uploaded to the database through their corresponding upload pages. Files could be uploaded by dragging and dropping into the dropzone or clicking on the dropzone to browse files. Only files with the extension of `.csv` will be accepted. Multiple files could be uploaded at once.

### Academic Plans

<img src="./cs28_project/static/pics/upload_plan.png"
     alt="upload_plan.png"
     width="512">  

Academics Plans could be uploaded through the Upload Academic Plan page.

**The CSV format is as follows:**  

Name: The name could be anything followed by the graduation year with the extension of `.csv` (Eg. `My Academic Plan 19-20.csv`)

File contents:  
| Academic Plan Code | Internal Course Code | MyCampus Description    | Course 1 | Weight 1 | Course 2 | Weight 2 | ... | Course 40 | Weight 40 |
|--------------------|----------------------|-------------------------|----------|----------|----------|----------|-----|-----------|-----------|
| F100-2208          | CHEM-4H              | Chemistry, BSc          | foo      | 0.5      | bar      | 0.5      | ... |           |           |
| F101-2207          | CHEM-5M              | Chemistry with WP, Msci | bar      | 1        |          |          | ... |           |           |

### Student Roster

Student Roster could be uploaded through the Upload Student Roster page.

**The CSV format is as follows:**  

Name: The name could be anything with the extension of `.csv` (Eg. `F100-2208-Graduating Year.csv`) as the upload system does not rely on any data from the name.

File contents:  
| StudentID | Name                         | Acad Plan | Grad Year |
|-----------|------------------------------|-----------|-----------|
| 3159976   | Ahab,Captain                 | F100-2208 | 19-20     |
| 2790987   | Blake,Flake                  | F100-2208 | 19-20     |
| 2110101   | Boingo,Oingo                 | F100-2208 | 18-19     |
| 3428888   | Chowder,Clam Stinky Gooey    | F100-2208 | 16-17     |
| 4512345   | Dinky,Fluffy Puffy           | F100-2208 | 19-20     |
| 1239876   | Gobsmacker,Flatulent Poopsie | F100-2208 | 18-19     |
| 2016655   | McBoatface,Boaty             | F100-2208 | 19-20     |

### Course Grades

Grades Roster could be uploaded through the Upload Course Grades page.

**The CSV format is as follows:**

Name: The name could be anything followed by the course code followed by the year (with underscores) with the extension of `.csv` (Eg. `Grade roster CHEM_4014_2019.csv`).

File contents:  
| EMPLID  | Name                         | Grade |
|---------|------------------------------|-------|
| 3159976 | Ahab,Captain                 | A3    |
| 2790987 | Blake,Flake                  | B1    |
| 2110101 | Boingo,Oingo                 | C1    |
| 3428888 | Chowder,Clam Stinky Gooey    | D3    |
| 4512345 | Dinky,Fluffy Puffy           | E2    |
| 1239876 | Gobsmacker,Flatulent Poopsie | A1    |
| 2016655 | McBoatface,Boaty             | G1    |


## Course Grades
This is where student's course grades are filtered and displayed, this page has viewing permission only, there is no editing from the user. 
Using the search bar that is located above "Alphanumeric Grade", allows the user to search for different information and will display only the data that matches the user's input, for example this could be a course code, studentId or a grade. 
The arrows next to the table column headers allow for users to display the requested data either in asending or desending order and the column icon to the far right of the screen above "22pt Grade" allows the user to toggle what data feilds are shown. 

## Manage and Export CSV

<img src="./cs28_project/static/pics/manage.png"
     alt="manage.png"
     width="512">  

This is where student's grades are managed and exported. Student's award will be calculated before being displayed on the table.

### Load Table
<img src="./cs28_project/static/pics/get_students.png"
     alt="get_students.png"
     width="256">  

The table could be loaded by selecting the required Academic Plan and Graduation Year. By clicking on "`Get Students`", the student's award will be calculated before being loaded to the table.

### Edit A Grade
<img src="./cs28_project/static/pics/award_row.png"
     alt="award_row.png"
     width="512">  

Grades could be edited by clicking on the [&#43;] icon which expands a subtable with all the grades for the student.

<img src="./cs28_project/static/pics/subtable.png"
     alt="subtable.png"
     width="512">

You could select a grade from the **Alphanumeric Grade** section to edit (Editable fields are in blue). A dropdown list will show up with all the possible grades. After a grade has been selected, [&#10003;] to keep changes or [&#x2715;] to discard changes (as with all editable fields). Notes could be added if required.

### Edit An Award

<img src="./cs28_project/static/pics/award_row.png"
     alt="award_row.png"
     width="512">  

Student's award could be edited by clicking on the award from the **Award** row. If the new award is not the same as the original award, the row will show up as green to signify that the award has been overridden. Notes could be added if required.


### The Table
The table comes with features such as row highlighting, note-taking,  sortability, searchablilty and keyboard shortcuts.
#### **Row Highlighting**

Rows are highlighted according to its corresponding issues. There is an order of priority as to which color the row will be highlighted should there be more than one issue. This is because we are not able to use all colors. The current order of importance is:

*Degree Overridden* &#8594; *Incomplete Course Assessment* &#8594; *Discretionary*

***Green***  
Degree Overridden  
> When a degree has been overridden (the new award is no longer the same as the original award), the row shows up as green. This will hide issues such as *Incomplete Course Assessments* or *Discretionary*.

Grades Overridden (Sub-table only)  
> When a grade has been overridden (the new grade is no longer the same as the original grade), the row shows up as green. This is only visible in the sub-table.

***Red***  
Incomplete Course Assessment  
> When a student is missing grades for their academic plan, or the grades are a special code (CW, CR or MV), the row shows up as red. This will hide issues such as grades being in the discretionary zone. The row highlighting will go away once all the issues have been fixed.

Course Grade Adjusted  
> When a student's grade has been overridden and there are still special codes, the row will show up as red. It will stay red if the student decides not to retake the course. This will hide *Discretionary* issues.

***Yellow***  
Discretionary  
> When a student's final gpa is in the discretionary range, the row will show up as yellow.

#### **Notes**

Notes could be added to both the grades and the award row to document changes and justification. The notes section is not searchable as with all editable fields. Simply click on the red *Add Notes* or an existing note to add a note or make changes.

#### **Sortability**

All columns are sortable. The first click sorts the column in ascending order, the second in descending order and the third to reset the sort.

#### **Searchability**

Almost all fields are searchable with the exception of editable fields.

#### **Filtering**
All columns are filterable. More than one column could be filtered at once. Column searches will be filtered by keyword matches.

#### **Export**
The data in the table could be exported in the following formats. The exported data will have the academic plan as the file name and will contain all the columns that are currently visible. To export in MyCampus friendly format, click on the Toggle MyCampus Layout to quickly toggle between edit-friendly and MyCampus layout.

***JSON***: Currently of no use but may be helpful in future projects to transfer data between databases (requested to be kept)  
***CSV***: The required format for MyCampus  
***TXT***: Exported in plain text separated by commas. The content is the same as *CSV*  
***MS-Excel***: Microsoft Excel format with the file extension of `.xls`. There will be a warning about file extension incompatibility which should not matter as the file format is `xlshtml` and the extension is `.xls`.  
***PDF***: Exports the table in pdf format. Notes that are too long will be truncated.

#### **Keyboard Shortcuts**

Keyboard shortcuts allow users to increase productivity by navigating the page smoothly. 

- ***Left* and *Right* arrow keys**: Move between pages
- **"`s`" key**: sets the caret (the "`|`" cursor in text boxes) to the search box for the table
- **"`r`" key**: refreshes the table manually (should it be opted over automatic refresh with every change)
- **"`t`" key**: toggles between the row view and the *Card View*


#### **Toolbar**
<img src="./cs28_project/static/pics/toolbar.png"
     alt="toolbar.png"
     width="256">  

From left to right:  
- ***Searchbar***: Searches the table for the query entered with the exception of editable fields
- ***Refresh***: Manual refresh of the table should it be opted over automatic refresh with every change
- ***Card View***: Shows all the rows in *Card View*  
<img src="./cs28_project/static/pics/card_view.png"
     alt="card_view.png"
     width="512">
- ***Full Screen***: Shows the table exclusively in full screen  
<img src="./cs28_project/static/pics/fullscreen.png"
     alt="fullscreen.png"
     width="512">
- ***Toggle Columns***: Choose columns to show or to hide from the table. The search bar inside the dropdown allows users to quickly search for the desired column  
<img src="./cs28_project/static/pics/toggle_columns.png"
     alt="toggle_columns.png"
     width="128">
- ***Export***: Export the table in the desired format.  
<img src="./cs28_project/static/pics/export.png"
     alt="export.png"
     width="128">

## Graphs
<img src="./cs28_project/static/pics/graphs.png"
     alt="graphs.png"
     width="512">  

Users could create visualizations from data from the database with the option of a GPA bar chart or a 22 point scale bar chart.

### Selecting Graph type

<img src="./cs28_project/static/pics/graph_type.png"
     alt="graph_type.png"
     width="256">  

The graph type could be selected by expanding the Graph Type dropdown. Clicking on Set Graph Type will remove all datasets that are currently on the chart (changing from GPA to 22 Point with data still on the chart).

### Setting Graph Labels

<img src="./cs28_project/static/pics/graph_label.png"
     alt="graph_label.png"
     width="256">  

Graph labels (title and axes names) could be changed by entering the desired names and clicking on Set Graph Labels. If nothing has been entered, the default will be used.

### Adding a Dataset

<img src="./cs28_project/static/pics/dataset.png"
     alt="dataset.png"
     width="256">  

A new dataset could be added by selecting all three fields then clicking on Add. To remove the last dataset added, click on Remove. Reset will remove all datasets that are currently on the chart.

### Chart
<img src="./cs28_project/static/pics/chart_value.png"
     alt="chart_value.png"
     width="256">  
By hovering over the bars, the exact value for each bar will pop up.

<img src="./cs28_project/static/pics/legend.png"
     alt="legend.png"
     width="256">  
Clicking on any dataset on the legend will hide the dataset from the chart.
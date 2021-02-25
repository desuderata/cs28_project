<p align="center">
    <a href="https://cs28.herokuapp.com/">
        <img class="logo"
             src="./cs28_project/static/icons/UoG_colour_edited.svg"
             alt="uog_logo"
             height="64">
        <p>View on Heroku</p>
    </a>
</p>

# CS28 Project

A bespoke and flexible database for the School of Chemistry (SoC) tailored for the calculation of Degree Classification as part of the Team Project module.

The project aims to develop a flexible datable for the School of Chemistry to manage and publish degree classification for final year students all while minimizing the use of Microsoft Excel. The output should be in a MyCampus-friendly format

### Requirements

***Degree Calculation Specific***
- Store grades (as 22point and alphanumeric) for each course
- Different weight for each course in a degree programme
- Support degree calculation using data given with the appropriate calculations
- Other features cherry-picked from legacy software by 19-20 teams

***DB***
- Flexible
  - Good cause
  - different weightages
- Input and output meshes with MyCampus requirements
- Ability to add notes
- Secure
- Sortable and Searchable
- Degree classification as 22 point or alphanumeric
- Exportable as excel or csv
- Anonymize

Site currently up on heroku
> [https://cs28.herokuapp.com/](https://cs28.herokuapp.com/)

##### Table of Contents
[Prerequisites](#prerequisites)  
[Installation / Setup](#installation-setup)  
[Superuser Account](#superuser-account)  
[Usage](#usage)  
[Contributing](#contributing)  
[Licenses](#licenses)  
[Authors and Contact](#authors-and-contact)  
[Team Coach](#team-coach)  
[Acknowledgements](#acknowledgements)  



## Prerequisites

This web app is built on:
- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
- [Django 3.1.3](https://docs.djangoproject.com/en/3.1/releases/3.1.3/)
- [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
- [Jquery 3.5.1](https://jquery.com/download/)

## Installation / Setup

1. Create a virtual environment:

```bash
conda create -n cs28 python
conda activate cs28
```

2. Clone the repository:
```bash
git clone https://stgit.dcs.gla.ac.uk/tp3-2020-CS28/cs28-main.git
```

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages through the requirements.txt file:
```bash
pip install -r requirements.txt
```

4. Migrate database models:
```bash
cd cs28_project
python manage.py makemigrations cs28
python manage.py migrate
```

5. Run the server
```bash
python manage.py runserver
```

### Superuser Account

**To create a superuser account:**

```bash
python manage.py createsuperuser
```

You will be prompted to enter your username, email and password.

## Usage

### Features

**User Interface**
- Professional look that is consistent with other webpages from the University
- Sidebar with quick access icons

**Security**
- [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) protection

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Licenses

- Bootstrap table ([MIT](https://github.com/wenzhixin/bootstrap-table/blob/master/LICENSE))

- x-editable ([MIT](https://github.com/Talv/x-editable/blob/develop/LICENSE-MIT))

- jsPDF ([MIT](https://github.com/MrRio/jsPDF/blob/master/LICENSE))

- js-xlsx ([Apache-2.0](https://github.com/protobi/js-xlsx/blob/beta/LICENSE))

- TableExport ([Apache-2.0](https://github.com/clarketm/TableExport/blob/master/LICENSE.txt))

- Malihu custom scrollbar ([MIT](https://github.com/malihu/malihu-custom-scrollbar-plugin/blob/master/LICENSE.txt))

## Authors and Contact
### Scrum Master
Alana Grant (Meeting Chair) - [2390384G@student.gla.ac.uk](2390384G@student.gla.ac.uk)

### Product Owner
Yee Hou Teoh (Note Taker) - [2471020T@student.gla.ac.uk](2471020T@student.gla.ac.uk)

### Development
Ekaterina Terzieva (Lead Demonstrator) - [2403606T@student.gla.ac.uk](2403606T@student.gla.ac.uk)

Hieu Nguyen (Checker) - [2471707N@student.gla.ac.uk](2471707N@student.gla.ac.uk)

Kien Welch (Checker) - [2371692W@student.gla.ac.uk](2371692W@student.gla.ac.uk)
## Team Coach

Robert Pringle - [2304777P@student.gla.ac.uk](2304777P@student.gla.ac.uk)

## Acknowledgements
[Make a README](https://www.makeareadme.com/)

[Font Awesome](https://fontawesome.com/)

[Bootstrap Table](https://bootstrap-table.com/)

[x-editable (bootstrap 4 support)](https://github.com/Talv/x-editable/tree/develop)

[jsPDF](https://github.com/MrRio/jsPDF)

[js-xlsx](https://www.npmjs.com/package/js-xlsx)

[TableExport](https://tableexport.v5.travismclarke.com/)

[Malihu custom scrollbar](https://github.com/malihu/malihu-custom-scrollbar-plugin)

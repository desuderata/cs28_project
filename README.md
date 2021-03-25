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
See [INSTALL.md](INSTALL.md) for full instructions on installation

## Usage

See [USAGE.md](USAGE.md) for detailed usage guide.

### Features

**User Interface**
- Professional look that is consistent with other webpages from the University
- Sidebar with quick access icons
- Search with quick links to student in [course grades](USAGE.md#course-grades) or [manage](USAGE.md#manage-and-export-csv)
- Row highlighting in tables

**Security**  
- Safe from [OWASP Top 10 vulnerabilities](https://owasp.org/www-project-top-ten/)  
  > *Ensure that site is appropriately [set up](INSTALL.md#live-server) for deployment*
- [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) protection

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Licenses

- CS28 Project ([MIT](LICENSE))

- Bootstrap table ([MIT](https://github.com/wenzhixin/bootstrap-table/blob/master/LICENSE))

- x-editable ([MIT](https://github.com/Talv/x-editable/blob/develop/LICENSE-MIT))

- jsPDF ([MIT](https://github.com/MrRio/jsPDF/blob/master/LICENSE))

- js-xlsx ([Apache-2.0](https://github.com/protobi/js-xlsx/blob/beta/LICENSE))

- TableExport ([Apache-2.0](https://github.com/clarketm/TableExport/blob/master/LICENSE.txt))

- Malihu custom scrollbar ([MIT](https://github.com/malihu/malihu-custom-scrollbar-plugin/blob/master/LICENSE.txt))

- Chart.js ([MIT](https://github.com/chartjs/Chart.js/blob/master/LICENSE.md))

- Dropzone.js ([MIT](https://github.com/dropzone/dropzone/blob/main/LICENSE))

- Django Axes ([MIT](https://github.com/jazzband/django-axes/blob/master/LICENSE))

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

[Chart.js](https://www.chartjs.org/)

[Dropzone.js](https://www.dropzonejs.com/)

[Django Axes](https://pypi.org/project/django-axes/)

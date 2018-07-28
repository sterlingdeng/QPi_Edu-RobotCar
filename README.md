# Robot Controller Website

The files enclosed provide the functionality to deploy a webserver using Flask which hosts a website that can execute python functions on the raspberry pi. This provides a more graphical user interface when controlling the car. This is built for QPi Education.

## Prerequisites

The flask python package is required to run the flask web server.

### Installing

If flask is not installed on the raspberry pi, first connect to the internet.

Go to the terminal and type

`pip install flask`

The package installer will automatically install the files necessary to run the flask server.

## Understanding the Files

This section will review each of the files and their purpose.

    .
    ├── static                    # --See Below
    |     ├── app.js              # Contains js scripts to control the buttons
    |     ├── jquery-3.3.1-min.js # jQuery framework needed to control the buttons
    |     └── style.css           # Styling Sheet
    |
    ├── templates                 # --See Below
    |     └── index.html          # HTML file for the webpage
    |
    ├── application.py            # Contains the flask webserver logic
    ├── carfunctions.py           # Library to control the car
    ├── cleanup.py                # Library to stop the car
    └── README.md                 # This file

Do not rename the `static` folder. The Flask webserver will refer all scripts or 'static' dependencies referenced in the header of the HTML in the `static` folder. This includes javascript files, images, styling sheets, frameworks, etc.

Do not rename the `templates` folder. The Flask webserver will load HTML pages found only in the `templates` directory.

## Deployment

Starting the webserver can be done through the terminal. First open the terminal and navigate to the directory with the webserver material.

This can be done by typing

`./Desktop/Exercises/RobotCarWebsite`

Next, type

`FLASK_APP=application.py flask run`

in the terminal window. Wait a few seconds and a website url will pop up.

Open up the web browser and navigate to the website.

Voila.. You can now control the car with the buttons on the website. Remember to check if the batteries and everything is hooked up.
# QPi_Edu-RobotCar

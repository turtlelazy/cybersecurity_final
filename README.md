# TEAM: Graceful Fish

## Roster:
* Ishraq Mahid
* Grace Chen

## Project Description:
We are creating a capture the flag type of activity where users will be required to use SQL injection and other already-taught tools. For the presentation, we will be reteaching how SQL works and useful keywords to reiterate students' understanding of SQL Injection. The activity will require students to deploy a web app locally (through a virtual machine or other personal device) and connect to it .

1/2/2022
* Grace Chen (at home): Successfully set up DigitalOcean machine for the challenge. Still need to configure it so that it doesn't allow remote root logins. Worked on the google slides for the presentation.

1/3/2022
* Grace Chen (in class): Continued working on google slides for presentation.
* Grace Chen (at home): Disabled remote root logins for DigitalOcean machine. Helped with walkthrough and slides.

## Haikus:
A graceful fish swims. <br>
Oh so very fast it is! <br>
With grace comes freedom.

Suddenly, currents <br>
The graceful fish can't keep up :( <br>
Will its grace prevail?

## Documents/Presentation + Any Other Resources
Link to planning document: https://docs.google.com/document/d/1Ha1vOAJRb35Ei32Rkq19hncYhVfalp1soGSrM-R59Ik/edit?usp=sharing <br>
Link to slides: https://docs.google.com/presentation/d/1lHERkTjasriZZWj2upCdgcLkcUiVW0KcoBhyXDWVAno/edit?usp=sharing <br>
Link to walkthrough: https://docs.google.com/document/d/16cP2Rw6tQDJ3z8khmlpGxjji0FtcgEO2X0o-9zVF5VI/edit?usp=sharing <br>


## Launch Codes:

Prerequisites:
    Python 3 is installed and necessary environment variables are setup properly.
    If using Windows, utilizing WSL and willing to go threw a few extra steps that may be necessary if certain packages aren't preinstalled
Clone repo:
    <br>
    In the directory you want to have the code in, type into a terminal
    <br>
    ```
    $ git clone https://github.com/turtlelazy/cybersecurity_final
    ```

Create a virtual environment (unless you already have one):
    <br>
    A virtual environment can be created using the following line in a terminal
    <br>
    ```
    $ python3 -m venv ~/path/to/virtual/environment/directory
    ```
    <br>
    The virtual environment can then be activated by being in the right directory, then typing the following line in a terminal
    <br>
    ```
    $ source (name of virtual environment directory)/bin/activate
    ```
    <br>
    To then install the required packages, navigate to this repository, and enter in the following with the virtual environment activated:
    ```
    pip install -r requirements.txt
    ```

Launching the website app:
    <br>
    cd into app
    <br>
    activate the virtual environment
    <br>
    run ```python3 __init__.py```
    <br>
    Open the link given from the the terminal.

## Daily Log:
12/14/2021
* Ishraq Mahid (in class): Worked on formatting repo + website app
* Ishraq Mahid (at home): Worked on website app + haiku + VM setup
* Grace Chen (in class): Worked on researching SQLmap and going through a tutorial for it + taking notes on how it works
* Grace Chen (at home): Successfully set up a virtual machine for use. Opened port on the machine and connected from another device and it works but not sure how to apply it to our project yet. Port seems to only be open when target machine is listening on that port (ex. with netcat).

12/15/2021
* Grace Chen (in class): Clarified assignment regarding how to use virtual machine for the project. Researched bit more about SQLmap and discussed with partner about plans for the steps we need to take. 
* Grace Chen (at home): researched more about sqlmap
* Ishraq Mahid (in class): worked more on the website and talked about vm's. almost done with website shouuld finish at home
* Ishraq Mahid (at home): finished the website and researched some sql injection tactics

12/16/2021
* Grace Chen (in class): Set up slides template, discussed plan for the activity and presentation, talked about utilization of virtual box and possibly using digital ocean
* Ishraq Mahid (in class): Set up slides template, discussed plan for the activity and presentation, talked about utilization of virtual box and possibly using digital ocean

12/17/2021
* Grace Chen (in class): Worked on the google slides and clarified plan for steps to capture the flag
* Ishraq Mahid (in class and at home): did research on sql injection methods

12/20/2021
* Grace Chen (in class): Worked on code to create a list of hashed passwords to be used with hashcat later on.
* Ishraq Mahid (in class and at home): Worked on thinking out ways to implement the different injection methods and allowing students to experiment with such methods

12/21/2021
* Ishraq Mahid (in class): Brainstormed some more obstacles and ideas reguarding password cracking and the flags needed to be captured.
* Grace Chen (in class): Finished code to create random list of 100 hashed passwords and uploaded data file with them.

12/22/2021
* Grace Chen (in class): Finished code to create a list of salted and hashed passwords and uploaded 

12/28/2021
* Grace Chen (at home): Set up Digitalocean account and successfully deployed a test machine and logged into it.

12/29/2021
* Ishraq Mahid (at home): search bar setup -> need to put in info and create challeneges for individual admin accounts

1/2/2022
* Ishraq Mahid (at home): finalizing project + finishing touches

1/3/2022
* Ishraq Mahid (at home): lessons + something i forgot to do before
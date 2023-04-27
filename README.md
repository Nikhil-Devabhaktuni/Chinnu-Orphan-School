# Chinnu-Orphan-School

Welcome to Chinnu Orphan School, a project dedicated to providing education and support to orphaned children around the world.

Project Overview:
Chinnu Orphan School aims to provide education and support to orphaned children who lack access to proper education. Our project focuses on creating an online learning platform that provides free educational resources, mentorship, and community support to orphaned children globally.

Web Application Features:

    Admin can log in and approve students and teachers and make changes to classes and student attendance.
    Teachers can log in and take attendance for students.
    Students can log in through the website, mark attendance, and listen to online classes.

Library:

    A custom library was created, named IpLibrary, which helps send emails to the admin whenever someone logs into the website, notifying the admin with IP address and location. The library was copied to the virtual environment to make it available for easy importing.

Cloud-based Services:

    The project was deployed using cloud services.
    A cloud pipeline was used for continuous integration, delivery, and deployment of the application.
    Stages were included in the cloud pipeline, such as code build and code deploy, to ensure proper building and deployment of the application.
    A build spec YAML file was used for the build stage.
    EBS was used to host the web application.

How to Run the Project:

    Install Python 3.7.6 (Don't forget to tick "Add to Path" while installing Python).
    Open Terminal and execute the following commands:
        python -m pip install -r requirements.txt
        Download the project zip folder and extract it.
    Move to the project folder in Terminal and run the following commands:
        py manage.py makemigrations
        py manage.py migrate
        py manage.py runserver
    Enter the following URL in your browser installed on your PC: http://127.0.0.1:8000/

Thank you for your interest in Chinnu Orphan School. Together, we can make a difference in the lives of orphaned children around the world.

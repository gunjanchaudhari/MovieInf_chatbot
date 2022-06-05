# MovieInf_chatbot

Steps to run the code,
1. install: conda install flask-CORS
2. pip install flask
3. pip instal rivescript
4. in folder Cinemainf, run command : "docker build -t my_service:latest ."
5. run command: "docker run --name Docker_cinema -p 8085:5000 -t my_service:latest __init__.py"
6. in folder timslot, run command : "docker build -t my_service:latest ."
7. run command: "docker run --name Docker_booker -p 8080:5000 -t my_service:latest __init__.py" 
8. Go to bot/chatbot/demo and run command : python __init__.py

This will start the environment by running both the dockers, containing booking and cinema information services, which are called in the ‘bot’ folder connected to the ‘wit.ai’
To connect to a chatbot navigate to the folder ‘jake’ and Run: python -m http.server
Using a browser, Go to http://localhost:8000


# File structure 
1. bot/chatbot/demo/v1/api/booker.py: Recieves input from the chatbot
2. bot/chatbot/demo/v1/api/cinema.py: Handles requests to CinemaInf container after dockerized
3. bot/chatbot/demo/v1/api/timeslot.py: Handles requests to timeslot container after dockerized
4. bot/chatbot/demo/v1/api/wit.py: Holds the conversation logic of the chatbot 
5. CinemaInf/cinema/demo/v2/api: Extracts information from the database through various functions
6. timeslot/booking/demo/v1/api/timeslot_booking.py: populates the database as well as extracts data from the database

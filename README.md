# sentiment-gui
GitHub Repository for the Sentiment Client GUI Service

# Building the container image
Within the sentiment-gui directory first run:
	docker build --tag docker-gui .
Then run:
	docker run -d --name gui -p 5000:80 docker-gui
	
# Using the container image
With the container running, navigate to localhost/5000 to access the gui, functionality is available only when the containers for the database and analyzer are running
In order to properly connect to the backend service, line 65 will need to be changed from building a connection string to localhost/5001 to {YOUR_IP}/5001 (e.g. 1.1.1.1/5001)
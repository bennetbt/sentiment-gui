# sentiment-gui
GitHub Repository for the Sentiment Client GUI Service

# Building the container image
Within the sentiment-gui directory first run:
	docker build --tag docker-gui .
Then run:
	docker run -d --name gui -p 5000:80 docker-gui
	
# Using the container image
With the container running, navigate to localhost/5000 to access the gui, functionality is available only when the containers for the database and analyzer are running
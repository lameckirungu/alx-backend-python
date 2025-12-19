FROM python:3.11-slim
# Set the working directory for the appliation
WORKDIR /usr/src/app

# copy the requirennets file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy the rest of the application code.
COPY . .

# Expose the port the container listens on, commands to run the server on startup
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
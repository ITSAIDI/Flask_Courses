FROM python:3.9-alpine

WORKDIR /flask_app

COPY requirements.txt .

RUN pip install -r requirements.txt

# Set up a new user named "user" with user ID 1000
RUN useradd user

# Switch to the "user" user
USER user

# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

# Set the working directory to the user's home directory
WORKDIR $HOME/app

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

EXPOSE 8888

CMD ["python", "main.py"]
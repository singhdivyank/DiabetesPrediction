# Python base image
FROM python:3.9

# change working directory
WORKDIR /code

# add requirements file to image
COPY ./requirements.txt /code/requirements.txt

# install python libraries
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# add Python code
COPY ./app /code/app

# add classifier.pkl file
COPY ./app/classifier.pkl /code/app/classifier.pkl

# expose application portal
EXPOSE 80

# specify default commands
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
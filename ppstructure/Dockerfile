# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y wget libgl1-mesa-glx libglib2.0-0

# Upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

# Download models
WORKDIR /app
RUN mkdir -p inference && cd inference && \
    wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/table/en_ppocr_mobile_v2.0_table_det_infer.tar && \
    tar xf en_ppocr_mobile_v2.0_table_det_infer.tar && \
    wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/table/en_ppocr_mobile_v2.0_table_rec_infer.tar && \
    tar xf en_ppocr_mobile_v2.0_table_rec_infer.tar && \
    wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/table/en_ppocr_mobile_v2.0_table_structure_infer.tar && \
    tar xf en_ppocr_mobile_v2.0_table_structure_infer.tar && \
    cd ..

# Set the working directory back to /app
WORKDIR /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

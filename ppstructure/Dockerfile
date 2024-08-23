# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ppstructure /app/ppstructure
COPY requirements.txt /app/requirements.txt

# Install system dependencies
RUN apt-get update && apt-get install -y wget

# Upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download models
WORKDIR /app/ppstructure
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

# Run paddleocr when the container launches
CMD ["python", "ppstructure/app.py"]
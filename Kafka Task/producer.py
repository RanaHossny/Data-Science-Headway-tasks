import os
import time
import io
from PIL import Image
from confluent_kafka import Producer
from threading import Thread

# Define the base path
base_path = r"D:\Users\rana.hosny\Downloads\kafka_demo\kafka_demo\Task\Kafka_Task_Pics"

kafka_topic = "image_topic"
kafka_bootstrap_servers = "localhost:9092"  

# Flag to allow image compression
compress_images = True  

producer = Producer({
    'bootstrap.servers': kafka_bootstrap_servers})

def compress_image(image_path):
    """
    Compress the image to reduce its size for transmission.
    Returns the compressed image as a byte stream.
    """
    try:

        with Image.open(image_path) as img:
            img = img.convert("RGB")  
            byte_stream = io.BytesIO()
            img.save(byte_stream, format="JPEG", optimize=True, quality=50)  
            byte_stream.seek(0)
            return byte_stream.read()
    except Exception as e:
        print(f"Error compressing image {image_path}: {e}")
        return None

def send_to_kafka(producer, topic, key, value):
    """
    Send data to a Kafka topic asynchronously.
    """
    print(f"Sending image '{key}' to Kafka topic: {topic}")  
    producer.produce(topic, key=key.encode("utf-8"), value=value)
    producer.flush()

def process_image(image_path):
    """
    Process each image, optionally compress it, and send it to Kafka.
    """
    global total_images, total_size
    image_data = None
    if compress_images:
        image_data = compress_image(image_path)
    else:
        with open(image_path, "rb") as img_file:
            image_data = img_file.read()

    if image_data:
        send_to_kafka(producer, kafka_topic, key=os.path.basename(image_path), value=image_data)
        total_images += 1
        total_size += len(image_data)

def measure_performance(base_path):
    """
    Read images from the directory, optionally compress them, and send to Kafka.
    Report throughput and latency metrics.
    """
    global total_images, total_size

    total_images = 0
    total_size = 0
    start_time = time.time()

    threads = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith(".jpg"):
                image_path = os.path.join(root, file)
                thread = Thread(target=process_image, args=(image_path,))
                threads.append(thread)
                thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Ensure all messages are flushed
    producer.flush()
    end_time = time.time()

    # Throughput and average latency calculation
    total_time = end_time - start_time
    throughput = total_images / total_time if total_time > 0 else 0
    average_latency = total_time / total_images if total_images > 0 else 0

    print("\nPerformance Metrics:")
    print(f"Total Images Sent: {total_images}")
    print(f"Total Data Sent: {total_size / 1024:.2f} KB")
    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Throughput: {throughput:.2f} images/second")
    print(f"Average Latency: {average_latency:.4f} seconds")

# Execute the function
measure_performance(base_path)

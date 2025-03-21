import os
import csv
from kafka import KafkaConsumer
import re


# Configuration
kafka_topic = "image_topic"
kafka_bootstrap_servers = "localhost:9092" 
received_image_folder = r"D:\Users\rana.hosny\Downloads\kafka_demo\kafka_demo\task\received_images"
csv_file_path = os.path.join(received_image_folder, "image_data.csv")

os.makedirs(received_image_folder, exist_ok=True)

def save_image(file_name, image_data):
    """
    Save the image data to a file.
    """
    try:
        image_path = os.path.join(received_image_folder, file_name)
        with open(image_path, "wb") as img_file:
            img_file.write(image_data)
        return image_path
    except Exception as e:
        print(f"Error saving image {file_name}: {e}")
        return None

def append_to_csv(file_name, image_path):
    """
    Append image information (Arabic or English) to the CSV file using UTF-8 encoding.
    """
    try:
        file_exists = os.path.isfile(csv_file_path)
        with open(csv_file_path, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(["Image Name", "Image Path"])
            file_name = re.sub(r'\.[^.]*$', '', file_name)
            writer.writerow([file_name, image_path])
        print(f"Image information appended to CSV: {file_name}, {image_path}")
    except Exception as e:
        print(f"Error writing to CSV: {e}")


def consume_images():
    """
    Consume images from Kafka, save them, and log metadata to a CSV.
    """
    # Initialize Kafka consumer
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers=kafka_bootstrap_servers,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="image-consumer-group"
    )
    print(f"Consumer is listening on topic: {kafka_topic}")

    for message in consumer:
        try:
            # Extract image data
            file_name = message.key.decode("utf-8") if message.key else "unknown.jpg"
            image_data = message.value

            # Save the image
            saved_path = save_image(file_name, image_data)
            if saved_path:
                # Append metadata to CSV
                append_to_csv(file_name, saved_path)

        except Exception as e:
            print(f"Error processing message: {e}")

# Execute the consumer
consume_images()

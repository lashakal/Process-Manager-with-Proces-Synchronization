import threading
import time
import random
import logger_config

# Size of the buffer
BUFFER_SIZE = 5

# Shared buffer
buffer = []

# Semaphores
mutex = threading.Semaphore(1)  # Mutex for buffer access
empty = threading.Semaphore(BUFFER_SIZE)  # Semaphore for empty slots
data = threading.Semaphore(0)  # Semaphore for filled slots

# Producer function
def producer():
    for i in range(10):#while True:
        item = random.randint(1, 100)  # Generate a random item
        empty.acquire()  # Wait for an empty slot
        mutex.acquire()  # Get exclusive access to the buffer
        buffer.append(item)  # Add item to the buffer
        print(f"Produced {item}. Buffer: {buffer}")
        logger_config.logger.info(f"Produced {item}. Buffer: {buffer}")
        mutex.release()  # Release the mutex
        data.release()  # Notify that a slot is filled
        time.sleep(random.uniform(0.1, 0.5))  # Simulate work

# Consumer function
def consumer():
    for i in range(10):#while True:
        data.acquire()  # Wait for a filled slot
        mutex.acquire()  # Get exclusive access to the buffer
        item = buffer.pop(0)  # Remove and consume the first item
        print(f"Consumed {item}. Buffer: {buffer}")
        logger_config.logger.info(f"Consumed {item}. Buffer: {buffer}")
        mutex.release()  # Release the mutex
        empty.release()  # Notify that a slot is empty
        time.sleep(random.uniform(0.1, 0.5))  # Simulate work

def producer_consumer_problem():
    # Create producer and consumer threads
    producers = [threading.Thread(target=producer) for _ in range(2)]
    consumers = [threading.Thread(target=consumer) for _ in range(2)]

    print("Producer-consumer problem with 2 producers and 2 consumers.\n")
    print("We have a buffer of fixed size. A producer can produce an item and can place in the buffer.\n"
          "A consumer can pick items and can consume them. We need to ensure that when a producer is \n"
          "placing an item in the buffer, then at the same time consumer should not consume any item.\n")

    # Start the threads
    for producer_thread in producers:
        producer_thread.start()
        logger_config.logger.info("Producer thread has started.")
    for consumer_thread in consumers:
        consumer_thread.start()
        logger_config.logger.info("Consumer thread has started.")

    # Allow the threads to run for some time
    time.sleep(5)

    # Terminate the threads
    for producer_thread in producers:
        producer_thread.join()
        logger_config.logger.info("Producer thread has been terminated.")
    for consumer_thread in consumers:
        consumer_thread.join()
        logger_config.logger.info("Producer thread has been terminated.")

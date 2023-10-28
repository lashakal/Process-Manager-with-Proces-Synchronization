import multiprocessing
import logger_config

# DEMONSTRATION OF MUTEX AND SEMAPHORE

# Create a shared variable and a mutex for controlling access
shared_value = multiprocessing.Value('i', 0)  # 'i' for integer type
mutex_for_demo = multiprocessing.Lock()  # Mutex for controlling access to shared_value
semaphore_for_demo = multiprocessing.Semaphore(1)

# Function to increment shared_value using a mutex
def increment_with_mutex(shared_value, mutex_for_demo):
    mutex_for_demo.acquire()
    print("Mutex lock acquired.")
    logger_config.logger.info("Mutex lock acquired.")
    shared_value.value += 1
    print(f"Shared value incremented with mutex: {shared_value.value}")
    logger_config.logger.info(f"Shared value incremented with mutex: {shared_value.value}")
    mutex_for_demo.release()
    print("Mutex lock released.")
    logger_config.logger.info("Mutex lock released.")

# Function to decrement shared_value using a mutex
def decrement_with_mutex(shared_value, mutex_for_demo):
    mutex_for_demo.acquire()
    print("Mutex lock acquired.")
    logger_config.logger.info("Mutex lock acquired.")
    shared_value.value -= 1
    print(f"Shared value decremented with mutex: {shared_value.value}")
    logger_config.logger.info(f"Shared value decremented with mutex: {shared_value.value}")
    mutex_for_demo.release()
    print("Mutex lock released.")
    logger_config.logger.info("Mutex lock released.")

# Function to increment shared_value using a semaphore
def increment_with_semaphore(shared_value, semaphore_for_demo):
    semaphore_for_demo.acquire()
    print("Semaphore acquired.")
    logger_config.logger.info("Semaphore acquired.")
    shared_value.value += 1
    print(f"Shared value incremented with semaphore: {shared_value.value}")
    logger_config.logger.info(f"Shared value incremented with semaphore: {shared_value.value}")
    semaphore_for_demo.release()
    print("Semaphore released.")
    logger_config.logger.info("Semaphore released.")

# Function to decrement shared_value using a semaphore
def decrement_with_semaphore(shared_value, semaphore_for_demo):
    semaphore_for_demo.acquire()
    print("Semaphore acquired.")
    logger_config.logger.info("Semaphore acquired.")
    shared_value.value -= 1
    print(f"Shared value decremented with semaphore: {shared_value.value}")
    logger_config.logger.info(f"Shared value decremented with semaphore: {shared_value.value}")
    semaphore_for_demo.release()
    print("Semaphore released.")
    logger_config.logger.info("Semaphore released.")

def process_synchronization_demo():
    print(f"Initial value of shared value: {shared_value.value}\n")

    while True:
        user_choice = input("\nChoose an option:\n"
                            "1. Increment with mutex\n"
                            "2. Decrement with mutex\n"
                            "3. Increment with semaphore\n"
                            "4. Decrement with semaphore\n"
                            "5. Quit\n")

        if user_choice == '1':
            increment_process_mutex = multiprocessing.Process(target=increment_with_mutex, args=(shared_value, mutex_for_demo))
            increment_process_mutex.start()
            increment_process_mutex.join()
        elif user_choice == '2':
            decrement_process_mutex = multiprocessing.Process(target=decrement_with_mutex, args=(shared_value, mutex_for_demo))
            decrement_process_mutex.start()
            decrement_process_mutex.join()
        elif user_choice == '3':
            increment_process_semaphore = multiprocessing.Process(target=increment_with_semaphore, args=(shared_value, semaphore_for_demo))
            increment_process_semaphore.start()
            increment_process_semaphore.join()
        elif user_choice == '4':
            decrement_process_semaphore = multiprocessing.Process(target=decrement_with_semaphore, args=(shared_value, semaphore_for_demo))
            decrement_process_semaphore.start()
            decrement_process_semaphore.join()
        else:
            break
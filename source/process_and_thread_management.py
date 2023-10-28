import os
import psutil
import threading
import time
import logger_config

# PROCESS CREATION - USING FORK()

def create_process():
    # Fork a child process
    child_pid = os.fork()

    # if this is a child process
    if child_pid == 0:
        message = f"Child process created successfully. PID: {child_pid}, Parent PID: {os.getpid()}"
        print(message)
        logger_config.logger.info(message)
    # wait for the child process, if this is a parent process
    else:
        os.waitpid(child_pid, 0)

# ----------------------------------------------------------------------------------------------------------------------
# PROCESS MANAGEMENT

# list, monitor, and terminate processes
def list_processes():
    for process in psutil.process_iter(['pid', 'name', 'ppid', 'status']):
        process_info = process.info
        pid = process_info['pid']
        name = process_info['name']
        ppid = process_info['ppid']
        state = process_info['status']
        print(f"PID: {pid}, Name: {name}, Parent PID: {ppid}, State: {state}")
    logger_config.logger.info("Processes have been listed.")

# function to terminate a process
def terminate_process(target_pid):
    target_pid = int(target_pid)
    try:
        process = psutil.Process(target_pid)
        process.terminate()
        print(f"Process with PID {target_pid} has been terminated.")
        logger_config.logger.info(f"Process with PID {target_pid} has been terminated.")
    except psutil.NoSuchProcess:
        print(f"Process with PID {target_pid} does not exist.")
        logger_config.logger.warning(f"Process termination - process with PID {target_pid} does not exist.")
    except psutil.AccessDenied:
        print(f"You don't have permission to terminate the process with PID {target_pid}.")
        logger_config.logger.warning(f"Process termination - Access Denied.")

# ----------------------------------------------------------------------------------------------------------------------
# THREADING

threads = []

# funtion to create a thread
def create_thread():
    thread = threading.Thread(target = worker)
    threads.append(thread)
    thread.start()
    logger_config.logger.info(f"Thread {thread.name} created.")
    return thread

# function to terminate a thread
def terminate_thread(thread):
    thread.join()
    threads.remove(thread)
    print(f"Thread {thread.name} terminated successfuly.")
    logger_config.logger.info(f"Thread {thread.name} terminated successfuly.")

# function to simulate some work for threads created by the user
def worker():
    print(f"Thread {threading.current_thread().name} is working...")
    logger_config.logger.info(f"Thread {threading.current_thread().name} is working...")
    print(f"Thread {threading.current_thread().name} is done.")
    logger_config.logger.info(f"Thread {threading.current_thread().name} is done.")

# function to synchronize threads using a semaphore
def synchronize_threads():
    # Define a semaphore with an initial value of 1
    semaphore = threading.Semaphore(1)

    print("Synchronization of 5 threads using a Semaphore:\n")

    # Function to simulate a task that requires a semaphore
    def task(thread_id):
        print(f"\nThread {thread_id} is waiting for the semaphore.")
        logger_config.logger.info(f"Thread {thread_id} is waiting for the semaphore.")
        # Acquire the semaphore
        semaphore.acquire()
        print(f"\nThread {thread_id} has acquired the semaphore.")
        logger_config.logger.info(f"Thread {thread_id} has acquired the semaphore.")
        # Simulate some work
        time.sleep(2)
        # Release the semaphore
        semaphore.release()
        print(f"\nThread {thread_id} has released the semaphore.")
        logger_config.logger.info(f"Thread {thread_id} has released the semaphore.")

    # Create and start multiple threads
    synch_threads = []
    for i in range(5):
        thread = threading.Thread(target=task, args=(i,))
        synch_threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in synch_threads:
        thread.join()

    print("All threads have finished.")
    logger_config.logger.info("Thread synchronization - all threads have finished.")

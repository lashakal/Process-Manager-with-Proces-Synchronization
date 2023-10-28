import multiprocessing
import logger_config

# INTER-PROCESS COMMUNICATION (IPC) USING PIPE

def sender(pipe, message):
    pipe.send(message)
    print(f"Sender process sent a message: {message}\n")
    logger_config.logger.info(f"Sender process sent a message: {message}")
    pipe.close()

def receiver(pipe):
    if pipe.poll():
        message = pipe.recv()
        print(f"Receiver process received a message: {message}\n")
        logger_config.logger.info(f"Receiver process received a message: {message}")
        pipe.close()
    else:
        print("No message in the pipe.\n")
        logger_config.logger.warning("IPC Pipe - no message in the pipe.")

def IPC_pipe():
    parent_pipe, child_pipe = multiprocessing.Pipe()

    while True:
        user_choice = input("\nChoose an option:\n"
                            "1. Send a message\n"
                            "2. Receive a message\n"
                            "3. Quit\n")

        if user_choice == '1':
            message = input("Enter a message to send: ")
            sender_process = multiprocessing.Process(target=sender, args=(child_pipe, message))
            sender_process.start()
            sender_process.join()
        elif user_choice == '2':
            receiver_process = multiprocessing.Process(target=receiver, args=(parent_pipe,))
            receiver_process.start()
            receiver_process.join()
        else:
            break

# ----------------------------------------------------------------------------------------------------------------------
# INTER-PROCESS COMMUNICATION (IPC) USING SHARED MEMORY

# Function for the process that writes to shared memory
def writer(shared_array, index, value):
    shared_array[index] = value
    logger_config.logger.info(f"IPC - Written to shared memory: {value}")

# Function for the process that reads from shared memory
def reader(shared_array, index):
    value = shared_array[index]
    print(f"Read from shared memory: {value}")
    logger_config.logger.info(f"IPC - Read from shared memory: {value}")

def IPC_shared_memory():
    # Create a shared memory array to store integers
    shared_array = multiprocessing.Array('i', 5)  # 'i' stands for integer type, and 5 is the size of the array
    print("Shared memory is an array of size 5 storing integers.")

    while True:
        user_choice = input("\nChoose an option:\n"
                            "1. Write to the shared memory\n"
                            "2. Read from the shared memory\n"
                            "3. Quit\n")

        if user_choice == '1':
            index = int(input("Enter the index to write to: "))
            value = int(input("Enter the value to write: "))
            writer_process = multiprocessing.Process(target=writer, args=(shared_array, index, value))
            writer_process.start()
            writer_process.join()
        elif user_choice == '2':
            index = int(input("Enter the index to read from: "))
            reader_process = multiprocessing.Process(target=reader, args=(shared_array, index))
            reader_process.start()
            reader_process.join()
        else:
            break
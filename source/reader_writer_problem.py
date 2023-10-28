import threading
import time
import logger_config

# semaphores for reading and writing
read_semaphore = threading.Semaphore()
write_semaphore = threading.Semaphore()

# number of readers present
read_count = 0

def reader():
    global read_count

    for i in range(10):
        # wait on read semaphore
        read_semaphore.acquire()
        read_count += 1         # increase count for reader by 1

        if read_count == 1:     # that means that reader is present
            write_semaphore.acquire() # wait on write semaphore

        read_semaphore.release()
        print(f"Reader {read_count} is reading.")
        logger_config.logger.info(f"Reader {read_count} is reading.")
        read_semaphore.acquire()
        read_count -= 1

        # if no reader present - allow writer to write the data
        if read_count == 0:
            write_semaphore.release()

        read_semaphore.release()
        time.sleep(3)

def writer():
    for i in range(10):
        write_semaphore.acquire()
        print("Writing data...")
        logger_config.logger.info("Writing data...")
        write_semaphore.release()
        time.sleep(3)

def reader_writer_problem():
    print("Reader-writer problem with 2 readers and 2 writers.\n")
    print("The reader-writer problem relates to an object such as a file that is \n"
          "shared between multiple processes. Some of these processes are readers \n"
          "i.e. they only want to read the data from the object and some of the \n"
          "processes are writers i.e. they want to write into the object.\n")

    t1 = threading.Thread(target=reader)
    t1.start()
    logger_config.logger.info("Reader-writer - thread 1 has started.")
    t2 = threading.Thread(target=writer)
    t2.start()
    logger_config.logger.info("Reader-writer - thread 2 has started.")
    t3 = threading.Thread(target=reader)
    t3.start()
    logger_config.logger.info("Reader-writer - thread 3 has started.")
    t4 = threading.Thread(target=writer)
    t4.start()
    logger_config.logger.info("Reader-writer - thread 4 has started.")

    # Allow the threads to run for some time
    time.sleep(5)

    t1.join()
    logger_config.logger.info("Reader-writer - thread 1 has ended.")
    t2.join()
    logger_config.logger.info("Reader-writer - thread 2 has ended.")
    t3.join()
    logger_config.logger.info("Reader-writer - thread 3 has ended.")
    t4.join()
    logger_config.logger.info("Reader-writer - thread 4 has ended.")
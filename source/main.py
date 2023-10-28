import process_and_thread_management
import IPC
import mutex_and_semaphore_demo
import producer_consumer_problem
import reader_writer_problem
import logger_config

# Command Line Interface
def CLI():
    while True:
        print("\nOptions:")
        print("1. Create a new process")
        print("2. List running processes")
        print("3. Terminate a process")
        print("4. Create a thread")
        print("5. Terminate a thread")
        print("6. Synchronize threads")
        print("7. Inter-Process Communication (IPC) using pipe")
        print("8. Inter-Process Communication (IPC) using shared memory")
        print("9. Process Synchronization - mutex and semaphore")
        print("10. Producer-consumer problem")
        print("11. Reader-writer problem")
        print("12. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            process_and_thread_management.create_process()

        elif choice == "2":
            process_and_thread_management.list_processes()

        elif choice == "3":
            inpt = input("Enter PID: ")
            process_and_thread_management.terminate_process(inpt)

        elif choice == "4":
            thread = process_and_thread_management.create_thread()
            print(f"Thread {thread.name} created.")

        elif choice == "5":
            if len(process_and_thread_management.threads) == 0:
                print("No threads to terminate.")
                logger_config.logger.warning("Thread termination - no threads to terminate.")
            else:
                print("Which Thread would you like to terminate?")
                for i in range(len(process_and_thread_management.threads)):
                    print(f"{i + 1}. {process_and_thread_management.threads[i].name}")
                thread_num = input("\nEnter your choice: ")
                process_and_thread_management.terminate_thread(process_and_thread_management.threads[int(thread_num) - 1])

        elif choice == "6":
            process_and_thread_management.synchronize_threads()

        elif choice == "7":
            IPC.IPC_pipe()

        elif choice == "8":
            IPC.IPC_shared_memory()

        elif choice == "9":
            mutex_and_semaphore_demo.process_synchronization_demo()

        elif choice == "10":
            producer_consumer_problem.producer_consumer_problem()

        elif choice == "11":
            reader_writer_problem.reader_writer_problem()

        elif choice == "12":
            logger_config.logger.info("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Run command-line interface
    CLI()
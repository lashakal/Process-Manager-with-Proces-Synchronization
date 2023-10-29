# **Advanced Process Manager with Process Synchronization**

This project implements a process manager with an emphasis on process synchronization. The process manager allows users to create, manage, synchronize, and interact with processes in a multi-threaded environment. It provides a command-line interface and uses system calls for process and thread control.


## **Functionalities of the Process Manager**

The process manager has the following functionalities:

1.	Process creation – the user can choose to create a new child process, in which case the program will call fork() system call.
2.	Process management – the user can tell the program to:\
  a.	List all running processes, displaying their process ID, process name, parent process ID, and state.\
  b.	Terminate a running process by entering its process ID.
3.	Threading – the user can tell the program to:\
  a.	Create a new thread.\
  b.	Terminate a newly created thread.\
  c.	Synchronize multiple threads - display a demonstration of thread synchronization.
4.	Inter-Process Communication (IPC) – the program implements two types of IPC:\
  a.	IPC via pipe – allowing users to see how two processes communicate with each other via pipe. The user can enter a message that will be sent by a sender process and received by a receiver process.\
  b.	IPC via shared memory – the program employs a shared array of size 5, and the user can make a process write to the shared memory, and a process read from the shared memory.
5.	Process Synchronization – the program provides demonstrations of:\
  a.	Mutex – the users can increment or decrement a shared value using a mutex.\
  b.	Semaphore – the users can increment or decrement a shared value using a semaphore.\
  c.	The use of synchronization mechanisms to solve the Producer-Consumer Problem.\
  d.	The use of synchronization mechanisms to solve the Reader-Writer Problem.
6.	Command-line interface (CLI) allows users to interact with the process manager and choose what to do using a clear and informative syntax and options.
7.	Logging and reporting – the process manager implements a logging mechanism and logs all significant events to the log file. To help the user track the execution of processes and threads, the program also displays every important detail to the user using CLI.


## **Running the Program**

All of the libraries used in the program are included in the Python standard library, except one – psutil. To install psutil, run the following command in the terminal: `pip install psutil`

To run the program, download the source file, which includes all of the source code of the project, including the log file, and run main.py by using the Python interpreter.


## **Functionality Discussion and Explanation**

### **1. Command-Line Interface**

The process manager uses a command-line interface to interact with the user. The user can choose from the following options:
  1. Create a new process
  2. List running processes
  3. Terminate a process
  4. Create a thread
  5. Terminate a thread
  6. Synchronize threads
  7. Inter-Process Communication (IPC) using pipe
  8. Inter-Process Communication (IPC) using shared memory
  9. Process synchronization – mutex and semaphore
  10. Producer-consumer problem
  11. Reader-writer problem
  12. Exit

The user can choose any of the options by entering the corresponding number of the choice. This is what the CLI looks like:

<img width="506" alt="Screenshot 2023-10-28 at 5 11 12 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/61bf7426-c49b-46a7-a061-0eb7fd8a9b75">

### **2. Process Creation**

If the user chooses the first option – to create a new process, the process creation method is called, which is in `process_and_thread_management.py` file, called `create_process()`. It uses `os.fork()` call to fork a child process, and if fork is successful the program displays the message saying that process creation was successful, along with the process’ PID, as well as its parent’s PID.

This is what the output looks like when the user chooses option #1:

<img width="506" alt="Screenshot 2023-10-28 at 5 10 03 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/2c7cc004-860c-40cb-82a2-037c4584e252">

### **3. List Running Processes**

If the user chooses to list running processes, the `list_processes()` method is called from `process_and_thread_management.py` file. The method uses psutil library to list information about all currently running processes, which includes their PID, name, parent PID, and state (e.g. running).

This is a snippet of what the output might look like – its details are going to vary across different devices at different times: 

<img width="536" alt="Screenshot 2023-10-28 at 5 18 08 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/fd071679-3e61-4df8-a730-41dfbc25da25">

### **4. Terminate a Process**

If the user wishes to terminate a process, they will first be asked to enter a PID of the target process (process about to be terminated). Depending on the input, either the program is going to terminate the process by calling `terminate_process()` function from `process_and_thread_management.py`, or in case of an error, it’s going to display that message as well.

If the process can be terminated, the program will do so by calling `terminate()` method from the psutil library. If there’s no such process with the PID entered, the program is going to display a message saying so, and if the access to terminate the process has been denied, the program will display that, as well.

Program’s output in the case of a successful termination:

<img width="491" alt="Screenshot 2023-10-28 at 5 23 06 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/65320634-79e6-444b-8210-dd90d1fa91ed">

Program’s output if the process with entered PID does not exist:

<img width="491" alt="Screenshot 2023-10-28 at 5 23 44 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/79c63a7f-cc1a-43c1-8af5-50a47ee998b4">

Program’s output if the access has been denied:

<img width="514" alt="Screenshot 2023-10-28 at 5 23 58 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/bbc6a560-ce7c-4916-8859-8fa7327154bb">

### **5. Thread Creation**

If the user chooses to create a thread, `create_thread()` method is called from `process_and_thread_management.py`. The method creates a thread using the threading library (`threading.Thread()`), gives it some function that simulates work, and starts the thread. The name of the thread is printed out to the console:

<img width="514" alt="Screenshot 2023-10-28 at 5 56 11 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/1882a690-fc1c-499d-88b7-5ee8b1bbee03">

### **6. Thread Termination**

If the user chooses to terminate a thread, first they have to choose which thread to terminate. All the threads created by the user beforehand will be listed, and the user will have to choose the corresponding number. After choosing the thread, the program calls `terminate_thread()` function from `process_and_thread_management.py`, which uses `join()` method to terminate the thread. This is what the output looks like if we have 4 threads:

<img width="514" alt="Screenshot 2023-10-28 at 5 58 50 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/71ba2927-9f64-414e-98eb-68114f7264bf">

### **7. Thread Synchronization**

If the user chooses the sixth option – synchronize threads, the process manager is going to display how multiple (in this case 5) threads can be synchronized using a semaphore. The program calls `synchronize_threads()` function from `process_and_thread_management.py`, which also employs methods from the threading library. First, we define a semaphore with the initial value of 1; then 5 threads are initialized, each given a task, and they complete the task by acquiring semaphore, doing the work, and releasing it one by one. After all threads are done, the semaphore is released. This is what the output looks like:

<img width="568" alt="Screenshot 2023-10-28 at 6 03 11 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/eb96e392-5423-4f16-8ada-7763aabd3a70">

### **8. Inter-Process Communication (IPC) Using Pipe**

If the user chooses to demonstrate inter-process communication using a pipe, the program calls `IPC_pipe()` function from `IPC.py`. The function employs two types of process – sender and receiver of a message – for demonstration purposes and creates those processes using the multiprocessing library. The pipe between them is also created using the same library by calling `multiprocessing.Pipe()`. 

The user is given 3 choices – to send a message, to receive a message, and to quit the IPC system. If the user wants to send a message, the program is going to take input of the user and assign it to the message variable, and the sender process is going to put the message in the pipe. If the user chooses to receive a message, the receiver process is going to get the oldest message from the pipe and display it to the console. The quit option returns to the main CLI.

This is what the interaction with the IPC pipe system looks like:

<img width="502" alt="Screenshot 2023-10-28 at 6 08 37 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/3a98af1e-2214-4918-a5d1-f13f2b71000b">

### **9. Inter-Process Communication (IPC) Using Shared Memory** 

If the user chooses to demonstrate inter-process communication using shared memory, `IPC_shared_memory()` method from `IPC.py` will be called. Similar to the previous method, this one also creates 2 processes, but in this case, one is a writer process, which writes to the shared memory, and the second one reads from the shared memory.

For simple demonstration purposes, shared memory in this case is an array of size 5 which can store integers. When the user chooses to write to the shared memory, a writer process is initialized, and the user is able to choose where to write the information, and what information to write (can choose the integer value). If the user chooses to read from the shared memory, they will be asked to enter the value of index they want to read from, and the program is going to initialize a reader process, which is going to read from the shared memory. This is what the interaction with this type of IPC system looks like:

<img width="502" alt="Screenshot 2023-10-28 at 6 13 13 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/6a3a1998-ce7a-42df-afdf-0dd05b02249f">

### **10. Process Synchronization - Demonstration of Mutex and Semaphore**

If the user chooses the ninth option, the program is going to demonstrate how mute and semaphore work by creating a shared value using `process_synchronization_demo()` function from `mutex_and_semaphore_demo.py`. The program lets the user choose to increment or decrement the shared value using a mutex, or increment or decrement the shared value using a semaphore.

Once the user chooses what to do, the program creates a process using the multiprocessing library and assigns tasks according to the user’s input.

This is what the output might look like when interacting with this demo:

<img width="502" alt="Screenshot 2023-10-28 at 6 17 23 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/6b290676-6001-4475-8527-03b18b53a95f">

### **11. Producer-Consumer Problem**

If the user chooses the 10th option, the program is going to call `producer_consumer_problem()` from `producer_consumer_problem.py`. This function demonstrates the producer-consumer problem with 2 producers and 2 consumers. We have a buffer of fixed size; a producer thread can produce an item and place it in the buffer, and a consumer can pick items from the buffer and consume them. The main goal is to ensure that when a producer is placing an item in the buffer, consumers should not consume any item at the same time.

To achieve that goal, we create a mutex for buffer access, a semaphore for empty slots, and a semaphore for filled slots. 

When a producer thread is tasked with producing an item, first it waits for an empty slot, and gets exclusive access to the buffer using the mutex. After that, it adds the produced item to the buffer, releases the mutex, and notifies that a slot is filled using the second semaphore. 

When a consumer thread is tasked with consuming an item, first it waits for a filled slot, then gets exclusive access to the buffer, consumes the first item in the buffer, releases the mutex, and notifies that a slot is empty using the first semaphore called empty. The program displays how the buffer changes on each iteration.

This is what the output looks like:

<img width="744" alt="Screenshot 2023-10-28 at 6 30 26 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/a4f35d85-c5e4-4243-821b-d63cb485037f">
<img width="744" alt="Screenshot 2023-10-28 at 6 30 35 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/7a6df6dc-fe1c-44ba-85da-9f2f41ad58bb">

### **12. Reader-Writer Problem**

If the user chooses the 11th option, the program calls `reader_writer_problem()` method from `reader_writer_problem.py`. This particular implementation of the problem involves 2 readers and 2 writers, and an object, which is shared between all four of the processes. Reader processes only want to read the data from the object and writer processes only want to write into the object. By using two semaphores, read_semaphore and write_semaphore, we ensure that the processes have exclusive access to the shared object. 

This is what the output looks like:

<img width="744" alt="Screenshot 2023-10-28 at 6 37 05 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/30cc9084-ab6c-4905-85a7-eda48ae07233">
<img width="744" alt="Screenshot 2023-10-28 at 6 37 15 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/83d037c4-546c-4cd5-90a1-d0aa57783dc9">

### **13. Logging**

In the project files, there is one called `logger_config.py`, which uses Python’s logging library to create a logger and log all significant events, warnings, and errors to the log file called `log_file.log`. The logger records the time of the event, the name of the logger, the level of the logger, and the message.

This is a snippet of what `log_file.log` could look like – it all depends on what the user’s choices are in the command-line interface:

<img width="853" alt="Screenshot 2023-10-28 at 6 07 47 PM" src="https://github.com/lashakal/Process-Manager-with-Proces-Synchronization/assets/111999712/0c33d952-e341-4d8e-8021-90a5dcccc082">


## **Discussion of the Results**

The project aimed to design and implement an advanced Process Manager with a strong emphasis on process synchronization. The main purpose was to create something that would allow users to interact with processes and threads and explore different functionalities of process synchronization in a multithreaded environment. 

By interacting with this program, the user can learn a lot about how things work – how to harness system calls to create, manage, and synchronize processes and threads effectively. Users can better understand the importance of managing system resources efficiently to minimize conflicts after their time with the project. The addition of a user-friendly command-line interface simplifies interactions with the process manager and greatly enhances its usability.

Also, the inclusion of logging and reporting features directly to the user enables us to effectively track the execution of processes and threads. This not only provides a comprehensive view of the system’s behavior but also can be very useful if debugging or error handling is needed.

Personally, the project expanded my technical skills in process and thread management. The user-friendly interface, comprehensive logging, and synchronization mechanisms make the process manager a valuable tool for learning more about multithreaded environments.


## **References**

1.	https://gyaanibuddy.com/assignments/assignment-detail/producer-consumerreader-writer-using-semaphore/
2.	https://docs.python.org/3/howto/logging.html
3.	https://docs.python.org/3/library/threading.html
4.	https://docs.python.org/3/library/multiprocessing.html
5.	https://www.datadoghq.com/blog/python-logging-best-practices/
6.	https://www.geeksforgeeks.org/python-os-fork-method/

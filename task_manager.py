import file_handler
import validation

def add_new_task():
    print("\n--- Add New Task ---")
    task_name = input("Kya kaam hai? (eg. Assignment): ")
    subject = input("Kaunsa subject?: ")
    
    print("Status: [1] Pending  [2] Done")
    status_choice = input("Status batao (1 or 2): ")
    
    if validation.check_status(status_choice) == False:
        print("Galat status! 1 ya 2 dabao.")
        return
        
    if status_choice == "1":
        status_text = "Pending"
    else:
        status_text = "Done"
        
    # Comma hata do taaki txt file kharab na ho
    task_name = task_name.replace(",", " ")
    subject = subject.replace(",", " ")
    
    # CSV format mein save karenge
    final_record = task_name + "," + subject + "," + status_text
    file_handler.save_task(final_record)
    print("Task save ho gaya!")

def show_all_tasks():
    lines = file_handler.get_all_tasks()
    
    if len(lines) == 0:
        print("\nAbhi tak koi task nahi hai.")
        return
        
    print("\n--- Tumhare Saare Tasks ---")
    for line in lines:
        if line.strip() != "":
            parts = line.strip().split(",")
            if len(parts) >= 3:
                print(parts[0] + " | Sub: " + parts[1] + " | Status: " + parts[2])
            else:
                print(line.strip())
                
import file_handler

def show_summary():
    lines = file_handler.get_all_tasks()
    
    total = 0
    pending = 0
    done = 0
    
    for line in lines:
        if line.strip() != "":
            total = total + 1
            parts = line.strip().split(",")
            
            if len(parts) >= 3:
                if parts[2].strip() == "Pending":
                    pending = pending + 1
                elif parts[2].strip() == "Done":
                    done = done + 1
                    
    print("\n--- Task Summary ---")
    print("Total Tasks     : ", total)
    print("Pending Tasks   : ", pending)
    print("Completed Tasks : ", done)
    print("--------------------")
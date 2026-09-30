import task_manager
import analysis

def show_menu():
    print("\n=== STUDENT TASK MANAGER ===")
    print("1. Naya Task Add Karo")
    print("2. Saare Tasks Dekho")
    print("3. Task Summary (Pending/Done)")
    print("4. Band karo")
    print("============================")

def start_app():
    while True:
        show_menu()
        choice = input("Kya karna hai? (1-4): ").strip()
        
        if choice == "1":
            task_manager.add_new_task()
            input("\n-> Press ENTER to continue...")
            
        elif choice == "2":
            task_manager.show_all_tasks()
            input("\n-> Press ENTER to continue...")
            
        elif choice == "3":
            analysis.show_summary()
            input("\n-> Press ENTER to continue...")
            
        elif choice == "4":
            print("Tata! Padhai karo.")
            break
            
        else:
            print("Galat option!")
            input("\n-> Press ENTER to continue...")

if __name__ == "__main__":
    start_app()
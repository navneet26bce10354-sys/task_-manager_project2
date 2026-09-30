file_name = "tasks_data.txt"

def save_task(line_data):
    # 'a' mode taaki purana data delete na ho
    f = open(file_name, "a")
    f.write(line_data + "\n")
    f.close()

def get_all_tasks():
    try:
        f = open(file_name, "r")
        lines = f.readlines()
        f.close()
        return lines
    except:
        # Agar file nahi bani hai toh khali list do
        return []
        
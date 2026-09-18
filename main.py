filepath = "./logs.txt"

def read_file(filepath):
    try:
        with open(filepath, 'r') as log_fd:
            r_log_fd = log_fd.readlines()
            return r_log_fd
            
    except FileNotFoundError:
        print(f"File not found in path {filepath}")

r_log_fd = read_file(filepath)

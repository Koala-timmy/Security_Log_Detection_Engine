filepath = "./logs.txt"

def read_file(filepath):
    try:
        with open(filepath, 'r') as log_fd:
            r_log_fd = log_fd.readlines()
            return r_log_fd
            
    except FileNotFoundError:
        print(f"File not found in path {filepath}")

r_log_fd = read_file(filepath)

def processor(r_log_fd):

    for i in r_log_fd:
        p_log_fd = i.split()

        if len(p_log_fd) == 4:
            if "LOGIN" in p_log_fd:
                if "SUCCESS" in p_log_fd:
                    event = "LOGIN SUCCESS"

                    print(f"{p_log_fd[3]} : {event}")

            if "LOGIN" in p_log_fd:
                if "FAILED" in p_log_fd:
                    event = "LOGIN FAILED"

                    print(f"{p_log_fd[3]} : {event}")

        # space for managing unknown events

        else:
            print(f"Invalid log: {i}" )

processor(r_log_fd)
filepath = "./logs.txt"
from datetime import date 

def date_constructor():
    current_date = date.today()
    
    today = current_date.strftime("%Y-%m-%d")
    ymd = today.split("-")

    return ymd

ymd = date_constructor()

def read_file(filepath):
    try:
        with open(filepath, 'r') as log_fd:
            r_log_fd = log_fd.readlines()
            return r_log_fd
            
    except FileNotFoundError:
        print(f"File not found in path {filepath}")

r_log_fd = read_file(filepath)

def processor(r_log_fd, ymd):
    C_year = int(ymd[0])
    C_month = int(ymd[1])
    C_day = int(ymd[2])

    print(f"=======================================")

    for item in r_log_fd:
        p_log_fd = item.split()
        valid_log_date = False

        def date_validator(p_log_fd, valid_log_date, C_year, C_month, C_day):
            log_date = p_log_fd[0]
            log_date_data = log_date.split("-")

            if len(log_date_data) == 3: #Date length checker
                log_year = log_date_data[0]

                if log_year.isdigit():
                    log_year = int(log_date_data[0])

                    if log_year > C_year:
                        print("-" * 30)
                        print(f"ERROR - Date out of range. {log_date}")
                        print("-" * 30)

                    elif log_year <= C_year:
                        valid_log_date = True
            
                else:
                    print(f"Invalid log data {log_year}")

                return valid_log_date
                        
        passed = date_validator(p_log_fd, valid_log_date, C_year, C_month, C_day)

        if passed == True:
            if len(p_log_fd) == 4: #Log length Checker
                if "LOGIN" in p_log_fd: #Login Type Checker
                    if "SUCCESS" in p_log_fd:
                        event = "LOGIN SUCCESS"
                        print(f"{p_log_fd[3]} : {event}")

                    elif "FAILED" in p_log_fd:
                        event = "LOGIN FAILED"
                        print(f"{p_log_fd[3]} : {event}")

                elif "FILE" in p_log_fd: #File Change Checker
                    if "DELETED" in p_log_fd:
                        event = "FILE DELETED"
                        print(f"{p_log_fd[3]} : {event}")

                    elif "ADDED" in p_log_fd:
                        event = "FILE ADDED"
                        print(f"{p_log_fd[3]} : {event}")

                else:
                    print(f"Unknown Event: {item}")
                    print(f"User: {p_log_fd[3]}")
            
        else:
            print(f"Validation Failed:\n{item}" )

    print(f"=======================================")

processor(r_log_fd, ymd)
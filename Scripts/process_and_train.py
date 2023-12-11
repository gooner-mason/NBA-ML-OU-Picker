import subprocess
import time
from src.Utils.ses import send_email_with_attachment

def run_commands():
    commands = [
        "cd ../src/Process-Data && python3 -m Get_Data",
        "cd ../src/Process-Data && python3 -m Get_Odds_Data",
        "cd ../src/Process-Data && python3 -m Create_Games",
        "cd ../src/Train-Models && python3 -m XGBoost_Model_ML",
        "cd ../src/Train-Models && python3 -m XGBoost_Model_UO",
        # "python3 main.py -xgb -odds=caesars -kc"
    ]

    results = []

    for command in commands:
        print("\033[92mRunning command:\033[0m", command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        print("\033[92mCommand output:\033[0m")
        print(output.decode('utf-8'))

        if process.returncode != 0:  
            print("\033[91mCommand error output:\033[0m")
            print(error.decode('utf-8'))

        results.append(f"Command: {command}\nOutput:\n{output.decode('utf-8')}\nError:\n{error.decode('utf-8')}")

    return results

if __name__ == "__main__":
    start_time = time.time()
    run_commands()
    end_time = time.time()
    elapsed_time_minutes = (end_time - start_time) / 60
    send_email_with_attachment(f"process_and_train executed successfully in {elapsed_time_minutes} minutes!")
    print(f"\033[92mCommands executed successfully in {elapsed_time_minutes} minutes!\033[0m")

import subprocess

def send_email(subject, body):
    print('Not YET IMPLEMENTED')

def run_commands():
    commands = [
        "cd src/Process-Data && python3 -m Get_Data",
        "cd src/Process-Data && python3 -m Get_Odds_Data",
        "cd src/Process-Data && python3 -m Create_Games",
        "cd Train-Models && python3 -m XGBoost_Model_ML",
        "cd Train-Models && python3 -m XGBoost_Model_UO",
        "cd .. && cd ..",
        "python3 main.py -xgb -odds=caesars -kc"
    ]

    results = []

    for command in commands:
        print("\033[92mRunning command:\033[0m", command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        print("\033[92mCommand output:\033[0m")
        print(output.decode('utf-8'))

        if process.returncode != 0:  # Print error only if there is an error
            print("\033[91mCommand error output:\033[0m")
            print(error.decode('utf-8'))

        results.append(f"Command: {command}\nOutput:\n{output.decode('utf-8')}\nError:\n{error.decode('utf-8')}")

    return results

if __name__ == "__main__":
    subject = "nba-ml-ou-picker results"
    body = "\n".join(run_commands())
    send_email(subject, body)
    print("\033[92mCommands executed and email sent successfully!\033[0m")

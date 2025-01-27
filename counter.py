import time
from tqdm import tqdm  # Add tqdm import for progress bar
import select
import sys
import os  # Add os import for clearing the command line


def concise_bar(times):
    return tqdm(range(times - 1, -1, -1), bar_format="{bar}| {remaining} seconds")


def prompt_user(prompt: str, default_return: str = "") -> str:
    """
    Get user input with a 10 second timeout
    Input:
        prompt: str - message to show user
        default_return: str - value to return if timeout
    Output:
        str - user input or default value
    """
    # Clear input buffer before prompting
    while select.select([sys.stdin], [], [], 0.0)[0]:
        os.read(sys.stdin.fileno(), 1024)

    print(prompt, end="", flush=True)
    # Wait for input with 10 second timeout
    if select.select([sys.stdin], [], [], 10)[0]:
        return input()
    else:
        return default_return


def relax_session(relax_times=60):
    # Start 60s fixed loop
    relax_minutes = 0
    while True:
        print(f"Relaxing for {relax_minutes} minutes...")
        for _ in concise_bar(relax_times):
            time.sleep(1)
        relax_minutes += 1
        user_input = prompt_user("continue study? (y/n)", default_return="n")
        if user_input.lower() == "y":
            break
        clear_screen()


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def counter(times, relax_times=6):
    """
    Function to count down from a given number to zero and then iterate.
    """
    while True:
        for _ in concise_bar(times):
            time.sleep(1)

        prompt_to_user = """
        Type 'q' to quit,
        'r' for 60s loop,
        enter a number to set timer,
        or press Enter to continue: """
        user_input = prompt_user(prompt_to_user, default_return="r")

        if user_input.lower() == "q":
            break

        elif user_input.lower() == "r":
            relax_session(relax_times)

        elif user_input.isdigit():
            times = int(user_input)
            continue
        # Clear the command line
        clear_screen()


def main():
    """
    Main function to run the counter function based on command line input.
    - None
    """
    import sys

    if len(sys.argv) > 2:
        print("Usage: python counter.py [times]")
        return

    try:
        if len(sys.argv) == 2:
            times = int(sys.argv[1])
        else:
            times = 15
            print("No input provided. Using default value: 15")
    except ValueError:
        print("Please provide a valid integer for [times].")
        return

    input("Press Enter to start the counter...")
    counter(times)


if __name__ == "__main__":
    main()

from .counter import counter


def get_times(input_times: str) -> int:
    if input_times.isdigit():
        return int(input_times)
    elif input_times.lower() == "read":
        # 15 minutes
        times = 60 * 15
        return times
    else:
        return 15


def interpret_input(input_times: str) -> int:
    """
    Interpret the input string.
    """
    if input_times.isdigit():
        return int(input_times)
    elif input_times.lower() == "read":
        # 15 minutes
        times = 60 * 15
        return times
    else:
        return 15


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
            if isinstance(sys.argv[1], str):
                times = get_times(sys.argv[1])
            else:
                times = get_times(sys.argv[1])
        else:
            times = 15
            print("No input provided. Using default value: 15")
    except Exception as e:
        print(f"Error: {e}")
        return

    input(f"Press Enter to start the counter. Time: {times} seconds")
    counter(times)


if __name__ == "__main__":
    main()

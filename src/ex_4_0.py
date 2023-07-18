""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    list_shut_down = list()
    with open(logfile, 'r') as file_lg:
        cont = file_lg.read()
    shutEntries = cont.splitlines()
    for shutEntry in shutEntries:
        if 'Shutdown initiated' in shutEntry :
            list_shut_down.append(shutEntry)
    return list_shut_down


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")

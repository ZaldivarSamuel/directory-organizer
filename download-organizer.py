import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

path = "/Users/samuel/Downloads"

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = True
    case_sensitive = True

    event_handler = PatternMatchingEventHandler(patterns, ignore_patterns,
                    ignore_directories, case_sensitive)

    print("Test")

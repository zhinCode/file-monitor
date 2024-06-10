import os
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import Fore, Style, init
from datetime import datetime
from logo import display_logo, display_app_info

# 색상 초기화
init(autoreset=True)

# 상수 변수
APP_VERSION = "0.0.1"
APP_AUTHOR = "Zhin"
APP_YEAR = "2024"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5MB

# 현재 실행 파일이 시작된 디렉토리와 그 하위 디렉토리 제외
EXCLUDE_DIR = os.path.abspath(os.path.dirname(__file__))

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, log_dir, log_filename):
        self.log_dir = log_dir
        self.log_filename = log_filename
        self.log_file = os.path.join(log_dir, log_filename)
        self.file_index = 0
        super().__init__()

    def on_created(self, event):
        self._log_event(event, 'C', Fore.GREEN)

    def on_deleted(self, event):
        self._log_event(event, 'D', Fore.RED)

    def on_modified(self, event):
        self._log_event(event, 'U', Fore.YELLOW)

    def on_moved(self, event):
        self._log_event(event, 'M', Fore.BLUE)

    def _log_event(self, event, action, color):
        if EXCLUDE_DIR in event.src_path:
            return
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'{timestamp} {action} - {event.src_path}'
        print(f'{color}{log_message}{Style.RESET_ALL}')

        # 로그 파일에 기록
        self._write_log(log_message)

    def _write_log(self, log_message):
        if os.path.exists(self.log_file) and os.path.getsize(self.log_file) > MAX_LOG_SIZE:
            self.file_index += 1
            base_filename, ext = os.path.splitext(self.log_filename)
            self.log_file = os.path.join(self.log_dir, f'{base_filename}_{self.file_index}{ext}')

        with open(self.log_file, 'a', encoding='utf-8') as log:
            log.write(log_message + '\n')

def get_all_drives():
    partitions = psutil.disk_partitions()
    drives = [p.mountpoint for p in partitions if p.fstype != '']
    return drives

def monitor_directories(paths):
    # 로그 디렉토리 생성
    log_dir = 'log'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 로그 파일명 생성
    log_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.txt'

    observers = []
    event_handler = FileEventHandler(log_dir, log_filename)

    for path in paths:
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observers.append(observer)
        observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        for observer in observers:
            observer.stop()
        for observer in observers:
            observer.join()

if __name__ == "__main__":
    display_logo()
    display_app_info(APP_VERSION, APP_AUTHOR, APP_YEAR)
    drives = get_all_drives()
    monitor_directories(drives)

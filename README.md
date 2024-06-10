# file-monitor

file-monitor(filemon) is a Python application to monitor file system events on all mounted drives.

Log files are stored in the ./log directory.
When a log file exceeds 5MB, a new file is created with an incremented index.
Log files are encoded in UTF-8.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/zhinCode/file-monitor.git
    cd file-monitor
    ```

2. Install dependencies:

    ```sh
    pip install watchdog colorama psutil
    ```

## Usage

To run the application:

```sh
python main.py
```

## Configuration



## License
This project is licensed under the MIT License.

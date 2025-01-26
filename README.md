# ClatChecker DownDetector Tool

A Python script for monitoring multiple website domains in real-time, displaying whether they are accessible (“up”) or unreachable (“down”). It also logs these status checks to a file (`website_monitor.log`). This tool runs until the user presses **ENTER**, allowing continuous website monitoring.

![clatchecker](https://github.com/user-attachments/assets/09f3dfc8-8254-45d1-bc33-235b6395dcda)

## Features
- **Multi-Domain Monitoring**: Checks multiple domains (entered by the user) in one script run.
- **Real-Time Checking**: Monitors each domain’s status every 1 second.
- **Immediate Stop**: Press **ENTER** at any time to halt the continuous check loop.
- **Colorful Output**: Uses the [Pystyle](https://pypi.org/project/Pystyle/) library for styled console printing (e.g., banners, color-coded text).
- **Logging**: Records each check result (e.g., “up”, “down”, errors) in `website_monitor.log`.

## How It Works

1. **User Input**:  
   - The script prompts you to input one or more domains (separated by commas).

2. **Background Thread**:
   - A separate “stopper” thread waits for the user to press **ENTER**.
   - Once pressed, it sets a `stop_flag` to `True`, signalling the monitoring loop to stop.

3. **Monitoring Loop**:
   - Repeatedly sends `GET` requests (via `requests.get()`) to each domain every 1 second.
   - If a domain returns an HTTP status code of **200**, it prints `"[+] <domain> is up"`.
   - If the HTTP code is not 200 or an exception occurs, it prints and logs a message indicating the site is down or inaccessible.
   - Continues indefinitely until **ENTER** is pressed.

4. **Logging**:
   - Saves each status check (timestamped) to `website_monitor.log` using the Python `logging` module.

## Installation

1. **System Requirements**:
   - **Python 3.6+** recommended.
   - OS compatibility: The script should work on any OS (Windows, macOS, Linux) as long as `pystyle` supports it.

2. **Python Libraries**:
   - [`requests`](https://docs.python-requests.org/en/master/)  
   - [`pystyle`](https://pypi.org/project/Pystyle/)  
   - `logging` (standard library)  
   - `time` (standard library)  
   - `threading` (standard library)

3. **Install Required Libraries**:

pip install requests pystyle

## Usage

1. **Clone or Copy** the script (e.g., `down_detector.py`) to your local machine.

2. **Run the Script**

3. **Input Domains**:
   - When prompted, enter one or more domain names separated by commas (e.g., `https://example.com, https://anotherdomain.com`).

4. **Monitoring**:
   - The script will check each domain in a loop every 1 second.
   - It will display whether each domain is up or down in the console.

5. **Stop Monitoring**:
   - At any time, press **ENTER** in the console window.
   - The script will exit the loop and print “Monitoring stopped.”

## Configuration

- **Check Interval**:
  - Currently hard-coded to **1 second** (`time.sleep(1)` in the `monitor_websites()` function).  
  - Adjust as needed for heavier or lighter monitoring frequencies.

- **Logging Setup**:
  - Logging is configured in the `main()` function with:
    
    logging.basicConfig(
        filename='website_monitor.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
  
  - Modify `filename`, `level`, or `format` as desired.

## Limitations and Known Issues

1. **Heavy Logging**:
   - Checking every second and logging each result can quickly grow `website_monitor.log`.  
   - Consider rotating logs or adjusting the check interval.

2. **No HTTPS Verification Settings**:
   - Currently, SSL verification is not altered. If you require special SSL certificates or want to disable verification, you must adjust the `requests.get()` parameters.

3. **Script Running Indefinitely**:
   - The script only stops when **ENTER** is pressed, so it’s not suitable for use in a purely headless environment (unless you modify the code).

4. **Connectivity Issues**:
   - A domain returning a non-200 code is flagged as “down,” but the domain may actually be reachable with a different status code. Modify as needed if your use case differs (e.g., for APIs returning 201, 204, etc.).

## Troubleshooting

- **Pressing ENTER Doesn’t Stop**:
  - In some shells or IDEs, the input buffering behavior might vary. Ensure you are running the script in a standard terminal or console.

- **Logging Not Working**:
  - Check that you have write permissions to the directory where the script runs.  
  - Verify the `logging` level and filepath in `logging.basicConfig`.

- **ImportError for `pystyle`**:
  - Make sure you installed the library with `pip install pystyle`.  
  - If installed globally, confirm your Python interpreter in the environment can see it.

**Author**:  
🛡️ By Joshua M Clatney - Ethical Pentesting Enthusiast 🛡️  
**Version**: 1.00  

**Disclaimer**: This script is provided as-is for basic website monitoring. Please adapt configurations (e.g. interval, logging verbosity) to your own requirements.

Copyright 2025 Joshua M Clatney (Clats97)

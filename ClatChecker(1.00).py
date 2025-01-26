from pystyle import Colors, Write
import requests
import time
import logging
import threading

stop_flag = False

def wait_for_enter():
    """
    Wait for user to press ENTER; when pressed, set stop_flag to True.
    """
    input("\nPress ENTER at any time to stop monitoring...\n")
    global stop_flag
    stop_flag = True

def monitor_websites(domains):
    """
    Check the given domains every 1 second until stop_flag is True.
    Logs and prints whether each domain is up or down.
    """
    global stop_flag
    while not stop_flag:
        for domain in domains:
            try:
                response = requests.get(domain.strip())
                if response.status_code == 200:
                    print(f"[+] {domain} is up")
                    logging.info(f"{domain} is up (HTTP 200)")
                else:
                    print(f"[-] {domain} is down (HTTP {response.status_code})")
                    logging.info(f"{domain} is down (HTTP {response.status_code})")
            except requests.exceptions.RequestException as e:
                print(f"[!] Error connecting to {domain}: {e}")
                logging.error(f"Error connecting to {domain}: {e}")
        time.sleep(1)

def main():
    try:
        
        print("\033[1;31m  ██████╗██╗     █████╗ ████████╗\033[0m")
        print("\033[1;31m ██╔════╝██║    ██╔══██╗╚══██╔══╝\033[0m")
        print("\033[1;31m ██║     ██║    ███████║   ██║   \033[0m")
        print("\033[1;31m ██║     ██║    ██╔══██║   ██║   \033[0m")
        print("\033[1;31m ╚██████╗███████╗██║  ██║   ██║   \033[0m")
        print("\033[1;31m  ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝   \033[0m")

        
        print("\033[1;31m ██████╗    ██╗  ██╗    ███████╗     ██████╗    ██╗  ██╗    ███████╗    ██████╗ \033[0m")
        print("\033[1;31m██╔════╝    ██║  ██║    ██╔════╝    ██╔════╝    ██║ ██╔╝    ██╔════╝    ██╔══██╗\033[0m")
        print("\033[1;31m██║         ███████║    █████╗      ██║         █████╔╝     █████╗      ██████╔╝\033[0m")
        print("\033[1;31m██║         ██╔══██║    ██╔══╝      ██║         ██╔═██╗     ██╔══╝      ██╔══██╗\033[0m")
        print("\033[1;31m╚██████╗    ██║  ██║    ███████╗    ╚██████╗    ██║  ██╗    ███████╗    ██║  ██║\033[0m")
        print("\033[1;31m ╚═════╝    ╚═╝  ╚═╝    ╚══════╝     ╚═════╝    ╚═╝  ╚═╝    ╚══════╝    ╚═╝  ╚═╝\033[0m")
        print()
        print("\033[1;34mD  O  W  N  D  E  T  E  C  T O R       T  O  O  L\033[0m\t\033[1;31mVersion 1.00\033[0m")

        
        author_line = "🛡️ By Joshua M Clatney - Ethical Pentesting Enthusiast 🛡️"
        Write.Print(author_line + "\n", Colors.white, interval=0)

        
        print()

        
        Write.Print("Domain Status Checker\n", Colors.white, interval=0)
        Write.Print("Site Status In Seconds\n", Colors.white, interval=0)

    except Exception as e:
        print(f"Error displaying banner: {e}")

    
    logging.basicConfig(
        filename='website_monitor.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    
    domains_input = input("Enter the domain(s) (comma separated): ")
    domains_list = [domain.strip() for domain in domains_input.split(',') if domain.strip()]

    if not domains_list:
        print("No valid domain(s) provided. Exiting...")
        return

    # Start a thread to detect when the user presses Enter
    stopper_thread = threading.Thread(target=wait_for_enter, daemon=True)
    stopper_thread.start()

    # Start monitoring the websites (indefinitely until user presses ENTER)
    monitor_websites(domains_list)
    print("Monitoring stopped.")

if __name__ == "__main__":
    main()
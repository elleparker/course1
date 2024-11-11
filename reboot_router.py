import telnetlib

def main():
    # Router credentials
    HOST = "192.168.1.1"
    PASSWORD = "MyPassword"
    COMMAND = "set reboot"

    try:
        # Connect to the router via telnet
        tn = telnetlib.Telnet(HOST)

        # Enter password
        tn.read_until(b"Password: ")
        tn.write(PASSWORD.encode('ascii') + b"\n")

        # Execute reboot command
        tn.write(COMMAND.encode('ascii') + b"\n")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

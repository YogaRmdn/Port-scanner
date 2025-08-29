import socket
import time
import sys
from options.header import *
from options.color import *


def port_scan(target, port_awal, port_akhir):
    try:
        print(f"{b_green}[*]{reset} Memulai scanning pada IP : {target} port [{port_awal}] - [{port_akhir}]")
        print(f"{b_green}\nPORT\t\tSTATUS\t\tSERVICE{reset}")
        print(f"{b_white}-{reset}" * 40)

        for port in range(port_awal, port_akhir + 1):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                data = s.connect_ex((target, port))

                if data == 0:
                    try:
                        service = socket.getservbyport(port)
                        print(f"{port}\t\tOPEN\t\t{service}")
                        time.sleep(0.5)
                    except:
                        service = "Unknown"
                        print(f"{port}\t\t{b_green}OPEN{b_green}\t\tUnknown")
                        time.sleep(0.5)
                s.close()

            except socket.gaierror:
                print(f"\n{b_red}[!] Gagal terhubung ke {target}{reset}")
                break
            except Exception as e:
                print(f"{b_red}[!] Error lain : {e}{reset}")
                break

    except KeyboardInterrupt:
        print(f"{b_red}[!] Tools dibatalkan...{reset}")
        sys.exit()


if __name__ == "__main__":
    while True:
        try:
            clean_screen()
            header_tools()
            target = input(f"{b_green}[?]{reset} IP target\t: ")
            start = int(input(f"{b_green}[?]{reset} Port awal\t: "))
            stop = int(input(f"{b_green}[?]{reset} Port akhir\t: "))

            port_scan(target, start, stop)
            print(f"\n{b_green}[✔] Scanning selesai...{reset}")
            t = input(f"{b_green}[?]{reset} Lagi? (y/n) : ")
            if t.lower() == "y":
                time.sleep(0.5)
                continue
            else:
                print(f"\n{b_green}[✔] Keluar dari tools...{reset}")
                time.sleep(0.5)
                break

        except KeyboardInterrupt:
            print(f"\n{b_red}[!] Tools dibatalkan...{reset}")
            time.sleep(0.5)
            break

from options.color import *
import os
import platform

def clean_screen():
    os.system("cls" if platform == "nt" else "clear")


def header_tools():
    print(f"""{b_yellow}
(                                                    
 )\ )           )                                     
(()/(    (   ( /(             )               (  (    
 /(_))(  )(  )\())  (   (  ( /(  (     (     ))\ )(   
(_))  )\(()\(_))/   )\  )\ )(_)) )\ )  )\ ) /((_|()\  
| _ \((_)((_) |_   ((_)((_|(_)_ _(_/( _(_/((_))  ((_) {reset}{b_red}
|  _/ _ \ '_|  _|  (_-< _|/ _` | ' \)) ' \)) -_)| '_| 
|_| \___/_|  \__|  /__|__|\__,_|_||_||_||_|\___||_|   {reset}{b_white}
            
            Author  : Bang yog
            Tools   : Port scanner
            Tiktok  : Bang yog{reset}{b_red}
-----------------------------------------------------
{reset}""")
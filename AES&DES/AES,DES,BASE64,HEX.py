import os
import base64
import hashlib
import binascii
from Crypto.Cipher import AES
from pyDes import *

#pip install Cryptodome

class AnalysisSwitch:
    def __init__(self):
        self.input_data()

    def input_data(self):
        Switch_data = input("Please Choice Number.. : ")
        self.Func(Switch_data)
        
    def Func(self, arg):
        if arg == "":
            self.input_data()
        self.case_name = "case_"+str(arg)
        self.case = getattr(self, self.case_name)
        return self.case()
        
    def case_1(self):
        try:
            b64a = input("base64 : ")
            keyde = base64.b64decode(b64a)
            print(keyde.decode("utf-8"))
            input("Press enter to exit ;)")
            Script_main()
        except AttributeError as e:
            print(e)
            
    def case_2(self):
        try:
            code = input("Chrome Incode : ")
            #"7akmFhsbpeF1odwY5JnYBs-Fo-5v0_42"
            #oeewe7akmFhsbpeF1odwY5JnYBs-Fo-5v0_42oeewe
            code = code.replace('oeewe','')
            #print(code)
            
            key = "Ab5d1Q32"

            keyE = key.encode("UTF-8")
            codeE = code.encode("UTF-16")

            keyde = base64.urlsafe_b64decode(key)
            codede = base64.urlsafe_b64decode(code)

            keydeD = keyde.decode("utf-16")
            codedeD = codede.decode("utf-16")

            k = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)

            d = k.decrypt(codede)
            f = d.decode("utf-8")
            f = f.replace("'","")
            print("Chrome Decode : "+f)
            input("Press enter to exit ;)")
            Script_main()
            
        except AttributeError as e:
            print(e)
            
    def case_3(self):
        try:
            cap = input("Capital Incode : ")
            cap = cap.replace('"','')
            cap = cap.replace(' ','')
            cap2 = cap.split(",")
            #"7flMlX9FRY/i5xlUFkS/Bw==", "ZUGLeC0xaDiarEO/1oAqBQ==", "a/JNQAhmlNXR2j0QZrh7LQ==", "oPrrwnMjWc0gDvyQZkp6kA==", "yyjuSyPIVErwP//xUhuIdQ=="
            result = list()
            for i in cap2:
                
                BS = AES.block_size
                pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
                unpad = lambda s : s[0:-s[-1]]

                key = b"9739DF758A34160C"; # 32bit
                iv = b'0102030405060708' # 16bit

                cipher = AES.new(key, AES.MODE_CBC, IV=iv)
                deciphed = cipher.decrypt(base64.b64decode(i))
                deciphed = unpad(deciphed)
                deciphed = deciphed.decode("utf-8")
                result.append(deciphed)
            print(", ".join(result))
            #print ('Capital Decode: '+str(deciphed))
            
            input("Press enter to exit ;)")
            Script_main()
            
        except AttributeError as e:
            print(e)
            
    def case_4(self):
        try:
            #cmH4Kh30LB/wLh7sLR72KS@yKyj2KybvGy@3MyPeNCTwKyDyGy@uLh/vLh/wLSDsLC@xG2MwcFP<
            
            #print (len(test))
            try:
                see8 = input("Config.DB Incode : ")

                fuck = ''
                for you in see8:
                    fuck = fuck + chr(ord(you)+1)

                gae3ki = base64.b64decode(fuck).decode('utf-8')

                got = ''
                for jo in gae3ki:
                    got = got + chr(ord(jo)+1)
                got = got.split(' ')
                print("IP Adders : " + got[0])
                print("Port Number : " + got[1])
                print("Password : " + got[2])
                print("URL : " + got[3])
                
            except TypeError as e:
                print(e)
            #print(test)
        except AttributeError as e:
            print(e)
            
def Script_main():
    os.system("cls")
    func = AnalysisSwitch()
    
if __name__ == '__main__':
    Script_main()

import os
import time

v = input("dulnchecker checks if you are compatible for duping. press Y to proceed or N to cancel.")
if v=="N":
    print("dulnchecker cancelled")
elif v=="Y":
    print("dulnchecker proceeding")
    print("checking version")
    y=os.getenv('LOCALAPPDATA')
    appd=os.path.abspath(os.path.join(y, os.pardir))
    print(appd)
    if os.path.isdir(os.path.join(appd, "LocalLow")):
        print("LocalLow Found")
        ll = os.path.join(appd, "LocalLow")
        if os.path.isdir(os.path.join(ll, "JustPlay_LOL")):
            print("JustPlay_LOL Found")
            JPL = os.path.join(ll, "JustPlay_LOL")
            if os.path.isdir(os.path.join(JPL, "1v1_LOL")):
                print("Sucessfully Found 1v1_LOL LL Folder")
                ILOL = os.path.join(JPL, "1v1_LOL")
                if os.path.isdir(os.path.join(ILOL, "com.unity.addressables")):
                    print("Writing to unity addressables")
                    CM = os.path.join(ILOL, "com.unity.addressables")
                    #CheckVer
                    name="catalog_2024.02.08.14.36.16.json"
                    for root, dirs, files in os.walk(CM):
                        if name in files:
                            o=input("This Version can be duped on! Type Y to proceed.")
                            if o=="Y":
                                #Insert DupeCode
                                print("Writing to dupe.sig file in dulnchecker. Once this window closes, you can follow the instructions on the github page!")
                                time.sleep(7)
                                f = open("dupe.sig", "w")
                                f.write("Checked version: Dupe available. Version Found: ")
                                f.close()
                                a = open("dupe.sig", "a")
                                a.write(name)
                                a.close()
                                #For some reason had to move the print above the code due to errors, shouldnt effect anything though.
                                print("Wrote to dupe.sig sucessfully!. You can now follow the instructions on the github page!")
                                time.sleep(1)
                            else:
                                print("dupe.sig writing cancelled. Press anything to exit")
                                time.sleep(1)
                        else:
                            print("Writing to dupe.sig file in dulnchecker. Your version cannot be duped on.")
                            time.sleep(7)
                            f = open("dupe.sig", "w")
                            f.write("Checked version: Dupe unavailable. Version Found: ")
                            f.close()
                            f = open("dupe.sig", "a")
                            f.write(name)
                            f.close()
                            print("Cannot dupe on your version. Press anything to exit")
                            time.sleep(1)

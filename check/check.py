import os
import shutil
import threading
import time


def check1():
    # 指定你想要监控的文件
    file_path = r"C:\Program Files (x86)\Seewo\EasiNote5\EasiNote5_5.2.3.1507\Main\Assets\SplashScreen.png"

    # 获取文件的最后修改时间
    last_modified = os.stat(file_path).st_mtime

    while True:
        time.sleep(1)  # 每秒检查一次

        # 再次获取文件的最后修改时间
        try:
            current_modified = os.stat(file_path).st_mtime

        except Exception:
            shutil.copy("D:/SplashScreen.png",
                        r"C:\Program Files (x86)\Seewo\EasiNote5\EasiNote5_5.2.3.1507\Main\Assets")
            last_modified = os.stat(file_path).st_mtime

        if current_modified != last_modified:
            shutil.copy("D:/SplashScreen.png",
                        r"C:\Program Files (x86)\Seewo\EasiNote5\EasiNote5_5.2.3.1507\Main\Assets")


def check2():
    file_path = os.environ['USERPROFILE'] + "/AppData/Roaming/Seewo/EasiNote5/Resources/Banner/Banner.png"
    try:
        last_modified = os.stat(file_path).st_mtime

    except Exception:
        shutil.copy("D:/Banner.png",
                    os.environ['USERPROFILE'] + "/AppData/Roaming/Seewo/EasiNote5/Resources/Banner/")
        last_modified = os.stat(file_path).st_mtime


    while True:
        time.sleep(1)  # 每秒检查一次

        # 再次获取文件的最后修改时间
        try:
            current_modified = os.stat(file_path).st_mtime

        except Exception:
            shutil.copy("D:/Banner.png",
                        os.environ['USERPROFILE'] + "/AppData/Roaming/Seewo/EasiNote5/Resources/Banner/")

        if current_modified != last_modified:
            try:
                shutil.copy("D:/Banner.png",
                        os.environ['USERPROFILE'] + "/AppData/Roaming/Seewo/EasiNote5/Resources/Banner/")

            except Exception:
                time.sleep(3)
                shutil.copy("D:/Banner.png",
                os.environ['USERPROFILE'] + "/AppData/Roaming/Seewo/EasiNote5/Resources/Banner/")


threading.Thread(target=check1).start()
threading.Thread(target=check2).start()

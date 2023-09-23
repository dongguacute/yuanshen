swenlauncher = """C:\Program Files (x86)\Seewo\EasiNote5\swenlauncher\swenlauncher.exe"""

set ws = createobject("wscript.shell")
' ±¸·Ý
ws.run "xcopy %userprofile%\AppData\Roaming\Seewo\EasiNote5\Resources\Banner\Banner.png %userprofile%\AppData\Roaming\Seewo\EasiNote5\Resources\Banner\Banner1.png /Y",vbhide
ws.run "xcopy img.png %userprofile%\AppData\Roaming\Seewo\EasiNote5\Resources\Banner\Banner.png /Y",vbhide
ws.run swenlauncher,vbhide
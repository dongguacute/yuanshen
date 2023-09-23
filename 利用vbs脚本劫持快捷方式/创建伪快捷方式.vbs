thisFolder = createobject("Scripting.FileSystemObject").GetFolder(".").Path '获取当前目录

' name：快捷方式名称
' targetPath：快捷方式的执行路径
' Icon：快捷方式图标
' description：快捷方式的描述
' workingDirectory：起始位置
Function CreateShortcutOnDesktop(name, targetPath, Icon, description, workingDirectory)
    set WshShell    = Wscript.CreateObject("Wscript.Shell") 
    strDesktop  = WshShell.SpecialFolders("Desktop") '在桌面创建快捷方式
    set oShellLink  = WshShell.CreateShortcut(strDesktop&"\"&name&".lnk") '创建一个快捷方式对象
    oShellLink.TargetPath  = targetPath '设置快捷方式的执行路径 
    oShellLink.WindowStyle = 7 '运行方式
    oShellLink.IconLocation= Icon '设置快捷方式的图标
    oShellLink.Description = description  '设置快捷方式的描述 
    oShellLink.WorkingDirectory = workingDirectory '起始位置
    oShellLink.Save
End Function


Call CreateShortcutOnDesktop("希沃白板 5", thisFolder&"\yuanshen.vbs", "C:\Program Files (x86)\Seewo\EasiNote5\swenlauncher\swenlauncher.exe", "", thisFolder) '创建快捷方式
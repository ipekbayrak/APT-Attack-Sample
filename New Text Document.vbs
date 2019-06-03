Option Explicit

Dim WshShell, strWinDir, strCmdLine, lngExitCode
Const OpenAsCurrentWindowIsOpened = 10, WaitForExit = True

Set WshShell = CreateObject("WScript.Shell")
strWinDir = WshShell.ExpandEnvironmentStrings("%WINDIR%")

strCmdLine = strWinDir & "\System32\SCHTASKS.exe /create /SC ONCE /TN ""TASK2"" /TR ""c:/admin.bat"" /ST 00:28  /RL HIGHEST /RU ""NT AUTHORITY\SYSTEM"""

lngExitCode = WshShell.Run(strCmdLine, OpenAsCurrentWindowIsOpened, WaitForExit)

If lngExitCode = 0 Then
  WScript.Echo "Success"
Else
  WScript.Echo "Failed with error code " & CStr(lngExitCode)
End If
Set WshShell = WScript.CreateObject("WScript.Shell")
WshShell.Run "cmd.exe /c ssh -o StrictHostKeyChecking=no gates538@192.168.179.145 ""ha core restart || sudo systemctl restart homeassistant || docker restart homeassistant > restart_log.txt 2>&1""", 1, False
WScript.Sleep 3000
WshShell.SendKeys "Apis12345"
WshShell.SendKeys "{ENTER}"
WScript.Sleep 1000

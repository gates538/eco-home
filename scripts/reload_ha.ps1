$token = "e156a2c3dfb9586571ca978180a89b37231af3bbac7039e020e3eae7c113b42ce865df6529b72855994a370d1d4a6e858197b0e5eb56041add9b3057046e7ac1"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

Write-Host "Reloading Home Assistant Automations..."
$res1 = Invoke-RestMethod -Uri "http://192.168.179.145:8123/api/services/automation/reload" -Method POST -Headers $headers
Write-Host "Automation Reload Result: $res1"

Write-Host "Reloading Core Config..."
$res2 = Invoke-RestMethod -Uri "http://192.168.179.145:8123/api/services/homeassistant/reload_core_config" -Method POST -Headers $headers
Write-Host "Core Config Reload Result: $res2"

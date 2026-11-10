# After a reboot: continue H-iso (finished cells and DFT runs are cached) and the last discovery round.
# Low heat: pw.x on 2 cores instead of 4. Run from the project root:  powershell -File scripts/resume_all.ps1
Set-Location (Split-Path $PSScriptRoot -Parent)
$env:HISO_NP = "2"
Start-Process -FilePath ".\.venv\Scripts\python.exe" -ArgumentList "scripts/hiso_l12_v2.py" -RedirectStandardOutput "data\hiso_l12_dft_v2.log" -RedirectStandardError "data\hiso_l12_dft_v2.err" -WindowStyle Hidden
# Start-Process -FilePath ".\.venv\Scripts\python.exe" -ArgumentList "scripts/discovery_round.py","emix_random","--deep","--resume" -RedirectStandardOutput ".orchestra\round3.log" -RedirectStandardError ".orchestra\round3.err" -WindowStyle Hidden
"started H-iso (np 2) and round 3 resume"

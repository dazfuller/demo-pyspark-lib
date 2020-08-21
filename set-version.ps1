param (
    [Parameter(Mandatory=$true)] [string] $BuildId
)

$updatedSetup = (Get-Content ./setup.py) -replace "0.0.1", "0.0.$BuildId"
$updatedModule = (Get-Content ./dazspark/__init__.py) -replace "0.0.1", "0.0.$BuildId"

$updatedSetup | Out-File ./setup.py
$updatedModule | Out-File ./dazspark/__init__.py
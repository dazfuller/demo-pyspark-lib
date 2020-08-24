param (
    [Parameter(Mandatory=$false)] [switch] $IsDevRelease,
    [Parameter(Mandatory=$false)] [string] $BuildId
)

if ($IsDevRelease -and $BuildId -eq $null) {
    throw "A build id number must be provided for development releases"
}

$versionMatch = Get-Content ./setup.py | Select-String -Pattern "version=`"(.+)`""

if ($null -eq $versionMatch) {
    throw "Unable to find version information"
} else {
    $currentVersion = $versionMatch.Matches.Groups[1].Value
}

$nextVersion = $currentVersion

if ($IsDevRelease) {
    $nextVersion = "$currentVersion.dev$BuildId"
} else {
    $versionParts = $currentVersion.Split(".")
    $versionParts[-1] = ([int]$versionParts[-1]) + 1
    $nextVersion = $versionParts -join "."
}

$updatedSetup = (Get-Content ./setup.py) -replace $currentVersion, $nextVersion
$updatedModule = (Get-Content ./dazspark/__init__.py) -replace $currentVersion, $nextVersion

$updatedSetup | Out-File ./setup.py
$updatedModule | Out-File ./dazspark/__init__.py
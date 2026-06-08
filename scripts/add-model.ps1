param(
    [Parameter(Mandatory)][string]$ModelName,
    [Parameter(Mandatory)][string]$DockerImage,
    [Parameter(Mandatory)][string]$Subdomain,
    [Parameter(Mandatory)][string]$Title,
    [Parameter(Mandatory)][string]$Models,
    [Parameter(Mandatory)][string]$Domain,
    [string]$Accuracy = "",
    [string]$Tags = "",
    [Parameter(Mandatory)][string]$Github,
    [Parameter(Mandatory)][string]$HfSpace,
    [string]$Status = "pending"
)

$registry = [System.Collections.ArrayList]::new()
$parsed = Get-Content models.json -Raw | ConvertFrom-Json
foreach ($item in $parsed) {
    [void]$registry.Add($item)
}

$exists = $registry | Where-Object { $_.name -eq $ModelName }
if ($exists) {
    Write-Host "Model '$ModelName' already registered, skipping."
    exit 0
}

$tagsArray = if ($Tags) { $Tags -split "," | ForEach-Object { $_.Trim() } } else { @() }

$entry = [PSCustomObject]@{
    name      = $ModelName
    title     = $Title
    models    = $Models
    domain    = $Domain
    accuracy  = $Accuracy
    tags      = $tagsArray
    status    = $Status
    github    = $Github
    hf_space  = $HfSpace
    image     = $DockerImage
    subdomain = $Subdomain
}

[void]$registry.Add($entry)

ConvertTo-Json -InputObject ($registry.ToArray()) -Depth 10 | Set-Content models.json -Encoding UTF8

Write-Host "Model '$ModelName' registered successfully."
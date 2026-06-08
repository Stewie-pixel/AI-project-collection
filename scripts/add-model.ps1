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

$models = @(Get-Content models.json | ConvertFrom-Json)

$exists = $models | Where-Object { $_.name -eq $ModelName }

if ($exists) {
    Write-Host "Model '$ModelName' already registered, skipping."
    exit 0
}

$tagsArray = if ($Tags) { $Tags -split "," | ForEach-Object { $_.Trim() } } else { @() }

$entry = @{
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

$models += $entry
ConvertTo-Json -InputObject @($models) -Depth 5 | Set-Content models.json

Write-Host "Model '$ModelName' registered successfully."
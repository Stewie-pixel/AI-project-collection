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

$modelsPath = Resolve-Path "models.json"
$registry   = [System.Collections.ArrayList]::new()

try {
    $content = [System.IO.File]::ReadAllText($modelsPath)
    $parsed  = $content | ConvertFrom-Json
    foreach ($item in $parsed) { [void]$registry.Add($item) }
} catch {
    Write-Error "Failed to parse models.json: $_"
    exit 1
}

if ($registry | Where-Object { $_.name -eq $ModelName }) {
    Write-Host "Model '$ModelName' already registered, skipping."
    exit 0
}

$tagsArray = if ($Tags) { @($Tags -split "," | ForEach-Object { $_.Trim() }) } else { @() }

[void]$registry.Add([PSCustomObject]@{
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
})

$json = ConvertTo-Json -InputObject ($registry.ToArray()) -Depth 10
$noBomUt8 = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($modelsPath, $json, $noBomUt8)

Write-Host "Model '$ModelName' registered successfully."
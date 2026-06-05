param(
    [Parameter(Mandatory)][string]$ModelName,
    [Parameter(Mandatory)][string]$DockerImage,
    [Parameter(Mandatory)][string]$Subdomain
)

$models = Get-Content models.json | ConvertFrom-Json
$models += @{ name = $ModelName; image = $DockerImage; subdomain = $Subdomain }
$models | ConvertTo-Json -Depth 3 | Set-Content models.json

$overlayPath = "k8s\overlays\$ModelName"
New-Item -ItemType Directory -Force -Path $overlayPath | Out-Null

$kustomization = @"
resources:
  - ../../base
patches:
  - patch: |-
      - op: replace
        path: /metadata/name
        value: $ModelName
      - op: replace
        path: /spec/selector/matchLabels/app
        value: $ModelName
      - op: replace
        path: /spec/template/metadata/labels/app
        value: $ModelName
      - op: replace
        path: /spec/template/spec/containers/0/image
        value: $DockerImage
    target:
      kind: Deployment
  - patch: |-
      - op: replace
        path: /metadata/name
        value: $ModelName
      - op: replace
        path: /spec/selector/app
        value: $ModelName
    target:
      kind: Service
"@

$kustomization | Set-Content "$overlayPath\kustomization.yml"

Write-Host "Model '$ModelName' added successfully."
$models = Get-Content models.json | ConvertFrom-Json

foreach ($model in $models) {
    Write-Host "Deploying $($model.name)..."
    kubectl apply -k "k8s\overlays\$($model.name)"
}

powershell -File scripts\generate-ingress.ps1
kubectl apply -f k8s\ingress\ingress.yml

Write-Host "All $($models.Count) model(s) deployed."
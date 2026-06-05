$models = Get-Content models.json | ConvertFrom-Json

$rules = ""
foreach ($model in $models) {
    $rules += "  - host: $($model.subdomain).localhost`n"
    $rules += "    http:`n"
    $rules += "      paths:`n"
    $rules += "        - path: /`n"
    $rules += "          pathType: Prefix`n"
    $rules += "          backend:`n"
    $rules += "            service:`n"
    $rules += "              name: $($model.name)`n"
    $rules += "              port:`n"
    $rules += "                number: 80`n"
}

$ingress = @"
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ml-models-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
$rules
"@

$ingress | Set-Content "k8s\ingress\ingress.yml"
Write-Host "Ingress regenerated for $($models.Count) model(s)."
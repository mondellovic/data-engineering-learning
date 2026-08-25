targetScope = 'subscription'

@description('Azure regionen hvor ressourcerne skal udrulles')
param location string = 'swedencentral' // Ændret fra westeurope til swedencentral

@description('Navnet på Resource Group')
param resourceGroupName string = 'rg-nordic-retail-group-dev'

// 1. Opret Resource Group
resource rg 'Microsoft.Resources/resourceGroups@2023-07-01' = {
  name: resourceGroupName
  location: location
  tags: {
    Environment: 'Development'
    Project: 'Nordic Retail Group Data Platform'
  }
}

// 2. Deploy Ressourcer i Resource Group via modul
module resources 'modules/resources.bicep' = {
  name: 'resourcesDeployment'
  scope: rg
  params: {
    location: location
  }
}

// Outputs
output resourceGroupName string = rg.name
output storageAccountName string = resources.outputs.storageAccountName
output keyVaultName string = resources.outputs.keyVaultName

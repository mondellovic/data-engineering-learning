// Bicep Main Deployment File - Data Platform Infrastructure
@description('Location for all resources.')
param location string = resourceGroup().location

@description('Prefix for resource names.')
param prefix string = 'delearn'

@description('Environment name.')
param environment string = 'dev'

var storageName = '${prefix}st${environment}${uniqueString(resourceGroup().id)}'
var keyVaultName = '${prefix}-kv-${environment}-${uniqueString(resourceGroup().id)}'
var adfName = '${prefix}-adf-${environment}-${uniqueString(resourceGroup().id)}'

// Azure Data Lake Storage Gen2 (Hierarchical Namespace enabled)
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: take(storageName, 24)
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true // Enable ADLS Gen2 Hierarchical Namespace
    accessTier: 'Hot'
    supportsHttpsTrafficOnly: true
  }
}

// Containers inside ADLS Gen2 (Medallion Architecture Storage)
resource rawContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  name: '${storageAccount.name}/default/raw'
}

resource cleansedContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  name: '${storageAccount.name}/default/cleansed'
}

resource curatedContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  name: '${storageAccount.name}/default/curated'
}

// Azure Key Vault for Secrets Management
resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: take(keyVaultName, 24)
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
  }
}

// Azure Data Factory
resource dataFactory 'Microsoft.DataFactory/factories@2018-06-01' = {
  name: take(adfName, 63)
  location: location
  identity: {
    type: 'SystemAssigned'
  }
}

output storageAccountName string = storageAccount.name
output keyVaultName string = keyVault.name
output dataFactoryName string = dataFactory.name
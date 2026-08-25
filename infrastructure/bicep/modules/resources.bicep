@description('Azure regionen hvor ressourcerne oprettes')
param location string

@description('Præfiks til ressourcenavne')
param resourcePrefix string = 'nrg'

@description('Unik suffix til ressourcenavne')
param uniqueSuffix string = uniqueString(resourceGroup().id)

// Garanterer gyldige navnelængder (min 3, max 24 tegn)
var fullStorageName = '${resourcePrefix}st${uniqueSuffix}'
var storageAccountName = take('${fullStorageName}123', 24)

var fullKvName = '${resourcePrefix}-kv-${uniqueSuffix}'
var keyVaultName = take('${fullKvName}-123', 24)

// ------------------------------------------------------------------
// 1. ADLS Gen2 Storage Account (Hierarchical Namespace enabled)
// ------------------------------------------------------------------
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true // Aktiverer HNS for ADLS Gen2
    accessTier: 'Hot'
    supportsHttpsTrafficOnly: true
    minimumTlsVersion: 'TLS1_2'
  }
}

// Blob Services
resource blobServices 'Microsoft.Storage/storageAccounts/blobServices@2023-01-01' = {
  parent: storageAccount
  name: 'default'
}

// ------------------------------------------------------------------
// 2. Data Lake Containers (raw, cleansed, curated)
// ------------------------------------------------------------------
resource rawContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  parent: blobServices
  name: 'raw'
  properties: {
    publicAccess: 'None'
  }
}

resource cleansedContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  parent: blobServices
  name: 'cleansed'
  properties: {
    publicAccess: 'None'
  }
}

resource curatedContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  parent: blobServices
  name: 'curated'
  properties: {
    publicAccess: 'None'
  }
}

// ------------------------------------------------------------------
// 3. Azure Key Vault & Secrets
// ------------------------------------------------------------------
resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: keyVaultName
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    enableSoftDelete: true
    softDeleteRetentionInDays: 7
    enableRbacAuthorization: true
  }
}

// Gem Storage Connection String sikkert i Key Vault
resource storageConnectionStringSecret 'Microsoft.KeyVault/vaults/secrets@2023-07-01' = {
  parent: keyVault
  name: 'storage-connection-string'
  properties: {
    value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccount.name};AccountKey=${storageAccount.listKeys().keys[0].value};EndpointSuffix=${environment().suffixes.storage}'
  }
}

// Outputs
output storageAccountName string = storageAccount.name
output keyVaultName string = keyVault.name

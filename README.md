
## Provision resources

Run this command to create a resource group:
```
az group create --name <resource-group-name> --location eastus
```

Run this command to get your user object id:
```
az ad signed-in-user show --query id -o tsv
```

Run the following command:
```
az deployment group create --resource-group <resource-group-name> --template-file basic-setup.bicep
```

Provide a name for the foundry resource, and copy paste the object id from above.

```python


```
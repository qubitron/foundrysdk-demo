

## Getting Started -- Python

### Login to azure locally

Install the azure cli if you dont have it already, and run
```
az login
```

### Create and activate virtual environment

On windows
```cmd
py -3 -m venv .venv
.venv\scripts\activate
```

On mac/linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install requirements

```
pip install -r requirements.txt
```

### Provision resources

Pick a name for your foundry resource, and run the python provisioning script:
```python
python provision.py <foundry-resource-name>
```

### Run Sample Code

Go into the models folder:
```
cd src/models
```

Chat completion with gpt-4o
```
python chat_gpt4o.py
```

Go back to agents folder
```
cd ../agents
```

Run basic agent creation code
```
python create_agent.py
```

## Provision resources (all other languages)

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
az deployment group create --resource-group <resource-group-name> --template-file main.bicep
```

Provide a name for the foundry resource, and copy paste the object id from above.

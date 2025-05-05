

## Getting Started: Python

### Login to azure locally

Install the azure cli if you dont have it already, and run:
```
az login
```

Make sure to set the correct subscription for the azure cli:
```
az account set --subscription "<subscription-id-or-name>"
```

NOTE: if you run into authentication issues, try running ```az logout``` and run the above steps again

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

## Getting started: all other languages

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

See the spreadsheet [here](https://microsoft-my.sharepoint.com/:x:/p/dcohen/ERELir8hvLJGg8uFmaETBYUB5JUOYyAxpE0VaocwpM-cEw?e=nZF3NA&nav=MTVfe0M2MDcyMkYyLUYwOTItNEQ1OC1CMzYyLTFFOTM4NUU4MDFFOH0) for SDK samples and package installation instructions for your language (don't forget to scroll right!).

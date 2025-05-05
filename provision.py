import subprocess
import json
import argparse

def run_cli(cmd):
    """Run an Azure CLI command and return the output."""
    print(f"Running command: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        exit(1)
    return result.stdout

if __name__ == "__main__":
    # Constants
    bicep_file = "main.bicep"

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Provision Azure resources using Bicep.")
    parser.add_argument("foundry_resource", help="The name of the Foundry resource.")
    parser.add_argument("--location", help="The name of the Foundry resource.", default="eastus", required=False)
    parser.add_argument("--resource_group", help="The name of an existing resource group (optional).", required=False)
    args = parser.parse_args()

    # Assign arguments to variables
    foundry_resource_name = args.foundry_resource
    resource_group = args.resource_group
    location = args.location
    project_name = foundry_resource_name

    print("Retrieving logged in user's object ID...")
    object_id = run_cli(f"az ad signed-in-user show --query id -o tsv")
    
    new_resource_group = resource_group is None
    if new_resource_group:
        resource_group = f"{foundry_resource_name}-rg"
        run_cli(f"az group create --name {resource_group} --location {location}")

    print("Deploying Bicep template...")
    run_cli(f"az deployment group create --name {foundry_resource_name}-bicep "
            f"--resource-group {resource_group} --template-file {bicep_file} "
            f"--parameters foundryResourceName={foundry_resource_name} location={location} userObjectId={object_id}")
    
    # Write the resource group name to an .env file
    with open(".env", "w") as env_file:
        env_file.write(f"AZURE_AI_PROJECT_ENDPOINT=https://{foundry_resource_name}.services.ai.azure.com/api/projects/{foundry_resource_name}\n")
    
# CSV Dynamic Inventory Plugin

Together we will review and prep the script:
> [create-csv-inventory_bt.py](https://raw.githubusercontent.com/r3dact3d/AnsibleProject/refs/heads/development/playbooks/development/create-csv-inventory_bt.py)

- Ensure that the inventory.csv file has a hostname column and a group column

- Or, update the code to reflect the columns in the inventory.csv file that represent the hostname and group.


## Steps:

1.** Upload the Script and CSV to Source Control:** Place both your modified Python script (e.g., create_csv_inventory_bt.py) and your inventory.csv file into a Source Control Management (SCM) repository (like Git) that your AAP project can access.
2. **Ensure Executable Permissions:** Make sure your create_csv_inventory_bt.py script has executable permissions (chmod +x) in your SCM repository. Otherwise, the Automation Controller will report a "Permission denied" error during execution.
3. **Create an Inventory in AAP:** Navigate to "Automation Execution" -> "Infrastructure" -> "Inventories" in the Automation Controller UI and create a new Inventory.
4. **Add an Inventory Source:** Within your newly created Inventory, go to the "Sources" tab and click "Create source".
5.**** Configure the Source Type: Select "Sourced from a Project" as the source type.
6. **Specify Project and Script:**
Choose the Project in AAP that is synchronized with your SCM repository.
- In the "Inventory file" field, select or type the relative path to your create_csv_inventory_bt.py script within your project's root directory.
7. **Pass the CSV Path via Source Variables:** In the "Source variables" field, you can specify the environment variable that your Python script expects to find the CSV path. 
- Enter this using YAML or JSON syntax.
> Example (YAML for Source Variables field):
> - (Replace "path/to/your/inventory.csv" with the actual relative path to your CSV file within your SCM project).
8. **Save and Sync:** Save the Inventory Source configuration. An update of the project will automatically trigger an inventory update where it is used. You can also manually sync the source.

This method ensures that your Python script receives the correct inventory.csv path from AAP without being hardcoded, making your automation more flexible and reusable.

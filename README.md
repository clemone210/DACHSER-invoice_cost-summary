# DACHSER invoice - cost summary

This repository/code is designed to give a quick overview of the actual cost of a shipment.

The code extracts all costs based on the order number and outputs them in a file with two sheets.
Sheet 1 contains all shipments (based on the reference) and lists all corresponding cost service types and their amount.
Sheet 2 contains all the shipments (based on the reference) and lists the sum of all the costs, so you have an overview of the total cost of the shipment.

You can place any number of invoice files into the "invoice" directory within this repository and receive one output file.

## How to use?

1. Open Windows Powershell and install git by using the following command:

	`winget install git` 

2.  Clone this repository

	`git clone https://github.com/clemone210/DACHSER-invoice_cost-summary.git`

3. Install Python on Windows by using this guide:  [install_python.md](https://github.com/clemone210/DACHSER-invoice_cost-summary/blob/d5cd11113221acf25388fa008caaaa46fba62fb2/install_python.md)

4. Install the dependencies

	`pip install -r requirements.txt`

5. Download the invoices from [eLogistics](https://elogistics.dachser.com/downloads/index?0) as a **.csv** file.
6. Create a new folder called "invoices" in the repository root directory.
7. Move all the downloaded invoices into the "invoices" folder.
8. Run a Powershell shell from the repository folder

	`python main.py` or `python3 main.py`

9. You should now have your shipment data in the repository directory.

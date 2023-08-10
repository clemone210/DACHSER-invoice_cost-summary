# DACHSER invoice - cost summary

This repository / code is intended to get quickly an overview of the actual cost of a shipment.

The code will extract all the cost based on the order number and output them into a file with two sheets.
Sheet 1 contains all shipments (based on the reference) and lists all its corresponding cost service types and their amount.
Sheet 2 contains all shipments (based on the reference) and list the sum of all the costs, so you have a overview of the total cost of the shipment.

You can put as many invoice files into the "invoice" directory within this repository and receive one output file.

## How to use?

1. Open Windows Powershell and install git by using the following command:

	`winget install git` 

2.  Clone this repository

	`git clone https://github.com/clemone210/DACHSER-invoice_cost-summary.git`

3. Install Python on Windows by using this guide:  [install_python.md](https://github.com/clemone210/DACHSER-invoice_cost-summary/blob/d5cd11113221acf25388fa008caaaa46fba62fb2/install_python.md)

4.	Install the dependencies

	`pip install -r requirements.txt`

5. Download the invoices from [eLogistics](https://elogistics.dachser.com/downloads/index?0) as **.csv** file.
6. Move all downloaded invoices into the "invoices" folder within this repository folder
7. Run a Powershell from the repository folder

	`python main.py` or `python3 main.py`

8. You should now have your shipment data in the repository directory.

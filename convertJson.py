import csv, json

print('start...')

def paseHeader(headerCSV):
    # Open the CSV
    f = open( headerCSV, 'r' )

    reader = csv.DictReader( f, fieldnames = ( "DocTaxNo","TaxDate","TaxRate","TransNo", "CreditTerm", 
            "TaxNo", "CompanyName", "Branch", "Address1", "Address2", "Address3", "PostNo", "DeliveryName", "DeliveryAddress1", "DeliveryAddress2", "DeliveryAddress3",
            "PackingNo", "PackingType", "PackingPackage", "DeliveryNo", "DeliverySeq", "InvoiceNo", "InvoiceSeq", "DeliveryQty", "PurchaseNo", "PurchaseType",
                    "PartNo", "PartType", "PartName", "Retail", "Price", "Discount"
       ))
    framenames = []
    storeHeader = []

    # header frame names in a list
    for row in reader:
        header= {"docTaxNo":row["DocTaxNo"], 
        "taxDate": row["TaxDate"],
        "taxRate": row["TaxRate"],
        "transNo": row["TransNo"],
        "creditTerm": row["CreditTerm"],
        "customer":[],
        "invoiceDetail":[]}
        if row["DocTaxNo"] not in framenames:
            framenames.append(row["DocTaxNo"])
            storeHeader.append(header)

    # Create Objects for Header, customer, Detial and article
    customer = {"taxNo":""}
    invoiceDetail = {"PackingNo": ""}
    for header in storeHeader:
        f = open( headerCSV, 'r' )
        reader = csv.DictReader( f, fieldnames = ("DocTaxNo","TaxDate","TaxRate","TransNo", "CreditTerm", 
            "TaxNo", "CompanyName", "Branch", "Address1", "Address2", "Address3", "PostNo", "DeliveryName", "DeliveryAddress1", "DeliveryAddress2", "DeliveryAddress3",
            "PackingNo", "PackingType", "PackingPackage", "DeliveryNo", "DeliverySeq", "InvoiceNo", "InvoiceSeq", "DeliveryQty", "PurchaseNo", "PurchaseType",
                    "PartNo", "PartType", "PartName", "Retail", "Price", "Discount"))
        for row in reader:
            if header["docTaxNo"] == row["DocTaxNo"]:
                 if customer["taxNo"] != row["TaxNo"]:
                    customer = {
                        "taxNo":            row["TaxNo"],
                        "companyName":      row["CompanyName"],
                        "branch":           row["Branch"],
                        "address1":         row["Address1"],
                        "address2":         row["Address2"],
                        "address3":         row["Address3"],
                        "deliveryName":     row["DeliveryName"],
                        "deliveryAddress1": row["DeliveryAddress1"],
                        "deliveryAddress2": row["DeliveryAddress2"],
                        "deliveryAddress3": row["DeliveryAddress3"]
                        }
                    header["customer"].append(customer)
                 else:
                    # if invoiceDetail["packingNo"] != row["PackingNo"]:
                    invoiceDetail = {
                        "packingNo":                row["PackingNo"], 
                        "packingType":              row["PackingType"],
                        "packingPackage":           row["PackingPackage"],
                        "deliveryNo":               row["DeliveryNo"],
                        "deliverySeq":              row["DeliverySeq"],
                        "invoiceNo":                row["InvoiceNo"],
                        "invoiceSeq":               row["InvoiceSeq"],
                        "deliveryQty":              row["DeliveryQty"],
                        "purchaseNo":               row["PurchaseNo"],
                        "purchaseType":             row["PurchaseType"],
                        "article":[{
                            "partNo":               row["PartNo"],
                            "partType":             row["PartType"],
                            "partName":             row["PartName"],
                            "retail":               row["Retail"],
                            "price":                row["Price"],
                            "discount":             row["Discount"]
                            }]
                        }
                    header["invoiceDetail"].append(invoiceDetail)
                     
            
    # Parse the CSV into JSON
    out = json.dumps(header, indent=4)
    # Save the JSON
    f = open( 'data.json', 'w')
    f.write(out)

paseHeader('jsonInvoice.csv')
print('end.....')
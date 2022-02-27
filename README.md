The script updates the catalog of the company using information sent by the supplier.

The images sent by the supplier are converted to smaller jpeg images and the text
is turned into an HTML file that shows the image and the product description. 
The contents of the HTML file is uploaded to a web service that is already running using Django.

The supplier is notified with an email that indicates the total weight of products that were uploaded. 
The email has a PDF attached with the name of the product and its total weight.

Parallel to the automation running, health_check.py  check the health of the system and send an email 
if something goes wrong. 
# What does this script do?
# READS "uscities" data set and parses California only cities and the counties they're in
# WRITES a "product_list" to be uploaded to Webflow as Products

import csv

# Define CSV file to write Product file for upload to Webflow
product_upload = open('product.csv', 'w')

    
print("Reading and writing product data")

#open CSV data file and read the file
with open('uscities.csv', 'r') as city_data:
    csv_reader = csv.reader(city_data)

    # next(csv_reader)

#create a for loop and assign usable variables
    for line in csv_reader:
        city = line[0]
        product_handle = city.replace(" ", "-")
        product_name = city + " Radius Map"
        product_type = "Advanced"
        product_desc = f"Product for {city}."
        product_categ = line[5]
        main_img_url = "https://google.com/image.jpeg"
        var_price = "300"
        shipping = "TRUE"
        tax = "Standard Automatic Tax calculation"
        state_id = line[2]
        item = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(product_handle, product_name, product_type, product_desc, product_categ, main_img_url, "", var_price, "", "", "", "", shipping, "", "", "", "", "", "", "", "", "", "", "", "")
        

# if statement to parse cities in California
        if state_id == "CA":
            #Write to CSV
            product_upload.write(item)
    
print("Closing file")
product_upload.close()
print("Product CSV File Created!")
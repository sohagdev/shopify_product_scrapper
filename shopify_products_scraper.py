import requests
import json
import pandas as pd

url = 'https://www.mamasandpapas.com/products.json?limit=250&page=10'

r = requests.get(url)
data = r.json()

product_list = []

for item in data['products']:
    handle = item['handle']
    title = item['title']
    bodyHtml = item['body_html']
    vendor = item['vendor']
    product_type = item['product_type']
    published = 'True'  # Assuming you want to set it to 'True' for all products

    for tag in item['tags']:
        tags = tag

    images = [image['src'] for image in item.get('images', [])]

    for variant in item['variants']:
        option1Value = variant.get('option1', '')
        option2Value = variant.get('option2', '')
        sku = variant['sku']
        grams = variant['grams']
        price = variant['price']
        requireShipping = variant['requires_shipping']
        taxable = variant['taxable']

        for image in images:
            product = {
                'Handle': handle,
                'Title': title,
                'Body (HTML)': bodyHtml,
                'Vendor': vendor,
                'Product Category': '',
                'Type': product_type,
                'Tags': tags,
                'Published': published,
                'Option1 Name': 'Size',
                'Option1 Value': option1Value,
                'Option2 Name': '',
                'Option2 Value': option2Value,
                'Option3 Name': '',
                'Option3 Value': '',
                'Variant SKU': sku,
                'Variant Grams': grams,
                'Variant Inventory Tracker': '',
                'Variant Inventory Qty': '',
                'Variant Inventory Policy': 'deny',
                'Variant Fulfillment Service': 'manual',
                'Variant Price': price,
                'Variant Compare At Price': '',
                'Variant Requires Shipping': requireShipping,
                'Variant Taxable': taxable,
                'Variant Barcode': '',
                'Image Src': image,
                'Status': 'active'
            }

            product_list.append(product)

df = pd.DataFrame(product_list)
df.to_csv('littleChamp_ten.csv', index=False)
print('Saved to file')


# this is what's possible and I will have to become someone who can withstand any kind of situation and any kind of pain and suffering for the rest of my life.
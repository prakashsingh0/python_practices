# file = open("ATower.txt", "r")

# contents = file.read().replace('|','').replace('--','').replace('Switch','').replace('Relay','').replace('""','').replace('\n\n','').replace('=','').replace('  ','')

# contents = contents.split('Version')
# file.close()

# for content in contents:
    

#     start_with_floor = content.find('FLOOR"')
#     end_with_equals = content.find('Zeus-D',start_with_floor)

    
#     text = content[start_with_floor+6:end_with_equals ]
#     print(text)
    


from pypdf import PdfReader

reader = PdfReader("DC-1.pdf")
text = ""

# Extract text from PDF
for page in reader.pages:
    extracted = page.extract_text()
    if extracted:  # avoid NoneType error
        text += extracted

# Clean text
contents = text.replace('|','').replace('--','').replace('Switch','') \
               .replace('Relay','').replace('""','') \
               .replace('\n\n','').replace('=','').replace('  ','')

contents = contents.split('Version')

# Open output file
with open("DC-1.txt", "w", encoding="utf-8") as output_file:

    for content in contents:
        start_with_floor = content.find('Slots"')
        end_with_equals = content.find('Zeus-D', start_with_floor)

        # Make sure both values exist
        if start_with_floor != -1 and end_with_equals != -1:
            result = content[start_with_floor+6:end_with_equals]
            output_file.write(result.strip() + "\n")

print("Done! Data written to output.txt")


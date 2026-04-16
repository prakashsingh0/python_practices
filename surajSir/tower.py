import csv
import re
from pypdf import PdfReader
import os

# Input file
input_file = input("Enter PDF file name: ").strip()

if not os.path.exists(input_file):
    print("❌ File not found")
    exit()

# Read PDF
reader = PdfReader(input_file)
text = ""

for page in reader.pages:
    t = page.extract_text()
    if t:
        text += t + "\n"

lines = text.split("\n")

# Output CSV
output_file = os.path.splitext(input_file)[0] + ".csv"

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    # Header
    writer.writerow(["Address", "Device", "Loop", "Tower", "Description"])

    count = 0

    for line in lines:
        line = line.strip()

        # Clean unwanted symbols
        line = line.replace("|", "").replace("--", "").strip()

        # Match valid device lines
        match = re.search(r'(\d+:\d+-\d+)\s+([A-Z0-9\-/]+)\s+"([^"]+)"', line)

        if match:
            address = match.group(1)
            device = match.group(2)
            desc = match.group(3)

            # Extract Tower & Loop
            parts = desc.split("/")
            tower = parts[0] if len(parts) > 0 else ""
            loop = parts[1] if len(parts) > 1 else ""

            writer.writerow([address, device, loop, tower, desc])
            count += 1

print(f"✅ Done! Extracted {count} rows into {output_file}")
# Updated main_script.py

import asyncio
from TruecallerApiFunctions import search_phonenumber

async def fetch_details_from_file(filename, output_file):
    try:
        with open(filename, 'r') as file:
            phone_numbers = file.read().splitlines()

        country_code = input("Enter the country code: ")
        installation_id = 'a1i04--lJ4wiWkSFpWkitpsBvziJgWa5jqtTMwDMGclLmsCCciMdejfoQ7AOuEbJ'  # Replace with your Truecaller installation ID

        results = []  # Store results for later writing to a file

        for phone_number in phone_numbers:
            result = await search_phonenumber(phone_number, country_code, installation_id)
            print(f"Details for phone number {phone_number}:")
            print(result)
            print("=" * 30)
            results.append(f"Details for phone number {phone_number}:\n{result}\n{'=' * 30}\n")

        # Save results to a file
        with open(output_file, 'w') as output:
            output.writelines(results)
        print(f"Results saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Get the filename and output file from the user
filename = input("Enter the filename containing phone numbers: ")
output_file = input("Enter the output filename: ")

# Run the event loop to execute the asynchronous function
asyncio.run(fetch_details_from_file(filename, output_file))

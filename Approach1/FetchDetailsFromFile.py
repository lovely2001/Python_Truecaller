# main_script.py

import asyncio
from TruecallerApiFunctions import search_phonenumber

async def fetch_details_from_user():
    phone_number = input("Enter the phone number: ")
    country_code = input("Enter the country code: ")
    installation_id = 'a1i04--lJ4wiWkSFpWkitpsBvziJgWa5jqtTMwDMGclLmsCCciMdejfoQ7AOuEbJ'  # Replace with your Truecaller installation ID

    result = await search_phonenumber(phone_number, country_code, installation_id)

    print(result)

# Run the event loop to execute the asynchronous function
asyncio.run(fetch_details_from_user())

import asyncio
from TruecallerApiFunctions import search_phonenumber

async def fetch_details_from_user():
    # Prompt user for input
    phone_number = input("Enter the phone number: ")
    country_code = input("Enter the country code: ")
    installation_id = 'a1i0B--lJHUYnFckvSnrGVLtxhpEqmQDqpIS3fq7Cu9Pn02sLSDJ4-L5S7APgPwQ'
    
    result = await search_phonenumber(phone_number, country_code, installation_id)
    print(result)

# Run the asynchronous function
asyncio.run(fetch_details_from_user())
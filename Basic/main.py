import asyncio
from truecallerpy import search_phonenumber

phone_number = "6395339208"
country_code = "IN"
installation_id = "a1i04--lJ4wiWkSFpWkitpsBvziJgWa5jqtTMwDMGclLmsCCciMdejfoQ7AOuEbJ"

response = asyncio.run(search_phonenumber(phone_number, country_code, installation_id))
print(response)
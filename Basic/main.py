import asyncio
from truecallerpy import search_phonenumber

phone_number = "6395339208"
country_code = "IN"
installation_id = "a1i0B--lJHUYnFckvSnrGVLtxhpEqmQDqpIS3fq7Cu9Pn02sLSDJ4-L5S7APgPwQ"

response = asyncio.run(search_phonenumber(phone_number, country_code, installation_id))
print(response)
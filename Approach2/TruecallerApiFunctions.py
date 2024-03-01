import httpx
from phonenumbers import parse, NumberParseException

async def search_phonenumber(phoneNumber, countryCode, installationId):
    
    try:
        full_phone_number = f"{countryCode}{phoneNumber}"
        phone_number = parse(full_phone_number, None)
        significant_number = phone_number.national_number
    except NumberParseException as e:
        return {
            "status_code": None,
            "error": "Invalid Phone Number",
            "message": str(e)
        }

    headers = {
        "content-type": "application/json; charset=UTF-8",
        "accept-encoding": "gzip",
        "user-agent": "Truecaller/11.75.5 (Android;10)",
        "Authorization": f"Bearer {installationId}"
    }
    params = {
        "q": str(significant_number),
        "countryCode": phone_number.country_code,
        "type": 4,
        "locAddr": "",
        "placement": "SEARCHRESULTS,HISTORY,DETAILS",
        "encoding": "json"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://search5-noneu.truecaller.com/v2/search", params=params, headers=headers
            )

        response.raise_for_status()

        # Extract relevant information from the Truecaller API response
        api_data = response.json()

        # Try to find user information in different possible keys
        user_data = (
            api_data.get('user_info') or
            api_data.get('result') or
            api_data.get('data') or
            (api_data.get('users', [{}])[0] if 'users' in api_data else {})  # Check if 'users' is present
        )

        # If user_data is a list, take the first element
        if isinstance(user_data, list):
            user_data = user_data[0]

        # Extract specific details (name, address, carrierservice)
        name = user_data.get('name', 'N/A')
        addresses = user_data.get('addresses', 'N/A')  # Adjust 'address' to the actual key in your API response

        # Print the specific details
        print("Name:", name)
        print("Addresses:", addresses)

        return {
            "name": name,
            "address": addresses
        }

    except httpx.HTTPError as exc:
        error_message = "An HTTP error occurred: " + str(exc)
        return {
            "status_code": exc.response.status_code if hasattr(exc, "response") else None,
            "error": "HTTP Error",
            "message": error_message
        }
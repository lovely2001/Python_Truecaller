import httpx
from phonenumbers import parse, NumberParseException

async def search_phonenumber(phoneNumber, countryCode, installationId):
    try:
        # Parse and validate the provided phone number
        full_phone_number = f"{countryCode}{phoneNumber}"
        phone_number = parse(full_phone_number, None)
    except NumberParseException as e:
        return {"error": "Invalid Phone Number", "message": str(e)}

    # Set up headers and parameters for the Truecaller API
    headers = {
        "content-type": "application/json; charset=UTF-8",
        "user-agent": "Truecaller/11.75.5 (Android;10)",
        "Authorization": f"Bearer {installationId}"
    }
    params = {
        "q": phone_number.national_number,
        "countryCode": phone_number.country_code,
        "type": 4,
        "placement": "SEARCHRESULTS,HISTORY,DETAILS",
        "encoding": "json"
    }

    try:
        # Make an asynchronous request to the Truecaller API
        async with httpx.AsyncClient() as client:
            response = await client.get("https://search5-noneu.truecaller.com/v2/search", params=params, headers=headers)

        response.raise_for_status()

        # Extract relevant information from the Truecaller API response
        api_data = response.json()

        # Extract user information considering different possible keys
        user_data = api_data.get('user_info', api_data.get('result', api_data.get('data', api_data.get('users', [{}])[0])))
        user_data = user_data[0] if isinstance(user_data, list) else user_data

        # Extract specific details (name, address)
        name = user_data.get('name', 'N/A')
        addresses = user_data.get('addresses', 'N/A')
        return {"name": name, "address": addresses}

    except httpx.HTTPError as exc:
        # Handle HTTP errors
        error_message = "An HTTP error occurred: " + str(exc)
        return {"error": "HTTP Error", "message": error_message}
import json

# import requests


def lambda_handler(event, context):
    num_to_letter = {
        '0': ['0'],
        '1': ['1'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'n', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z'],
    }

    phone_num = event['Details']['ContactData']['CustomerEndpoint']['Address']
    contact_id = event['Details']['ContactData']['ContactId']
    country_code = phone_num[0] + phone_num[1]
    digits = str(phone_num[2: ])

    def vanity_1(digits):
        option_1 = ''

        if len(digits) != 10:
            return 'false'
        else:
            for ele in digits:
                option_1 += num_to_letter[ele][0]
        return option_1

    check = vanity_1(digits)

    print(f'option 1 for vanity {check} phone num is {digits}, country code {country_code} and contact ID is {contact_id}')
    resultMap = {'option_one': check}
    return resultMap

    # {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "hello world",
    #         # "location": ip.text.replace("\n", "")
    #     }),
    # }


# Use this terminal command to test the function
# sam local invoke -e /root/projects/python/voiceFoundry-assessment/voiceFoundry-lambda/events/event.json HelloWorldFunction

# Make sure to run below after each change prior to invoking the event
# sam build

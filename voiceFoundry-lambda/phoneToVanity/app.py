import json

# import requests

# Dict that has a list of letters for each number
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

def lambda_handler(event, context):

    # Extract data from the event (the event occurs when the incoming call invokes the lambda func in the contact flow)
    phone_num = event['Details']['ContactData']['CustomerEndpoint']['Address']
    contact_id = event['Details']['ContactData']['ContactId']
    country_code = phone_num[0] + phone_num[1]
    # This variable formats the phone number so the country code is removed and turns the int into string (return value must be a string)
    digits = str(phone_num[2: ])

    option_1 = vanity_1(digits)

    print(f'option 1 for vanity {option_1} phone num is {digits}, country code {country_code} and contact ID is {contact_id}')
    resultMap = {'option_one': option_1}
    return resultMap


# Function that takes in a phone number and returns the option_1 vanity number for the contact flow
def vanity_1(phone_num):
    option_1 = ''

    if len(phone_num) != 10:
        return 'false'
    else:
        for ele in phone_num:
            option_1 += num_to_letter[ele][0]
    return option_1

def vanity_2(phone_num):
    option_2 = ''

    return option_2

def vanity_3(phone_num):
    option_3 = ''

    return option_3

def vanity_4(phone_num):
    option_4 = ''

    return option_4

def vanity_5(phone_num):
    option_5 = ''

    return option_5

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

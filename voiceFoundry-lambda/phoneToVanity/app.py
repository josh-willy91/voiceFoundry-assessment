import json
# import requests

# note that the below 3 lines should be commented out if trying to invoke an event in console for testing
# import boto3
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('voiceFoundry')

# Dict that has a list of letters for each number
num_to_letter = {
    '0': ['0', '0', '0'],
    '1': ['1', '1', '1'],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
}

# array of common three letter words
threeLetterWords = ["the","and","for","are","but","not","you","all","any","can","had","her","was","one","our","out","day","get","has","him","his","how","man","new","now","old","see","two","way","who","boy","did","its","let","put","say","she","too","use"]


def lambda_handler(event, context):

    # Extract data from the event (the event occurs when the incoming call invokes the lambda func in the contact flow)
    phone_num = event['Details']['ContactData']['CustomerEndpoint']['Address']
    contact_id = event['Details']['ContactData']['ContactId']

    # This variable formats the phone number so the country code is removed and turns the int into string (return value must be a string)
    digits = str(phone_num[2: ])

    option_1 = vanity_1(digits)
    option_2 = vanity_2(digits)
    option_3 = vanity_3(digits)
    option_4 = vanity_4(digits)
    option_5 = vanity_5(digits)

    # note that the below line should be commented out if trying to invoke an event in console for testing
    # dynamodb_put(digits, contact_id, option_1, option_2, option_3, option_4, option_5)

    resultMap = {'option_one': option_1, 'option_two': option_2, 'option_three': option_3, 'option_four': option_4 ,'option_five': option_5}
    return resultMap


# function that adds an item in dynamoDB
# Note that this should be commented out if trying to invoke an event for testing in console
# def dynamodb_put(digits, contact_id, option_1, option_2, option_3, option_4, option_5):
#     table.put_item(
#         Item = {
#             "id": contact_id,
#             "phoneNumber": digits,
#             "vanityOption1": option_1,
#             "vanityOption2": option_2,
#             "vanityOption3": option_3,
#             "vanityOption4": option_4,
#             "vanityOption5": option_5
#         }
#     )


# Function that takes in a phone number and returns the option_1 vanity number for the contact flow
# This option is completely random and has a low chance of coming up with a good vanity number
def vanity_1(phone_num):
    option_1 = ''

    for num in phone_num:
        option_1 += num_to_letter[num][0]

    return option_1


# Function that takes a phone number and tries to find a possible combo of 3 digits that matches one of the 3 letter words in the array
# I thought this would be the best option but I wasn't able to reduce the time complexity enough to make it viable.  Lambda's time out after 3 secs
def vanity_2(phone_num):
    option_2 = '1888 hire me'

    # *****Note****** The belwo comments were going to try to match a three letter word but due to time complexity of O(n²) the lambda times out after 3secs to it's no good...
    # first_three = phone_num[0: 3]
    # second_three = phone_num[3: 6]
    # last_four = phone_num[6: ]

    # matching_words = []
    # i = 0
    # j = 1
    # k = 2

    # helper func to find any potential words that are matching a set of 3 digits
    # def match_ltrs(array_of_digits, words_array, index):
    #     matching_words = []
    #     for word in words_array:
    #         first_ltr = word[index]
    #         ltr_array = num_to_letter[array_of_digits[index]]
    #         for ltr in ltr_array:
    #             if ltr == first_ltr.upper():
    #                 matching_words.append(word)

    # match_ltrs(first_three, threeLetterWords, i)
    # match_ltrs(first_three, matching_words, j)
    # match_ltrs(first_three, matching_words, k)
    # print(matching_words, '==========matching words======================')

    return option_2


# Function that takes in a phone number and returns the option_3 vanity number for the contact flow
# This option is completely random and has a low chance of coming up with a good vanity number
def vanity_3(phone_num):
    option_3 = ''

    for ele in phone_num:
        option_3 += num_to_letter[ele][1]

    return option_3


# Function that takes in a phone number and returns the option_4 vanity number for the contact flow
# This option is completely random and has a low chance of coming up with a good vanity number
def vanity_4(phone_num):
    option_4 = ''

    for ele in phone_num:
        option_4 += num_to_letter[ele][2]

    return option_4


# function to find matching nums and push same ltrs into vanity option else will push a numbers
# this function could be best if the number has many repeated numbers like 407-888-3322 which would be 407-TTT-DDAA
def vanity_5(phone_num):
    option_5 = ''
    i = 0

    while i < 10:
        num = phone_num[i]
        if i == 9 and num == phone_num[i - 1]:
            option_5 += num_to_letter[num][0]
            i += 1

        elif i < 9 and num == phone_num[i + 1]:
            option_5 += num_to_letter[num][0]
            i += 1
        else:
            option_5 += num
            i += 1

    return option_5



# Use this terminal command to test the function
# sam local invoke -e /root/projects/python/voiceFoundry-assessment/voiceFoundry-lambda/events/event.json HelloWorldFunction

# Make sure to run below after each change prior to invoking the event
# sam build

# Use this to deploy all changes in file to AWS lambda. Should alway run sam build prior
# sam deploy

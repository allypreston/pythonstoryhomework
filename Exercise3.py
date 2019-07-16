# create a list with 10 future clients for sparta
# access at least 4 clients with a nice sentence
list_of_clients = ['MD PLC', 'Irrigation systems LTD', 'BO', 'Ireland enterprises', 'Earthport', 'Sparta global', 'Crown court justice', 'Google', 'direct line', 'home office']

print(list_of_clients[0] + list_of_clients[1])
print(f"{list_of_clients[3]} needs additional people and will require Adam to choose another person")
print(f"{list_of_clients[1]} have pulled out the deal")
print(f"{list_of_clients[8]} has failed to submit form 10J")
print(list_of_clients[7] + ' ' + list_of_clients[2])
print(f"We have had an issue with {list_of_clients[5]} and need to renegotiate contract")
print(list_of_clients[9] + " have agreed to take 4 spartans")
print(list_of_clients[1] + "has accepted 4 spartans :)" )
print("There has been a merger between " + list_of_clients[3] + " and " + list_of_clients[1] + ", they require additional spartans ")

# part 2 create a hash / dictionary that contains a story
# it should have at least 3 sections
# print the story in an orderly fashion

story = {
    'beginning': "Once upon a time there was a DevOps class.",
    'middle': "They were having fun with python.",
    'end':"Then they all got placed to go to Ireland."
}
input_keys = {
    'key1': 'do you want to hear a story y/n > ',
    'key2': 'do you want to continue y/n > ',
    'key3': 'do you want to hear the end y/n > '
}
input1 = input(input_keys['key1'])
if input1 == 'y':
    print(story['beginning'])
    input2 = input(story['key2'])
    if input2 == 'y':
        print(story['middle'])
        input3 = input(story['key3'])
        if input3 == 'y':
            print(story['end'])
        else:
            print("we'll finish later then")
    else:
        print("true it probably wasn't an overly long story")
else:
    print('very well, maybe another time')


Story = {
    'beginning': 'Hark there stranger, I need to deliver the message to the king about the dragon that just flew over this here castle, but alas my eyes are old and grey, can you tell me what colour the dragon was?',
    'middle1': 'ah indeed, just as we feared, a ',
    'middle2': ' dragon, we have known they have been returning. Tell me stranger, which way did it head?',
    'end': "? towards the castle, then we haven't a moment to lose, follow me, we have to warn the crown"
}
print(Story['beginning'])
usercolour = input('The dragons colour was ...')
print(Story['middle1'] + usercolour + Story['middle2'])
userdirection = input('The dragon was heading...')
print(Story[userdirection + 'end'])
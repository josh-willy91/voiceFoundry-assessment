



# Voice Foundry Technical Assessment
## Date 11/01/2021 - Josh Williams

### Link to Connect's contact flow
https://voicefoundry-project.my.connect.aws/
username: admin
password: Password#1

Bonus:
Phone number for call center: 302-551-6388

## Notes and Reflections
    DEFINING VANITY RESULTS - After thinking over it, I decided that the best vanity number was one that was memorable.  The best 2 options I could think of were if the number had multiple numbers repeating, then convering those repeated number into the same letters.  If the number did not have any repeated numbers then I will try to match any 3 digit series to a 3 letter word.  After that the other 3 functions just return a random collection of letters.

    CHALLENGES - I did not have any experience with the aws services of lamdba functions, dynamoDB, or Connect.  AWS had really good documentation but there was so much it got overwhelming at times.  The majority of my time was spent in creating and integrating lambda, dynamodb, and connect contact flows so I didn't spend as much time as I wanted on coming up with better vanity conversion functions.  I was disappointed that I didn't end up improving the time compexity of vanity_2 to get it to work.

    SHORTCUTS - I used the SAM Cli with the AWS Cli but I skimmed through the documentation and don't know it well.  I ran into an issue with the SAM deploy cli but I opted to just cut and paste the function into lambda instead of figuring out the issues with the sam deploy error.

    IMPROVEMENTS - Fixing vanity_2 so it runs faster and coming up with more/better vanity options.


Deliverables
1.           Git Repo with all code and documentation
2.           BONUS - a working Amazon Connect phone number to test in your environment :-)

Exercise
1.           Create a Lambda that converts phone numbers to vanity numbers and save the best 5 resulting vanity numbers and the caller's number in a DynamoDB table. "Best" is defined as you see fit - explain your thoughts.
2.           Create an Amazon Connect contact flow that looks at the caller's phone number and says the 3 vanity possibilities that come back from the Lambda function.
3.          Writing and Documentation

    -          Record your reasons for implementing the solution the way you did, struggles you faced and problems you overcame.

    -          What shortcuts did you take that would be a bad practice in production?

    -          What would you have done with more time? We know you have a life. :-)

Show off. This is your chance to demonstrate your ability to learn, Google, and figure it out. Do your best to express your areas of expertise and ability.

print('Welcome to Garhy.com, please create an account!')
users_email=input('Please enter an Email!:')
while True:
    if '@gmail' in users_email or '@hotmail'in users_email or 'outlook'in users_email :
        break
    elif len(users_email)<8:
        print('Invalid Email')
        users_email=input('Please enter a valid Email!:')
    else:
        print('Please enter a valid Email containing "gmail.com", "@hotmail.com", or "@outlook.com".')
        users_email=input('Please enter an Email!:')

print('Thank you, now for the password')
print('Password must contain an uppercase,lowercase,number and a special charcter such as #,@,&,* ')
users_pass=input('Please create a password:')
while True:
    if len(users_pass)<9:
        print('Password must be atleast 9 characters')
        users_pass=input('Please create a valid password:')
    elif users_pass!=users_pass.capitalize():
        print('Password must contain an uppercase,lowercase,number and a special charcter such as #,@,&,* ')
        users_pass=input('Please try again!:')
    elif '@' not in users_pass and '#' not in users_pass and '&' not in users_pass and  '*' not in users_pass:
        print('Password must contain an uppercase,lowercase,number and a special charcter such as #,@,&,* ')
        users_pass=input('Please try again!:')
    elif not any(char.isdigit() for char in users_pass):
        print('Password must contain an uppercase,lowercase,number and a special charcter such as #,@,&,* ')
        users_pass=input('Please try again!:')
    else:
        break
print('Done, You can now sign in!')




    
 



     

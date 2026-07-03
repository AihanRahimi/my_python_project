import string

#information of users
name = input('name:')
password = input('password:')

name_strip=name.strip()
password_strip=password.strip()
name_list = name_strip.split()
first_name = name_list[0]
nick_name = name_list [1]
print('hello',first_name)
print('your family name is',nick_name.upper())
password_replace= password_strip.replace('a','%')
password_replace= password_replace.replace('o','%')
password_replace= password_replace.replace('e','%')
password_replace= password_replace.replace('i','%')
password_replace= password_replace.replace('u','%')
password_replace=password_replace.replace('1','+')
password_replace=password_replace.replace('2','+')
password_replace=password_replace.replace('3','+')
password_replace=password_replace.replace('4','+')
password_replace=password_replace.replace('5','+')
password_replace=password_replace.replace('6','+')
password_replace=password_replace.replace('7','+')
password_replace=password_replace.replace('8','+')
password_replace=password_replace.replace('9','+')
print('your password is:',password_replace)


""" Program that displays only the unique addresses from a list """

def remove_duplicate_emails( email_list ):
    # convert all email addresses to lowercase and add them to a set
    unique_emails = set( email.lower() for email in email_list )

    # convert the set back to a list
    unique_emails_list = list( unique_emails )

    # display the unique email addresses
    print("Unique email addresses:")
    for email in unique_emails_list:
        print(email)
# end function remove_duplicate_emails


# use the function with diferent lists
list1 = ["test@example.com", "Test@example.com", "hello@world.com", "HELLO@WORLD.COM", "user@domain.com"]
list2 = [ "admin@site.com", "admin@site.com", "Admin@Site.com", "contact@site.com"]
list3 = [ "unique@one.com", "unique@two.com", "unique@one.com", "UNIQUE@ONE.COM"]

print("List 1:")
remove_duplicate_emails(list1)
print("\nList 2:")
remove_duplicate_emails(list2)
print("\nList 3:")
remove_duplicate_emails(list3

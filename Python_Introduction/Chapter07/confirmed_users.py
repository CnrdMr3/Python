# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

populated_list = ['a', 'b', 'c', 'd']
unpopulated_list = []

while populated_list:
    current_list = populated_list.pop()
    print(f"Verifying list: {current_list.title()}")
    unpopulated_list.append(current_list)

print("\nThe following list has been confirmed:")
for unpopulated_list in current_list:
    print(unpopulated_list.title())
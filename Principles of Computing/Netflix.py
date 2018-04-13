import Netflix

try:
    # Create a new rating
    create_rating = n.post('users/*final_user_id*/ratings/title/actual/70072945', params={'rating': '5'})

    print (create_rating)
except NetflixAPIError:
    # This returns a status message if successful.
    # If it's already been rated, it will return a NetflixAPIError, code 422
    pass


# Update/Clear rating
update_rating = n.put('users/*final_user_id*/ratings/title/actual/70072945', params={'rating': 'no_opinion'})

print (update_rating)

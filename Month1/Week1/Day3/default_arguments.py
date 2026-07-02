#6. Write a function with a default argument, and add a comment explaining why mutable default arguments (like a list) are risky in Python

# Function using a safe default argument (None) to avoid mutable bugs
def add_to_playlist(song_title, playlist=None):
    # In Python, default arguments are evaluated only ONCE when the function 
    # is first defined, not fresh on every call. 
    # If we used a mutable object like playlist=[] directly in the signature, 
    # Python would reuse the exact same list instance for every single call. 
    # If User A added a song, User B would unexpectedly see User A's song in 
    # their playlist because they are sharing the same memory space.
    # so we use None as a placeholder, and initialize a brand-new 
    # list inside the function scope if no playlist is provided.
    
    if playlist is None:
        playlist= []  # A fresh list is created in memory every time
        
    playlist.append(song_title)
    return playlist

#Demonstration of it working perfectly and independently
user1= add_to_playlist("espresso")
print("User 1 Playlist:", user1)  

user2 = add_to_playlist("please please please")
print("User 2 Playlist:", user2)  
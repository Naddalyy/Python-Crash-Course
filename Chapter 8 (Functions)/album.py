def make_album(artist_name, album_title, num_songs=None):
    album_dict = {'artist': artist_name.title(), 
                  'title': album_title.title(),
                  }
    if num_songs:
        album_dict['number of songs'] = num_songs
    return album_dict

# album = make_album('leprous', 'pitfalls')
# print(album)
# album = make_album('ren', 'demos vol 2.')
# print(album)
# print(make_album('porcupine tree', 'in absentia', 33))

while True:
    print("Tell me about your favorite album!")
    print("Enter 'q' to exit at any time.")
    artist = input("Artist: ").title()
    if artist.lower() == 'q':
        break
    title = input("Album Title: ").title()
    if title.lower() == 'q':
        break
    album = make_album(artist, title)
    print(album)
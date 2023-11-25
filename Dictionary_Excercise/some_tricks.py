some_dict = {"mp3": ['song1', 'song2', 'song3'], \
             "mp4": ['song1', 'song2', 'song3'],
             "video": ['video1', 'video2', 'video3']}

for key, value in some_dict.items():
    print(key, value)

for key in some_dict.keys():
    print(key)

for key, value in some_dict.values():
    print(key)
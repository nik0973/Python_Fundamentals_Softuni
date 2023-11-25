world_ban = input().split(', ')
text = input()

for world in world_ban:
    text = text.replace(world, '*' * len(world))
print(text)

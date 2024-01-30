def bottles_of_beer(num_bottles):
    for i in range(num_bottles, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.")
        print()

# Generate all verses starting from 99 bottles
bottles_of_beer(99)
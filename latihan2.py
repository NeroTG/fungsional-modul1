

int_values = {}
float_values = ()
string_values = []
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

for items in random_list:
    if isinstance(items, int):
        # Memisahkan angka 
        ratusan = items // 100
        puluhan = (items // 10) % 10
        satuan = items % 10
        int_values[items] = (ratusan, puluhan, satuan)
    elif isinstance(items, float):
        float_values += (items,)
    elif isinstance(items, str):
        string_values.append(items)

print("Data int:")
print(int_values)

print("Data float:")
print(float_values)

print("Data string:")
print(string_values)
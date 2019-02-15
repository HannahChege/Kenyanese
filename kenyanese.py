# Make the key map
y_in = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
x_out = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
key_map = dict(zip(x_out, y_in))

# Add the missing letter 'z'
key_map['z'] = 'q'

# Make the translate tool
y_in = ''.join(key_map.values())
x_out = ''.join(key_map.keys())
key_translate = str.maketrans(y_in, x_out)

# Open input and make output files
input_file = 'A-small-practice.in'
output_file = 'A-small-practice.out'

my_file_in = open(input_file, 'r')
my_file_out = open(output_file, 'w')

# Make the list with text lines
file_list = my_file_in.readlines()

# Make the file in English
for num, line in enumerate(file_list[1:], 1):
    my_file_out.write('Case #' + str(num) + ': ' + line.translate(key_translate))

my_file_in.close()
my_file_out.close()

for i in (file_list):
    print("Case",i)
    print(file_list)



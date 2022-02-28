
def get_errors_from_log(file_name='log.txt'):
    return (line for line in open(file_name, 'r') if 'ERROR' in line)


gen = get_errors_from_log()

for line in gen:
    print(line)

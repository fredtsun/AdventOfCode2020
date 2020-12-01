def read_lines_as_list(input_path):
    with open(input_path) as f:
        data = f.read()
    return data.split('\n')

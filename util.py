def read_lines_as_list(input_path, split_pattern='\n'):
    with open(input_path) as f:
        data = f.read()
    return data.split(split_pattern) if split_pattern else data

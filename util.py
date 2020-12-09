def read_lines_as_list(input_path, split_pattern='\n'):
    if not split_pattern:
        raise Exception("Wtf dude. Just leave it alone. If you dont want it to split, use another function! Gosh!")
    with open(input_path) as f:
        data = f.read()
    return data.split(split_pattern)

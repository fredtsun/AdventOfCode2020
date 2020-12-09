from util import read_lines_as_list

class Bag(object):
    def __init__(self, s):
        self._parse(s)

    def _parse(self, s):
        '''only use this in the init function
        '''
        unparsed_bag_type, unparsed_contains = s.split('contain')
        self.bag_type = unparsed_bag_type.rstrip(' ').rstrip('bags').rstrip(' ')
        self._parse_contains_bags(unparsed_contains)

    def _parse_contains_bags(self, unparsed_contains):
        '''
        1. all of them end in periods so strip that off
        2. they will start with a space to strip that off too.
        3. split by commas, then parse the array
        '''
        self.contains_bag = {}
        # hacky shit
        if 'no other bags' in unparsed_contains:
            return
        unparsed_contains_list = [
            upc.lstrip(' ').rstrip('bags').rstrip('bag').rstrip(' ') for upc in unparsed_contains.rstrip('.').split(',')]
        for unparsed_bag in unparsed_contains_list:
            bag_type, count = self._parse_bag(unparsed_bag)

            self.contains_bag[bag_type] = count

    def _parse_bag(self, unparsed_bag):
        ptr = 0
        while unparsed_bag[ptr].isdigit():
            ptr += 1
        return unparsed_bag[ptr + 1:], int(unparsed_bag[:ptr])


def build_graph():
    input_data = read_lines_as_list('data/day7.txt')
    bags = [Bag(data) for data in input_data]
    graph = {}
    for b in bags:
        graph[b.bag_type] = list(b.contains_bag.items())
    return graph

def part1():
    graph = build_graph()
    visited = {}
    def traverse(node):
        if node in visited:
            return visited[node]
        contains_shiny_gold = False
        for next_node, _ in graph[node]:
            if next_node == 'shiny gold' or traverse(next_node): 
                contains_shiny_gold = True
                break
        visited[node] = contains_shiny_gold
        return visited[node]
    for n in graph.keys():
        traverse(n)
    return len([v for v in visited.values() if v])


def part2():
    graph = build_graph()
    visited = {}

    def traverse(node):
        if node in visited:
            return visited[node]
        num_bags = 1
        for next_node, num in graph[node]:
            num_bags += traverse(next_node) * num
        return num_bags
    return traverse('shiny gold') - 1

if __name__ == '__main__':
    print(part1())
    print(part2())
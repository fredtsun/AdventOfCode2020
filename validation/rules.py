import abc


class ValidationRule(metaclass=abc.ABCMeta):
    '''This is a class you make when you're bored and wanna overkill the implementation.
    ...and dont want to leave good comments
    ...or write tests. 
    Stuff like this will get you on the naughty list >:)

    Validate input against a set of rules after it's been parsed.
    '''
    @abc.abstractmethod
    def __call__(self, value):
        '''function used to validate the input value. returns true/false
        '''
        raise NotImplementedError


class Exists(ValidationRule):
    '''Checks if a value is present'''
    def __init__(self):
        pass

    def __call__(self, value):
        return value is not None


class Number(ValidationRule):
    '''Check to see if the number passed in abides by the rules
    '''
    def __init__(self, len=None, min=-float('inf'), max= float('inf')):
        self.len = len
        self.min = min
        self.max = max

    def __call__(self, value):
        if self.len != None and self.len != len(value):
            return False
        try:
            num = int(value)
        except:
            #log(f'{value} is not not a number')
            return False
        return self.min <= num < self.max


class Enum(ValidationRule):
    '''Checks to see if the passed in value exist in a given set
    '''
    def __init__(self, values=None):
        self.values = values or set()

    def __call__(self, value):
        return value in self.values


class CustomRule(ValidationRule):
    '''Executes a function on the input and returns the result (True/False)
    '''
    def __init__(self, fn=None):
        if not fn:
            raise Exception("No function given")
        self.fn = fn

    def __call__(self, value):
        return self.fn(value)


class Length(ValidationRule):
    '''Checks if length of passed in value equals the expected value
    '''

    def __init__(self, length):
        self.length = length

    def __call__(self, value):
        return self.length == len(value)


class ObjectRule(ValidationRule):
    '''Validates an input object (dictionary)
    '''
    def __init__(self, schema=None):
        self.schema = schema

    def __call__(self, obj):
        if self.schema is None:
            raise Exception("No schema provided")
        for field, rule in self.schema.items():
            if field not in obj or not rule(obj[field]):
                return False
        return True


class All(ValidationRule):
    '''combines multiple rules/functions, all of which must eval to be be truthy
    '''
    def __init__(self, *rules):
        self.rules = rules

    def __call__(self, obj):
        return all(r(obj) for r in self.rules)


class Switch(ValidationRule):
    '''Declarative switch statement to validate input
    '''
    def __init__(self, eval_fn, switch_config, default=None):
        self.switch_config = switch_config
        self.eval_fn = eval_fn
        self.default = default or (lambda obj: False)

    def __call__(self, obj):
        res = self.eval_fn(obj)
        fn = self.switch_config.get(res, self.default)
        return fn(obj)

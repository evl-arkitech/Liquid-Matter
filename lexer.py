import re

# Define token types
class TokenType:
    SET = 'SET'
    TO = 'TO'
    ADD = 'ADD'
    DISPLAY = 'DISPLAY'
    IDENTIFIER = 'IDENTIFIER'
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    DEFINE = 'DEFINE'
    ACTION = 'ACTION'
    END = 'END'
    PERFORM = 'PERFORM'
    WITH = 'WITH'
    INTENTIONTO = 'INTENTIONTO'
    IF = 'IF'
    IS = 'IS'
    THEN = 'THEN'
    REPEAT = 'REPEAT'
    TIMES = 'TIMES'
    COMPILE = 'COMPILE'
    TEST = 'TEST'
    PRODUCTION = 'PRODUCTION'
    CONTAINER = 'CONTAINER'
    SLASH = 'SLASH'
    COLON = 'COLON'
    PIPE = 'PIPE'
    DOUBLE_PIPE = 'DOUBLE_PIPE'
    TRIGGER = 'TRIGGER'
    OUTPUT = 'OUTPUT'
    INPUT = 'INPUT'
    OF = 'OF'
    READ = 'READ'
    WRITE = 'WRITE'
    FETCH = 'FETCH'
    INTO = 'INTO'
    FILE = 'FILE'
    SPAWN = 'SPAWN'
    AT = 'AT'
    BIND = 'BIND'
    MOVE = 'MOVE'
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    WHEN = 'WHEN'
    TOUCHES = 'TOUCHES'
    SUBTRACT = 'SUBTRACT'
    FROM = 'FROM'
    ATTEMPT = 'ATTEMPT'
    RECOVER = 'RECOVER'
    QUERY = 'QUERY'
    PARSE = 'PARSE'
    JSON = 'JSON'
    GET = 'GET'
    FOR = 'FOR'
    EACH = 'EACH'
    IN = 'IN'
    ASYNC = 'ASYNC'
    SECRET = 'SECRET'
    SECRETS = 'SECRETS'
    LOAD = 'LOAD'
    PAINT = 'PAINT'
    SHAPE = 'SHAPE'
    BREAKPOINT = 'BREAKPOINT'
    INPUT = 'INPUT'
    LOCAL = 'LOCAL'
    USING = 'USING'
    AND = 'AND'
    RETURN = 'RETURN'
    CREATE = 'CREATE'
    LIST = 'LIST'
    CONTAINING = 'CONTAINING'
    APPEND = 'APPEND'
    MULTIPLY = 'MULTIPLY'
    BY = 'BY'
    DIVIDE = 'DIVIDE'
    LESS = 'LESS'
    GREATER = 'GREATER'
    THAN = 'THAN'
    OR = 'OR'
    ELSE = 'ELSE'
    UPDATE = 'UPDATE'
    RANDOM = 'RANDOM'
    BETWEEN = 'BETWEEN'
    EOF = 'EOF'

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char in ' \t\r\n*,':
            self.advance()

    def number(self):
        result = ''
        if self.current_char == '-':
            result += '-'
            self.advance()
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result))

    def _id(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        # Check for natural language keywords
        keyword = result.lower()
        if keyword == 'set':
            return Token(TokenType.SET, keyword)
        elif keyword == 'to':
            return Token(TokenType.TO, keyword)
        elif keyword == 'add':
            return Token(TokenType.ADD, keyword)
        elif keyword == 'display':
            return Token(TokenType.DISPLAY, keyword)
        elif keyword == 'define':
            return Token(TokenType.DEFINE, keyword)
        elif keyword == 'action':
            return Token(TokenType.ACTION, keyword)
        elif keyword == 'end':
            return Token(TokenType.END, keyword)
        elif keyword == 'perform':
            return Token(TokenType.PERFORM, keyword)
        elif keyword == 'with':
            return Token(TokenType.WITH, keyword)
        elif keyword == 'intentionto':
            return Token(TokenType.INTENTIONTO, keyword)
        elif keyword == 'if':
            return Token(TokenType.IF, keyword)
        elif keyword == 'is':
            return Token(TokenType.IS, keyword)
        elif keyword == 'then':
            return Token(TokenType.THEN, keyword)
        elif keyword == 'repeat':
            return Token(TokenType.REPEAT, keyword)
        elif keyword == 'times':
            return Token(TokenType.TIMES, keyword)
        elif keyword == 'compile':
            return Token(TokenType.COMPILE, keyword)
        elif keyword == 'test':
            return Token(TokenType.TEST, keyword)
        elif keyword == 'production':
            return Token(TokenType.PRODUCTION, keyword)
        elif keyword == 'container':
            return Token(TokenType.CONTAINER, keyword)
        elif keyword == 'trigger':
            return Token(TokenType.TRIGGER, keyword)
        elif keyword == 'output':
            return Token(TokenType.OUTPUT, keyword)
        elif keyword == 'input':
            return Token(TokenType.INPUT, keyword)
        elif keyword == 'of':
            return Token(TokenType.OF, keyword)
        elif keyword == 'read':
            return Token(TokenType.READ, keyword)
        elif keyword == 'write':
            return Token(TokenType.WRITE, keyword)
        elif keyword == 'fetch':
            return Token(TokenType.FETCH, keyword)
        elif keyword == 'into':
            return Token(TokenType.INTO, keyword)
        elif keyword == 'file':
            return Token(TokenType.FILE, keyword)
        elif keyword == 'spawn':
            return Token(TokenType.SPAWN, keyword)
        elif keyword == 'at':
            return Token(TokenType.AT, keyword)
        elif keyword == 'bind':
            return Token(TokenType.BIND, keyword)
        elif keyword == 'move':
            return Token(TokenType.MOVE, keyword)
        elif keyword == 'up':
            return Token(TokenType.UP, keyword)
        elif keyword == 'down':
            return Token(TokenType.DOWN, keyword)
        elif keyword == 'left':
            return Token(TokenType.LEFT, keyword)
        elif keyword == 'right':
            return Token(TokenType.RIGHT, keyword)
        elif keyword == 'when':
            return Token(TokenType.WHEN, keyword)
        elif keyword == 'touches':
            return Token(TokenType.TOUCHES, keyword)
        elif keyword == 'subtract':
            return Token(TokenType.SUBTRACT, keyword)
        elif keyword == 'from':
            return Token(TokenType.FROM, keyword)
        elif keyword == 'attempt':
            return Token(TokenType.ATTEMPT, keyword)
        elif keyword == 'recover':
            return Token(TokenType.RECOVER, keyword)
        elif keyword == 'query':
            return Token(TokenType.QUERY, keyword)
        elif keyword == 'parse':
            return Token(TokenType.PARSE, keyword)
        elif keyword == 'json':
            return Token(TokenType.JSON, keyword)
        elif keyword == 'get':
            return Token(TokenType.GET, keyword)
        elif keyword == 'for':
            return Token(TokenType.FOR, keyword)
        elif keyword == 'each':
            return Token(TokenType.EACH, keyword)
        elif keyword == 'in':
            return Token(TokenType.IN, keyword)
        elif keyword == 'async':
            return Token(TokenType.ASYNC, keyword)
        elif keyword == 'secret':
            return Token(TokenType.SECRET, keyword)
        elif keyword == 'secrets':
            return Token(TokenType.SECRETS, keyword)
        elif keyword == 'load':
            return Token(TokenType.LOAD, keyword)
        elif keyword == 'paint':
            return Token(TokenType.PAINT, keyword)
        elif keyword == 'shape':
            return Token(TokenType.SHAPE, keyword)
        elif keyword == 'breakpoint':
            return Token(TokenType.BREAKPOINT, keyword)
        elif keyword == 'input':
            return Token(TokenType.INPUT, keyword)
        elif keyword == 'local': return Token(TokenType.LOCAL, keyword)
        elif keyword == 'using': return Token(TokenType.USING, keyword)
        elif keyword == 'and': return Token(TokenType.AND, keyword)
        elif keyword == 'return': return Token(TokenType.RETURN, keyword)
        elif keyword == 'create': return Token(TokenType.CREATE, keyword)
        elif keyword == 'list': return Token(TokenType.LIST, keyword)
        elif keyword == 'containing': return Token(TokenType.CONTAINING, keyword)
        elif keyword == 'append': return Token(TokenType.APPEND, keyword)
        elif keyword == 'multiply': return Token(TokenType.MULTIPLY, keyword)
        elif keyword == 'by': return Token(TokenType.BY, keyword)
        elif keyword == 'divide': return Token(TokenType.DIVIDE, keyword)
        elif keyword == 'less': return Token(TokenType.LESS, keyword)
        elif keyword == 'greater': return Token(TokenType.GREATER, keyword)
        elif keyword == 'than': return Token(TokenType.THAN, keyword)
        elif keyword == 'or': return Token(TokenType.OR, keyword)
        elif keyword == 'else': return Token(TokenType.ELSE, keyword)
        elif keyword == 'update': return Token(TokenType.UPDATE, keyword)
        elif keyword == 'random': return Token(TokenType.RANDOM, keyword)
        elif keyword == 'between': return Token(TokenType.BETWEEN, keyword)
            
        return Token(TokenType.IDENTIFIER, result)

    def string(self):
        result = ''
        self.advance() # Skip opening quote
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance() # Skip closing quote
        return Token(TokenType.STRING, result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char in ' \t\r\n*,':
                self.skip_whitespace()
                continue

            elif self.current_char.isdigit() or self.current_char == '-':
                if self.current_char == '-' and (self.pos + 1 >= len(self.text) or not self.text[self.pos + 1].isdigit()):
                    # Not a negative number, but we don't have subtract operator so this is an error
                    self.error()
                return self.number()

            if self.current_char.isalpha() or self.current_char == '_':
                return self._id()
                
            if self.current_char == '"':
                return self.string()
                
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.SLASH, '/')
            if self.current_char == ':':
                self.advance()
                return Token(TokenType.COLON, ':')
            if self.current_char == '|':
                self.advance()
                if self.current_char == '|':
                    self.advance()
                    return Token(TokenType.DOUBLE_PIPE, '||')
                return Token(TokenType.PIPE, '|')

            raise Exception(f"Liquid Matter doesn't understand this character: '{self.current_char}'")

        return Token(TokenType.EOF, None)

    def tokenize(self):
        tokens = []
        while True:
            tok = self.get_next_token()
            tokens.append(tok)
            if tok.type == TokenType.EOF:
                break
        return tokens

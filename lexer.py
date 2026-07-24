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
    ON = 'ON'
    EOF = 'EOF'
    ABSORB = 'ABSORB'
    NATIVE = 'NATIVE'
    INITIATE = 'INITIATE'
    ENABLE = 'ENABLE'
    DISABLE = 'DISABLE'
    CAMERA = 'CAMERA'
    MODE = 'MODE'
    ORBIT = 'ORBIT'
    ENTITY = 'ENTITY'
    MATERIAL = 'MATERIAL'
    GLOW = 'GLOW'
    ROTATE = 'ROTATE'
    CONTINUOUSLY = 'CONTINUOUSLY'
    AXIS = 'AXIS'
    SPHERE = 'SPHERE'
    CUBE = 'CUBE'
    OVERLAY = 'OVERLAY'
    BUTTON = 'BUTTON'
    STYLE = 'STYLE'
    CHANGE = 'CHANGE'
    CLICK = 'CLICK'
    START = 'START'
    RENDER = 'RENDER'
    LOOP = 'LOOP'
    COLOR = 'COLOR'
    BACKGROUND = 'BACKGROUND'
    WINDOW = 'WINDOW'
    TITLE = 'TITLE'
    ARCHITECTURE = 'ARCHITECTURE'
    NETWORK = 'NETWORK'
    NODE = 'NODE'
    CRYPTOGRAPHIC = 'CRYPTOGRAPHIC'
    CYBER = 'CYBER'
    MATRIX = 'MATRIX'
    FLUID = 'FLUID'
    DYNAMIC = 'DYNAMIC'
    INITIALIZE = 'INITIALIZE'
    TERMINATE = 'TERMINATE'
    BYPASS = 'BYPASS'
    KERNEL = 'KERNEL'
    PROTOCOL = 'PROTOCOL'
    SWARM = 'SWARM'
    AGENT = 'AGENT'
    AUTONOMOUS = 'AUTONOMOUS'
    GENERATE = 'GENERATE'
    MESH = 'MESH'
    TEXTURE = 'TEXTURE'
    SHADER = 'SHADER'
    LIGHTING = 'LIGHTING'
    PHYSICS = 'PHYSICS'
    COLLISION = 'COLLISION'
    GRAVITY = 'GRAVITY'
    VELOCITY = 'VELOCITY'
    VECTOR = 'VECTOR'
    TENSOR = 'TENSOR'
    NEURAL = 'NEURAL'
    LAYER = 'LAYER'
    GRADIENT = 'GRADIENT'
    EPOCH = 'EPOCH'
    LOSS = 'LOSS'
    OPTIMIZER = 'OPTIMIZER'
    TOKEN = 'TOKEN'
    CONTEXT = 'CONTEXT'
    ATTENTION = 'ATTENTION'
    TRANSFORMER = 'TRANSFORMER'
    WEB = 'WEB'
    ENVIRONMENT = 'ENVIRONMENT'
    ANTI = 'ANTI'
    ALIASING = 'ALIASING'
    FLOOR = 'FLOOR'
    PULSE = 'PULSE'
    ANIMATION = 'ANIMATION'
    CORE = 'CORE'
    SERVER = 'SERVER'
    MONOLITH = 'MONOLITH'
    GLASSMORPHISM = 'GLASSMORPHISM'
    REGISTRY = 'REGISTRY'
    ENCRYPTED = 'ENCRYPTED'
    FILES = 'FILES'
    SHREDDED = 'SHREDDED'
    UPON = 'UPON'
    TRANSFER = 'TRANSFER'
    SCREEN = 'SCREEN'
    GLITCH = 'GLITCH'
    EFFECT = 'EFFECT'
    DEPLOY = 'DEPLOY'
    EXECUTE = 'EXECUTE'
    NEXUS = 'NEXUS'
    VAULT = 'VAULT'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    STAR = 'STAR'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    EQ = 'EQ'
    NEQ = 'NEQ'
    GTE = 'GTE'
    LTE = 'LTE'
    GT = 'GT'
    LT = 'LT'
    COMMA = 'COMMA'
    NOT = 'NOT'
    DICTIONARY = 'DICTIONARY'
    KEY = 'KEY'


def format_diagnostic_error(message, source_code, line, column):
    prefix = "" if message.startswith(("Syntax Error:", "Liquid Error:", "Liquid Matter")) else "Syntax Error: "
    full_message = f"{prefix}{message}"
    if not source_code:
        return f"{full_message}\n  at Line {line}, Column {column}"
    lines = source_code.splitlines()
    if 1 <= line <= len(lines):
        snippet = lines[line - 1]
        line_str = str(line)
        gutter_width = max(len(line_str), 3)
        padded_line_num = line_str.rjust(gutter_width)
        gutter_indent = " " * gutter_width
        
        caret_pos = max(1, column) - 1
        visual_snippet = snippet.replace('\t', '    ')
        prefix_len = len(snippet[:caret_pos].replace('\t', '    '))
        pointer = " " * prefix_len + "^"

        error_box = (
            f"{full_message}\n"
            f"  at Line {line}, Column {column}:\n"
            f"    {padded_line_num} | {visual_snippet}\n"
            f"    {gutter_indent} | {pointer}"
        )
        return error_box
    else:
        return f"{full_message}\n  at Line {line}, Column {column}"


class Token:
    def __init__(self, type_, value, line=1, column=1):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, line={self.line}, col={self.column})"

import re

class Lexer:
    def __init__(self, text):
        self.text = text
        self.token_specification = [
            ('COMMENT',     r'\|\|[^\n]*'),
            ('EQ',          r'=='),
            ('NEQ',         r'!='),
            ('GTE',         r'>='),
            ('LTE',         r'<='),
            ('GT',          r'>'),
            ('LT',          r'<'),
            ('DOUBLE_PIPE', r'\|\|'),
            ('PIPE',        r'\|'),
            ('PLUS',        r'\+'),
            ('MINUS',       r'-'),
            ('STAR',        r'\*'),
            ('SLASH',       r'/'),
            ('LPAREN',      r'\('),
            ('RPAREN',      r'\)'),
            ('COLON',       r':'),
            ('COMMA',       r','),
            ('NUMBER',      r'\d+(\.\d+)?'),
            ('STRING',      r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"[^"]*"|\'[^\']*\'' ),
            ('ID',          r'[a-zA-Z_]\w*'),
            ('WS',          r'[ \t\r\n]+'),
            ('MISMATCH',    r'.'),
        ]
        self.tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_specification)
        self.keyword_map = {
            'set': TokenType.SET, 'to': TokenType.TO, 'add': TokenType.ADD, 'display': TokenType.DISPLAY,
            'define': TokenType.DEFINE, 'action': TokenType.ACTION, 'end': TokenType.END, 'perform': TokenType.PERFORM,
            'with': TokenType.WITH, 'intentionto': TokenType.INTENTIONTO, 'if': TokenType.IF, 'is': TokenType.IS,
            'then': TokenType.THEN, 'repeat': TokenType.REPEAT, 'times': TokenType.TIMES, 'compile': TokenType.COMPILE,
            'test': TokenType.TEST, 'production': TokenType.PRODUCTION, 'container': TokenType.CONTAINER,
            'trigger': TokenType.TRIGGER, 'output': TokenType.OUTPUT, 'input': TokenType.INPUT, 'of': TokenType.OF,
            'read': TokenType.READ, 'write': TokenType.WRITE, 'fetch': TokenType.FETCH, 'into': TokenType.INTO,
            'file': TokenType.FILE, 'spawn': TokenType.SPAWN, 'at': TokenType.AT, 'bind': TokenType.BIND,
            'move': TokenType.MOVE, 'up': TokenType.UP, 'down': TokenType.DOWN, 'left': TokenType.LEFT,
            'right': TokenType.RIGHT, 'when': TokenType.WHEN, 'touches': TokenType.TOUCHES, 'subtract': TokenType.SUBTRACT,
            'from': TokenType.FROM, 'attempt': TokenType.ATTEMPT, 'recover': TokenType.RECOVER, 'query': TokenType.QUERY,
            'parse': TokenType.PARSE, 'json': TokenType.JSON, 'get': TokenType.GET, 'for': TokenType.FOR,
            'each': TokenType.EACH, 'in': TokenType.IN, 'async': TokenType.ASYNC, 'secret': TokenType.SECRET,
            'secrets': TokenType.SECRETS, 'load': TokenType.LOAD, 'paint': TokenType.PAINT, 'shape': TokenType.SHAPE,
            'breakpoint': TokenType.BREAKPOINT, 'local': TokenType.LOCAL, 'using': TokenType.USING, 'and': TokenType.AND,
            'return': TokenType.RETURN, 'create': TokenType.CREATE, 'list': TokenType.LIST, 'containing': TokenType.CONTAINING,
            'append': TokenType.APPEND, 'multiply': TokenType.MULTIPLY, 'by': TokenType.BY, 'divide': TokenType.DIVIDE,
            'less': TokenType.LESS, 'greater': TokenType.GREATER, 'than': TokenType.THAN, 'or': TokenType.OR,
            'else': TokenType.ELSE, 'update': TokenType.UPDATE, 'random': TokenType.RANDOM, 'between': TokenType.BETWEEN,
            'on': TokenType.ON, 'absorb': TokenType.ABSORB, 'native': TokenType.NATIVE,
            'not': TokenType.NOT, 'dictionary': TokenType.DICTIONARY, 'dict': TokenType.DICTIONARY, 'key': TokenType.KEY,
            'initiate': TokenType.INITIATE,
            'enable': TokenType.ENABLE,
            'disable': TokenType.DISABLE,
            'camera': TokenType.CAMERA,
            'mode': TokenType.MODE,
            'orbit': TokenType.ORBIT,
            'entity': TokenType.ENTITY,
            'material': TokenType.MATERIAL,
            'glow': TokenType.GLOW,
            'rotate': TokenType.ROTATE,
            'continuously': TokenType.CONTINUOUSLY,
            'axis': TokenType.AXIS,
            'sphere': TokenType.SPHERE,
            'cube': TokenType.CUBE,
            'overlay': TokenType.OVERLAY,
            'button': TokenType.BUTTON,
            'style': TokenType.STYLE,
            'change': TokenType.CHANGE,
            'click': TokenType.CLICK,
            'start': TokenType.START,
            'render': TokenType.RENDER,
            'loop': TokenType.LOOP,
            'color': TokenType.COLOR,
            'background': TokenType.BACKGROUND,
            'window': TokenType.WINDOW,
            'title': TokenType.TITLE,
            'architecture': TokenType.ARCHITECTURE,
            'network': TokenType.NETWORK,
            'node': TokenType.NODE,
            'cryptographic': TokenType.CRYPTOGRAPHIC,
            'cyber': TokenType.CYBER,
            'matrix': TokenType.MATRIX,
            'fluid': TokenType.FLUID,
            'dynamic': TokenType.DYNAMIC,
            'initialize': TokenType.INITIALIZE,
            'terminate': TokenType.TERMINATE,
            'bypass': TokenType.BYPASS,
            'kernel': TokenType.KERNEL,
            'protocol': TokenType.PROTOCOL,
            'swarm': TokenType.SWARM,
            'agent': TokenType.AGENT,
            'autonomous': TokenType.AUTONOMOUS,
            'generate': TokenType.GENERATE,
            'mesh': TokenType.MESH,
            'texture': TokenType.TEXTURE,
            'shader': TokenType.SHADER,
            'lighting': TokenType.LIGHTING,
            'physics': TokenType.PHYSICS,
            'collision': TokenType.COLLISION,
            'gravity': TokenType.GRAVITY,
            'velocity': TokenType.VELOCITY,
            'vector': TokenType.VECTOR,
            'tensor': TokenType.TENSOR,
            'neural': TokenType.NEURAL,
            'layer': TokenType.LAYER,
            'gradient': TokenType.GRADIENT,
            'epoch': TokenType.EPOCH,
            'loss': TokenType.LOSS,
            'optimizer': TokenType.OPTIMIZER,
            'token': TokenType.TOKEN,
            'context': TokenType.CONTEXT,
            'attention': TokenType.ATTENTION,
            'transformer': TokenType.TRANSFORMER,
            'web': TokenType.WEB,
            'environment': TokenType.ENVIRONMENT,
            'anti': TokenType.ANTI,
            'aliasing': TokenType.ALIASING,
            'floor': TokenType.FLOOR,
            'pulse': TokenType.PULSE,
            'animation': TokenType.ANIMATION,
            'core': TokenType.CORE,
            'server': TokenType.SERVER,
            'monolith': TokenType.MONOLITH,
            'glassmorphism': TokenType.GLASSMORPHISM,
            'registry': TokenType.REGISTRY,
            'encrypted': TokenType.ENCRYPTED,
            'files': TokenType.FILES,
            'shredded': TokenType.SHREDDED,
            'upon': TokenType.UPON,
            'transfer': TokenType.TRANSFER,
            'screen': TokenType.SCREEN,
            'glitch': TokenType.GLITCH,
            'effect': TokenType.EFFECT,
            'deploy': TokenType.DEPLOY,
            'execute': TokenType.EXECUTE,
            'nexus': TokenType.NEXUS,
            'vault': TokenType.VAULT
        }
        self.parsed_tokens = self.tokenize()
        self.token_iter = iter(self.parsed_tokens)

    def format_error(self, message, line, column):
        return format_diagnostic_error(message, self.text, line, column)

    def tokenize(self):
        tokens = []
        for mo in re.finditer(self.tok_regex, self.text):
            kind = mo.lastgroup
            value = mo.group()
            start_pos = mo.start()
            
            line = self.text.count('\n', 0, start_pos) + 1
            last_newline = self.text.rfind('\n', 0, start_pos)
            column = start_pos + 1 if last_newline == -1 else start_pos - last_newline
            
            if kind == 'WS' or kind == 'COMMENT':
                continue
            elif kind == 'NUMBER':
                val = float(value) if '.' in value else int(value)
                tokens.append(Token(TokenType.NUMBER, val, line, column))
            elif kind == 'STRING':
                if value.startswith(('"""', "'''")):
                    raw_str = value[3:-3]
                else:
                    raw_str = value[1:-1]
                tokens.append(Token(TokenType.STRING, raw_str, line, column))
            elif kind == 'ID':
                kw = value.lower()
                # Check thesaurus dictionary for natural language synonyms
                from thesaurus import SYNONYM_MAP
                mapped_kw = SYNONYM_MAP.get(kw, kw)
                
                if mapped_kw in self.keyword_map:
                    tokens.append(Token(self.keyword_map[mapped_kw], mapped_kw, line, column))
                elif kw in self.keyword_map:
                    tokens.append(Token(self.keyword_map[kw], kw, line, column))
                else:
                    tokens.append(Token(TokenType.IDENTIFIER, value, line, column))
            elif kind == 'PLUS':
                tokens.append(Token(TokenType.PLUS, '+', line, column))
            elif kind == 'MINUS':
                tokens.append(Token(TokenType.MINUS, '-', line, column))
            elif kind == 'STAR':
                tokens.append(Token(TokenType.STAR, '*', line, column))
            elif kind == 'SLASH':
                tokens.append(Token(TokenType.SLASH, '/', line, column))
            elif kind == 'LPAREN':
                tokens.append(Token(TokenType.LPAREN, '(', line, column))
            elif kind == 'RPAREN':
                tokens.append(Token(TokenType.RPAREN, ')', line, column))
            elif kind == 'EQ':
                tokens.append(Token(TokenType.EQ, '==', line, column))
            elif kind == 'NEQ':
                tokens.append(Token(TokenType.NEQ, '!=', line, column))
            elif kind == 'GTE':
                tokens.append(Token(TokenType.GTE, '>=', line, column))
            elif kind == 'LTE':
                tokens.append(Token(TokenType.LTE, '<=', line, column))
            elif kind == 'GT':
                tokens.append(Token(TokenType.GT, '>', line, column))
            elif kind == 'LT':
                tokens.append(Token(TokenType.LT, '<', line, column))
            elif kind == 'COMMA':
                tokens.append(Token(TokenType.COMMA, ',', line, column))
            elif kind == 'DOUBLE_PIPE':
                tokens.append(Token(TokenType.DOUBLE_PIPE, '||', line, column))
            elif kind == 'PIPE':
                tokens.append(Token(TokenType.PIPE, '|', line, column))
            elif kind == 'COLON':
                tokens.append(Token(TokenType.COLON, ':', line, column))
            elif kind == 'MISMATCH':
                err_msg = self.format_error(f"Liquid Matter doesn't understand this character: '{value}'", line, column)
                raise Exception(err_msg)
                
        end_pos = len(self.text)
        eof_line = self.text.count('\n', 0, end_pos) + 1
        last_newline = self.text.rfind('\n', 0, end_pos)
        eof_column = end_pos + 1 if last_newline == -1 else end_pos - last_newline
        tokens.append(Token(TokenType.EOF, None, eof_line, eof_column))
        return tokens

    def get_next_token(self):
        try:
            return next(self.token_iter)
        except StopIteration:
            end_pos = len(self.text)
            eof_line = self.text.count('\n', 0, end_pos) + 1
            last_newline = self.text.rfind('\n', 0, end_pos)
            eof_column = end_pos + 1 if last_newline == -1 else end_pos - last_newline
            return Token(TokenType.EOF, None, eof_line, eof_column)


from lexer import TokenType

# Abstract Syntax Tree Nodes
class AST:
    pass

class WebGLNode(AST):
    def __init__(self, raw_tokens):
        self.raw_tokens = raw_tokens

    pass

class SetStatement(AST):
    def __init__(self, target, value, is_local=False):
        self.target = target
        self.value = value
        self.is_local = is_local

class AddStatement(AST):
    def __init__(self, value, identifier):
        self.value = value
        self.identifier = identifier

class SubtractStatement(AST):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class MultiplyStatement(AST):
    def __init__(self, target, value):
        self.target = target
        self.value = value

class DivideStatement(AST):
    def __init__(self, target, value):
        self.target = target
        self.value = value

class DisplayStatement(AST):
    def __init__(self, target):
        self.target = target # Could be an identifier or a number

class NumberNode(AST):
    def __init__(self, value):
        self.value = value

class StringNode(AST):
    def __init__(self, value):
        self.value = value

class FunctionDefNode(AST):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCallNode(AST):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class IntentionNode(AST):
    def __init__(self, target):
        self.target = target

class BinaryOpNode(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOpNode(AST):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

class CreateDictionaryNode(AST):
    def __init__(self, target):
        self.target = target

class SetDictKeyNode(AST):
    def __init__(self, dict_name, key, value):
        self.dict_name = dict_name
        self.key = key
        self.value = value

class IfNode(AST):
    def __init__(self, condition=None, body=None, else_body=None, left=None, operator=None, right=None):
        self.condition = condition
        self.body = body if body is not None else []
        self.else_body = else_body
        self.left = left
        self.operator = operator
        self.right = right

class RepeatNode(AST):
    def __init__(self, count, body):
        self.count = count
        self.body = body

class CompileNode(AST):
    pass

class TestProductionNode(AST):
    pass

class ContainerNode(AST):
    def __init__(self, name, attributes, output_body, input_body):
        self.name = name
        self.attributes = attributes
        self.output_body = output_body
        self.input_body = input_body

class TriggerContainerNode(AST):
    def __init__(self, name, trigger_type):
        self.name = name
        self.trigger_type = trigger_type

class ReadFileNode(AST):
    def __init__(self, filepath, target):
        self.filepath = filepath
        self.target = target

class WriteFileNode(AST):
    def __init__(self, content, filepath):
        self.content = content
        self.filepath = filepath

class FetchNode(AST):
    def __init__(self, url, target):
        self.url = url
        self.target = target

class SpawnNode(AST):
    def __init__(self, target, x, y):
        self.target = target
        self.x = x
        self.y = y

class BindNode(AST):
    def __init__(self, key, action_name):
        self.key = key
        self.action_name = action_name

class MoveNode(AST):
    def __init__(self, target, direction):
        self.target = target
        self.direction = direction

class CollisionNode(AST):
    def __init__(self, obj1, obj2, action_name):
        self.obj1 = obj1
        self.obj2 = obj2
        self.action_name = action_name

class AttemptNode(AST):
    def __init__(self, attempt_body, recover_body):
        self.attempt_body = attempt_body
        self.recover_body = recover_body

class QueryNode(AST):
    def __init__(self, query_string):
        self.query_string = query_string

class ParseJsonNode(AST):
    def __init__(self, source, target):
        self.source = source
        self.target = target

class GetNode(AST):
    def __init__(self, key, source, target):
        self.key = key
        self.source = source
        self.target = target

class ForEachNode(AST):
    def __init__(self, iterator_name, list_name, action_name):
        self.iterator_name = iterator_name
        self.list_name = list_name
        self.action_name = action_name

class AsyncNode(AST):
    def __init__(self, action_name):
        self.action_name = action_name

class LoadSecretsNode(AST):
    pass

class GetSecretNode(AST):
    def __init__(self, secret_name, target):
        self.secret_name = secret_name
        self.target = target

class PaintNode(AST):
    def __init__(self, target, color):
        self.target = target
        self.color = color

class ShapeNode(AST):
    def __init__(self, target, shape):
        self.target = target
        self.shape = shape

class BreakpointNode(AST):
    pass

class AbsorbNode(AST):
    def __init__(self, target_file):
        self.target_file = target_file

class ExecuteNativeNode(AST):
    def __init__(self, code_string):
        self.code_string = code_string

class InputNode(AST):
    def __init__(self, prompt, target):
        self.prompt = prompt
        self.target = target

class CreateListNode(AST):
    def __init__(self, target, items):
        self.target = target
        self.items = items

class AppendListNode(AST):
    def __init__(self, value, target):
        self.value = value
        self.target = target

class ReturnNode(AST):
    def __init__(self, value):
        self.value = value

class RandomNode(AST):
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

class OnUpdateNode(AST):
    def __init__(self, action_name):
        self.action_name = action_name

class IdentifierNode(AST):
    def __init__(self, value):
        self.value = value

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def format_error(self, message, token=None):
        if token is None:
            token = self.current_token
        if hasattr(self.lexer, 'format_error') and hasattr(token, 'line') and hasattr(token, 'column'):
            return self.lexer.format_error(message, token.line, token.column)
        return message

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            msg = f"Liquid Matter expected {token_type} but found {self.current_token.type}"
            raise Exception(self.format_error(msg, self.current_token))

    def parse_expression(self):
        return self.parse_or()

    def parse_or(self):
        left = self.parse_and()
        while self.current_token.type == TokenType.OR:
            op = self.current_token.value
            self.eat(TokenType.OR)
            right = self.parse_and()
            left = BinaryOpNode(left, op, right)
        return left

    def parse_and(self):
        left = self.parse_not()
        while self.current_token.type == TokenType.AND:
            op = self.current_token.value
            self.eat(TokenType.AND)
            right = self.parse_not()
            left = BinaryOpNode(left, op, right)
        return left

    def parse_not(self):
        if self.current_token.type == TokenType.NOT:
            self.eat(TokenType.NOT)
            expr = self.parse_not()
            return UnaryOpNode('not', expr)
        return self.parse_comparison()

    def parse_comparison(self):
        left = self.parse_add_sub()
        
        if self.current_token.type in (TokenType.EQ, TokenType.NEQ, TokenType.GT, TokenType.LT, TokenType.GTE, TokenType.LTE):
            op = self.current_token.value
            self.eat(self.current_token.type)
            right = self.parse_add_sub()
            return BinaryOpNode(left, op, right)
        elif self.current_token.type == TokenType.IS:
            self.eat(TokenType.IS)
            if self.current_token.type == TokenType.GREATER:
                self.eat(TokenType.GREATER)
                self.eat(TokenType.THAN)
                op = ">"
            elif self.current_token.type == TokenType.LESS:
                self.eat(TokenType.LESS)
                self.eat(TokenType.THAN)
                op = "<"
            elif self.current_token.type == TokenType.NOT:
                self.eat(TokenType.NOT)
                op = "!="
            else:
                op = "=="
            right = self.parse_add_sub()
            return BinaryOpNode(left, op, right)
        elif self.current_token.type == TokenType.GREATER:
            self.eat(TokenType.GREATER)
            self.eat(TokenType.THAN)
            op = ">"
            right = self.parse_add_sub()
            return BinaryOpNode(left, op, right)
        elif self.current_token.type == TokenType.LESS:
            self.eat(TokenType.LESS)
            self.eat(TokenType.THAN)
            op = "<"
            right = self.parse_add_sub()
            return BinaryOpNode(left, op, right)
            
        return left

    def parse_add_sub(self):
        left = self.parse_mul_div()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token.value
            self.eat(self.current_token.type)
            right = self.parse_mul_div()
            left = BinaryOpNode(left, op, right)
        return left

    def parse_mul_div(self):
        left = self.parse_unary()
        while self.current_token.type in (TokenType.STAR, TokenType.SLASH):
            op = self.current_token.value
            self.eat(self.current_token.type)
            right = self.parse_unary()
            left = BinaryOpNode(left, op, right)
        return left

    def parse_unary(self):
        if self.current_token.type == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            expr = self.parse_unary()
            return UnaryOpNode('-', expr)
        return self.parse_primary()

    def parse_primary(self):
        if self.current_token.type == TokenType.NUMBER:
            val = self.current_token.value
            self.eat(TokenType.NUMBER)
            return NumberNode(val)
        elif self.current_token.type == TokenType.STRING:
            val = self.current_token.value
            self.eat(TokenType.STRING)
            return StringNode(val)
        elif self.current_token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            expr = self.parse_expression()
            self.eat(TokenType.RPAREN)
            return expr
        elif self.current_token.type == TokenType.RANDOM:
            self.eat(TokenType.RANDOM)
            self.eat(TokenType.BETWEEN)
            min_val = self.parse_expression()
            self.eat(TokenType.AND)
            max_val = self.parse_expression()
            return RandomNode(min_val, max_val)
        elif self.current_token.type == TokenType.PERFORM:
            return self.statement()
        elif self.current_token.type == TokenType.GET:
            return self.statement()
        elif self.current_token.type == TokenType.IDENTIFIER:
            val = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return IdentifierNode(val)
        else:
            msg = f"Liquid Matter parser expected expression, found: {self.current_token.type} ('{self.current_token.value}')"
            raise Exception(self.format_error(msg, self.current_token))

    def statement(self):

        if self.current_token.type == TokenType.INITIATE:
            self.eat(TokenType.INITIATE)
            tokens = []
            while self.current_token.type != TokenType.EOF:
                tokens.append(str(self.current_token.value))
                self.current_token = self.lexer.get_next_token()
            return WebGLNode(tokens)

        # e.g., "set x to 10" or "set key 'age' of user to 30"
        if self.current_token.type == TokenType.SET:
            self.eat(TokenType.SET)
            
            if self.current_token.type == TokenType.KEY:
                self.eat(TokenType.KEY)
                key_expr = self.parse_expression()
                self.eat(TokenType.OF)
                dict_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                self.eat(TokenType.TO)
                val_expr = self.parse_expression()
                return SetDictKeyNode(IdentifierNode(dict_name), key_expr, val_expr)

            is_local = False
            if self.current_token.type == TokenType.LOCAL:
                self.eat(TokenType.LOCAL)
                is_local = True
            
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.TO)
            
            value = self.parse_expression()
            return SetStatement(IdentifierNode(target), value, is_local)
            
        # e.g., "add 5 to x" or "add score to total"
        elif self.current_token.type == TokenType.ADD:
            self.eat(TokenType.ADD)
            if self.current_token.type == TokenType.NUMBER:
                amount = NumberNode(self.current_token.value)
                self.eat(TokenType.NUMBER)
            else:
                amount = IdentifierNode(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.TO)
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return AddStatement(amount, IdentifierNode(var_name))

        # e.g., "display x"
        elif self.current_token.type == TokenType.DISPLAY:
            self.eat(TokenType.DISPLAY)
            expr = self.parse_expression()
            return DisplayStatement(expr)
                
        # e.g., "define action greet with name"
        elif self.current_token.type == TokenType.DEFINE:
            self.eat(TokenType.DEFINE)
            self.eat(TokenType.ACTION)
            func_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            
            params = []
            if self.current_token.type == TokenType.WITH:
                self.eat(TokenType.WITH)
                while self.current_token.type == TokenType.IDENTIFIER:
                    params.append(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
                    if self.current_token.type == TokenType.AND:
                        self.eat(TokenType.AND)
            
            body = []
            while self.current_token.type != TokenType.END and self.current_token.type != TokenType.EOF:
                body.append(self.statement())
            
            self.eat(TokenType.END)
            return FunctionDefNode(IdentifierNode(func_name), params, body)

        # e.g., "perform greet with Liquid"
        elif self.current_token.type == TokenType.PERFORM:
            self.eat(TokenType.PERFORM)
            func_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            
            args = []
            if self.current_token.type == TokenType.WITH:
                self.eat(TokenType.WITH)
                while self.current_token.type in (TokenType.IDENTIFIER, TokenType.NUMBER, TokenType.STRING):
                    if self.current_token.type == TokenType.NUMBER:
                        args.append(NumberNode(self.current_token.value))
                        self.eat(TokenType.NUMBER)
                    elif self.current_token.type == TokenType.STRING:
                        args.append(StringNode(self.current_token.value))
                        self.eat(TokenType.STRING)
                    else:
                        args.append(IdentifierNode(self.current_token.value))
                        self.eat(TokenType.IDENTIFIER)
                    if self.current_token.type == TokenType.AND:
                        self.eat(TokenType.AND)
                        
            return FunctionCallNode(IdentifierNode(func_name), args)
            
        # e.g., 'IntentionTO "build Unity Project"'
        elif self.current_token.type == TokenType.INTENTIONTO:
            self.eat(TokenType.INTENTIONTO)
            target = self.current_token.value
            self.eat(TokenType.STRING)
            return IntentionNode(target)
            
        # e.g., "if power is 10 then", "if x > 5 and y < 10 then"
        elif self.current_token.type == TokenType.IF:
            self.eat(TokenType.IF)
            condition = self.parse_expression()
            self.eat(TokenType.THEN)
            
            body = []
            while self.current_token.type not in (TokenType.END, TokenType.ELSE, TokenType.EOF):
                body.append(self.statement())
                
            else_body = None
            if self.current_token.type == TokenType.ELSE:
                self.eat(TokenType.ELSE)
                else_body = []
                while self.current_token.type not in (TokenType.END, TokenType.EOF):
                    else_body.append(self.statement())
                
            self.eat(TokenType.END)
            return IfNode(condition=condition, body=body, else_body=else_body)
            
        # e.g., "repeat 5 times"
        elif self.current_token.type == TokenType.REPEAT:
            self.eat(TokenType.REPEAT)
            count = self.parse_expression()
            self.eat(TokenType.TIMES)
            
            body = []
            while self.current_token.type != TokenType.END and self.current_token.type != TokenType.EOF:
                body.append(self.statement())
                
            self.eat(TokenType.END)
            return RepeatNode(count, body)
            
        # e.g., "Compile"
        elif self.current_token.type == TokenType.COMPILE:
            self.eat(TokenType.COMPILE)
            return CompileNode()
            
        # e.g., "Test Production"
        elif self.current_token.type == TokenType.TEST:
            self.eat(TokenType.TEST)
            self.eat(TokenType.PRODUCTION)
            return TestProductionNode()
            
        # e.g., Container/Player: health 100, speed 5 | display "Ready" | || set health to 50 ||
        elif self.current_token.type == TokenType.CONTAINER:
            self.eat(TokenType.CONTAINER)
            self.eat(TokenType.SLASH)
            container_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.COLON)
            
            attributes = []
            while self.current_token.type != TokenType.PIPE:
                attr_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                
                if self.current_token.type == TokenType.NUMBER:
                    attr_val = NumberNode(self.current_token.value)
                    self.eat(TokenType.NUMBER)
                elif self.current_token.type == TokenType.STRING:
                    attr_val = StringNode(self.current_token.value)
                    self.eat(TokenType.STRING)
                else:
                    attr_val = IdentifierNode(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
                    
                attributes.append((attr_name, attr_val))
                
            self.eat(TokenType.PIPE)
            output_body = []
            while self.current_token.type != TokenType.PIPE:
                output_body.append(self.statement())
            self.eat(TokenType.PIPE)
            
            self.eat(TokenType.DOUBLE_PIPE)
            input_body = []
            while self.current_token.type != TokenType.DOUBLE_PIPE:
                input_body.append(self.statement())
            self.eat(TokenType.DOUBLE_PIPE)
            
            return ContainerNode(container_name, attributes, output_body, input_body)
            
        # e.g., trigger Output of Player
        elif self.current_token.type == TokenType.TRIGGER:
            self.eat(TokenType.TRIGGER)
            t_type = self.current_token.value.lower()
            if t_type == 'output':
                self.eat(TokenType.OUTPUT)
            elif t_type == 'input':
                self.eat(TokenType.INPUT)
                
            if self.current_token.type == TokenType.OF:
                self.eat(TokenType.OF)
                
            c_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return TriggerContainerNode(c_name, t_type)

        # e.g., "read file 'data.txt' into config"
        elif self.current_token.type == TokenType.READ:
            self.eat(TokenType.READ)
            if self.current_token.type == TokenType.FILE:
                self.eat(TokenType.FILE)
            filepath = self.current_token.value
            self.eat(TokenType.STRING)
            self.eat(TokenType.INTO)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return ReadFileNode(StringNode(filepath), IdentifierNode(target))

        # e.g., "write 'hello' into file 'data.txt'"
        elif self.current_token.type == TokenType.WRITE:
            self.eat(TokenType.WRITE)
            
            if self.current_token.type == TokenType.STRING:
                content = StringNode(self.current_token.value)
                self.eat(TokenType.STRING)
            else:
                content = IdentifierNode(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
                
            self.eat(TokenType.INTO)
            if self.current_token.type == TokenType.FILE:
                self.eat(TokenType.FILE)
                
            filepath = self.current_token.value
            self.eat(TokenType.STRING)
            return WriteFileNode(content, StringNode(filepath))

        # e.g., "fetch 'https://api.github.com' into data"
        elif self.current_token.type == TokenType.FETCH:
            self.eat(TokenType.FETCH)
            url = self.current_token.value
            self.eat(TokenType.STRING)
            self.eat(TokenType.INTO)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return FetchNode(StringNode(url), IdentifierNode(target))
            
        # e.g., "spawn Player at 0 0"
        elif self.current_token.type == TokenType.SPAWN:
            self.eat(TokenType.SPAWN)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.AT)
            x = self.current_token.value
            self.eat(TokenType.NUMBER)
            y = self.current_token.value
            self.eat(TokenType.NUMBER)
            return SpawnNode(IdentifierNode(target), NumberNode(x), NumberNode(y))
            
        # e.g., "bind 'w' to moveUp"
        elif self.current_token.type == TokenType.BIND:
            self.eat(TokenType.BIND)
            key = self.current_token.value
            self.eat(TokenType.STRING)
            self.eat(TokenType.TO)
            action_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return BindNode(StringNode(key), IdentifierNode(action_name))
            
        # e.g., "move Player up"
        elif self.current_token.type == TokenType.MOVE:
            self.eat(TokenType.MOVE)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            
            dir_val = self.current_token.value
            if self.current_token.type in (TokenType.UP, TokenType.DOWN, TokenType.LEFT, TokenType.RIGHT):
                self.eat(self.current_token.type)
            else:
                msg = f"Liquid Matter expects a direction (up, down, left, right), found '{self.current_token.value}'"
                raise Exception(self.format_error(msg, self.current_token))
            return MoveNode(IdentifierNode(target), StringNode(dir_val))
            
        # e.g., "subtract 10 from health"
        elif self.current_token.type == TokenType.SUBTRACT:
            self.eat(TokenType.SUBTRACT)
            if self.current_token.type == TokenType.NUMBER:
                value = NumberNode(self.current_token.value)
                self.eat(TokenType.NUMBER)
            else:
                value = IdentifierNode(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.FROM)
            identifier = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return SubtractStatement(IdentifierNode(identifier), value)

        # e.g., "multiply score by 2"
        elif self.current_token.type == TokenType.MULTIPLY:
            self.eat(TokenType.MULTIPLY)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.BY)
            if self.current_token.type == TokenType.NUMBER:
                value = NumberNode(self.current_token.value)
                self.eat(TokenType.NUMBER)
            else:
                value = IdentifierNode(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
            return MultiplyStatement(IdentifierNode(target), value)

        # e.g., "divide score by 2"
        elif self.current_token.type == TokenType.DIVIDE:
            self.eat(TokenType.DIVIDE)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.BY)
            if self.current_token.type == TokenType.NUMBER:
                value = NumberNode(self.current_token.value)
                self.eat(TokenType.NUMBER)
            else:
                value = IdentifierNode(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
            return DivideStatement(IdentifierNode(target), value)
            
        # e.g. "create dictionary user" or "create list roster containing 'A', 'B'"
        elif self.current_token.type == TokenType.CREATE:
            self.eat(TokenType.CREATE)
            if self.current_token.type == TokenType.DICTIONARY:
                self.eat(TokenType.DICTIONARY)
                target = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                return CreateDictionaryNode(IdentifierNode(target))
            elif self.current_token.type == TokenType.LIST:
                self.eat(TokenType.LIST)
                target = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                self.eat(TokenType.CONTAINING)
                items = []
                while self.current_token.type in (TokenType.STRING, TokenType.NUMBER, TokenType.IDENTIFIER):
                    if self.current_token.type == TokenType.STRING:
                        items.append(StringNode(self.current_token.value))
                        self.eat(TokenType.STRING)
                    elif self.current_token.type == TokenType.NUMBER:
                        items.append(NumberNode(self.current_token.value))
                        self.eat(TokenType.NUMBER)
                    elif self.current_token.type == TokenType.IDENTIFIER:
                        items.append(IdentifierNode(self.current_token.value))
                        self.eat(TokenType.IDENTIFIER)
                    if self.current_token.type == TokenType.COMMA:
                        self.eat(TokenType.COMMA)
                return CreateListNode(IdentifierNode(target), items)
            
        # e.g. "append 'A' to roster"
        elif self.current_token.type == TokenType.APPEND:
            self.eat(TokenType.APPEND)
            val = self.parse_expression()
            self.eat(TokenType.TO)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return AppendListNode(val, IdentifierNode(target))
            
        # e.g., "return 50"
        elif self.current_token.type == TokenType.RETURN:
            self.eat(TokenType.RETURN)
            val = self.parse_expression()
            return ReturnNode(val)
            
        # e.g., "on update perform tick"
        elif self.current_token.type == TokenType.ON:
            self.eat(TokenType.ON)
            self.eat(TokenType.UPDATE)
            self.eat(TokenType.PERFORM)
            action = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return OnUpdateNode(IdentifierNode(action))
            
        # e.g., "when Player touches Enemy perform takeDamage"
        elif self.current_token.type == TokenType.WHEN:
            self.eat(TokenType.WHEN)
            obj1 = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.TOUCHES)
            obj2 = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.PERFORM)
            action = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return CollisionNode(IdentifierNode(obj1), IdentifierNode(obj2), IdentifierNode(action))
            
        # e.g., "attempt ... recover ... end"
        elif self.current_token.type == TokenType.ATTEMPT:
            self.eat(TokenType.ATTEMPT)
            attempt_body = []
            while self.current_token.type != TokenType.RECOVER and self.current_token.type != TokenType.EOF:
                attempt_body.append(self.statement())
                
            self.eat(TokenType.RECOVER)
            recover_body = []
            while self.current_token.type != TokenType.END and self.current_token.type != TokenType.EOF:
                recover_body.append(self.statement())
                
            self.eat(TokenType.END)
            return AttemptNode(attempt_body, recover_body)
            
        # e.g., "query 'SELECT * FROM users'"
        elif self.current_token.type == TokenType.QUERY:
            self.eat(TokenType.QUERY)
            query_str = self.current_token.value
            self.eat(TokenType.STRING)
            return QueryNode(StringNode(query_str))
            
        # e.g., "parse json rawData into parsedData"
        elif self.current_token.type == TokenType.PARSE:
            self.eat(TokenType.PARSE)
            self.eat(TokenType.JSON)
            source = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.INTO)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return ParseJsonNode(IdentifierNode(source), IdentifierNode(target))
            
        # e.g. "load secrets"
        elif self.current_token.type == TokenType.LOAD:
            self.eat(TokenType.LOAD)
            self.eat(TokenType.SECRETS)
            return LoadSecretsNode()

        # e.g., "get 'name' from parsedData into val" OR "get secret 'API_KEY' into val"
        elif self.current_token.type == TokenType.GET:
            self.eat(TokenType.GET)
            
            if self.current_token.type == TokenType.SECRET:
                self.eat(TokenType.SECRET)
                secret_name = StringNode(self.current_token.value)
                self.eat(TokenType.STRING)
                self.eat(TokenType.INTO)
                target = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                return GetSecretNode(secret_name, IdentifierNode(target))
            
            if self.current_token.type == TokenType.KEY:
                self.eat(TokenType.KEY)
                
            key = self.parse_expression()
            self.eat(TokenType.FROM)
            source = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.INTO)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return GetNode(key, IdentifierNode(source), IdentifierNode(target))

        # e.g., "for each user in userList perform printUser"
        elif self.current_token.type == TokenType.FOR:
            self.eat(TokenType.FOR)
            self.eat(TokenType.EACH)
            iterator = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.IN)
            list_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.PERFORM)
            action_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return ForEachNode(IdentifierNode(iterator), IdentifierNode(list_name), IdentifierNode(action_name))

        # e.g., "async perform heavyTask"
        elif self.current_token.type == TokenType.ASYNC:
            self.eat(TokenType.ASYNC)
            self.eat(TokenType.PERFORM)
            action = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return AsyncNode(IdentifierNode(action))
            
        # e.g. "paint Player 'blue'"
        elif self.current_token.type == TokenType.PAINT:
            self.eat(TokenType.PAINT)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            color = self.current_token.value
            self.eat(TokenType.STRING)
            return PaintNode(IdentifierNode(target), StringNode(color))
            
        # e.g. "shape Player 'circle'"
        elif self.current_token.type == TokenType.SHAPE:
            self.eat(TokenType.SHAPE)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            shape = self.current_token.value
            self.eat(TokenType.STRING)
            return ShapeNode(IdentifierNode(target), StringNode(shape))
            
        # e.g. "breakpoint"
        elif self.current_token.type == TokenType.BREAKPOINT:
            self.eat(TokenType.BREAKPOINT)
            return BreakpointNode()
            
        elif self.current_token.type == TokenType.ABSORB:
            self.eat(TokenType.ABSORB)
            if self.current_token.type == TokenType.STRING:
                target = StringNode(self.current_token.value)
                self.eat(TokenType.STRING)
            elif self.current_token.type == TokenType.IDENTIFIER:
                target = StringNode(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
            else:
                target = StringNode(self.current_token.value)
                self.eat(self.current_token.type)
            return AbsorbNode(target)
            
        elif self.current_token.type == TokenType.NATIVE:
            self.eat(TokenType.NATIVE)
            code = StringNode(self.current_token.value)
            self.eat(TokenType.STRING)
            return ExecuteNativeNode(code)
            
        # e.g. "input 'Enter name: ' into username" or "input 'Age' to age"
        elif self.current_token.type == TokenType.INPUT:
            self.eat(TokenType.INPUT)
            prompt_str = self.current_token.value
            self.eat(TokenType.STRING)
            if self.current_token.type == TokenType.INTO:
                self.eat(TokenType.INTO)
            elif self.current_token.type == TokenType.TO:
                self.eat(TokenType.TO)
            target = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return InputNode(StringNode(prompt_str), IdentifierNode(target))

        msg = f"Liquid Matter didn't recognize the statement starting with: {self.current_token.value}"
        raise Exception(self.format_error(msg, self.current_token))

    def parse(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            statements.append(self.statement())
        return statements

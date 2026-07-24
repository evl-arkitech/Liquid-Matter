# Liquid Matter Comprehensive Thesaurus & Natural Language Synonym Map
# Normalizes user natural language phrasings into canonical Liquid Matter AST keywords

SYNONYM_MAP = {
    # SET / ASSIGNMENT SYNONYMS
    "make": "set",
    "assign": "set",
    "let": "set",
    "define_var": "set",
    "store": "set",
    "initialize_var": "set",
    "put": "set",

    # DISPLAY / OUTPUT SYNONYMS
    "print": "display",
    "show": "display",
    "log": "display",
    "output": "display",
    "echo": "display",
    "write_out": "display",
    "render_text": "display",

    # DEFINE FUNCTION SYNONYMS
    "create_action": "define action",
    "function": "define action",
    "func": "define action",
    "procedure": "define action",
    "def": "define action",
    "routine": "define action",

    # CALL FUNCTION SYNONYMS
    "run": "perform",
    "execute": "perform",
    "call": "perform",
    "invoke": "perform",
    "trigger_action": "perform",
    "launch": "perform",

    # ADD SYNONYMS
    "increment": "add",
    "increase": "add",
    "plus": "add",
    "sum": "add",

    # SUBTRACT SYNONYMS
    "decrement": "subtract",
    "decrease": "subtract",
    "minus": "subtract",
    "deduct": "subtract",

    # MULTIPLY SYNONYMS
    "scale": "multiply",
    "product": "multiply",

    # DIVIDE SYNONYMS
    "split": "divide",
    "partition": "divide",

    # IF / CONDITION SYNONYMS
    "when": "if",
    "whenever": "if",
    "provided": "if",
    "in_case": "if",

    # REPEAT / LOOP SYNONYMS
    "loop": "repeat",
    "iterate": "repeat",
    "cycle": "repeat",

    # ABSORB / IMPORT SYNONYMS
    "import": "absorb",
    "include": "absorb",
    "require": "absorb",
    "use": "absorb",
    "load_module": "absorb",

    # RETURN SYNONYMS
    "yield": "return",
    "give_back": "return",
    "pass_back": "return",

    # ATTEMPT / CATCH SYNONYMS
    "try": "attempt",
    "catch": "recover",
    "handle": "recover",

    # LIST SYNONYMS
    "array": "list",
    "collection": "list",
    "sequence": "list",
    "push": "append",
    "add_to_list": "append",
}

# Extensive technical dictionary words for domain coverage
TECHNICAL_KEYWORDS = [
    # AI & ML Primitives
    "NEURAL", "MODEL", "WEIGHTS", "BIAS", "TENSOR", "TRANSFORMER", "ATTENTION", "EMBEDDING",
    "VECTOR", "INFERENCE", "TRAIN", "PREDICT", "EPOCH", "LOSS", "OPTIMIZER", "GRADIENT",
    
    # 3D, WebGL & Graphic Primitives
    "MESH", "SHADOW", "LIGHTING", "TEXTURE", "SHADER", "MATERIAL", "CAMERA", "RENDERER",
    "CANVAS", "PIXEL", "RAYCAST", "ANIMATION", "FPS", "VIEWPORT", "TEXTURE_MAP",
    
    # Security, Cryptography & Network
    "ENCRYPT", "DECRYPT", "CYBER", "MATRIX", "HASH", "CIPHER", "VAULT", "SOCKET",
    "PROTOCOL", "PAYLOAD", "PACKET", "TOKEN", "AUTH", "CREDENTIAL", "TLS",
    
    # Database & System Storage
    "QUERY", "DATABASE", "TABLE", "ROW", "COLUMN", "INDEX", "TRANSACTION", "COMMIT",
    "ROLLBACK", "RECORD", "SCHEMA", "MIGRATE", "PERSIST",
    
    # Game Development & Physics
    "RIGIDBODY", "COLLIDER", "FORCE", "VELOCITY", "MASS", "FRICTION", "BOUNDS",
    "HITBOX", "SCORE", "SPAWN_POINT", "HEALTH_BAR", "PARTICLE",
]

def normalize_token(word):
    """Normalize input text/token through the Liquid thesaurus."""
    word_lower = word.lower().strip()
    return SYNONYM_MAP.get(word_lower, word)

7/24/2026

 ###  Complete List of Completed Updates:

  1. Infix Math Expressions & Compound Logic (parser.py, evaluator.py)
      ΓÇó Support for complex infix math operations (+, -, *, /, %, ^), parenthesized grouping ( ), and compound
      boolean expressions (and, or, not).
  2. Native Dictionary Data Structure (parser.py, evaluator.py)
      ΓÇó Added native statements for create dictionary <name>, set key <key> of <dict> to <val>, and get key <key>
      from <dict> into <var>.
  3. Line & Column Token Tracking & Syntax Error Callouts (lexer.py, parser.py)
      ΓÇó Every token tracks 1-indexed line and column numbers.
      ΓÇó Syntax and parser error tracebacks output code snippets with visual arrows (^).
  4. Module Resolution & Circular Absorption Safeguards (evaluator.py)
      ΓÇó Added loaded_modules set to prevent circular absorb infinite recursion stack overflows.
      ΓÇó Modules automatically resolve against the current working directory or the ./modules/ package folder.
  5. Engine Bug & QA Hardening Fixes (evaluator.py, water.py)
      ΓÇó Undefined Variable Fix: Missing variables raise clean Liquid Error instead of Python NameError.
      ΓÇó Scope Isolation Fix: set local properly confines variables inside function scopes without mutating outer
      variables.
      ΓÇó Windows CP1252 Fix: Resolved Unicode block ASCII printing issues in water.py.
      ΓÇó Async Thread Life Cycle: Async tasks spawned by async perform are tracked by the evaluator.

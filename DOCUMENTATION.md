# 💧 Liquid Matter - Official Documentation (v2.0)

Welcome to the official documentation for **Liquid Matter**, the English-based programming language built for speed, readability, and scale.

---

## 1. Variables and Math
Variables in Liquid Matter are declared using the `set` keyword. You can store numbers, strings, and use complex math. By default, variables are globally accessible.

```text
|| Basic Variables
set player_name to "EVL"
set score to 100

|| Math Operations
add 50 to score
subtract 10 from score
multiply score by 2
divide score by 4
```

### Local Scopes (Enterprise V2)
If you only want a variable to exist inside a specific function (so it doesn't clutter global memory), use the `local` keyword:
```text
define action calculateBonus
    set local bonus to 500
    add bonus to score
end
```

---

## 2. String Interpolation
You can inject variables directly into text using curly braces `{}`.

```text
set user to "EVL"
set level to 99
display "Welcome back {user}! You are currently level {level}."
```

---

## 3. Native Lists (Arrays)
Liquid Matter natively supports arrays (Lists) and looping through them seamlessly.

```text
create list Enemies containing "Goblin", "Orc", "Troll"
append "Dragon" to Enemies

for each enemy in Enemies perform
    display "A wild {enemy} appears!"
end
```

---

## 4. Conditional Logic (If / Else)
Control the flow of your program with english logic gates.

```text
set health to 40

if health is less than 50 then
    display "Warning: Low Health!"
else
    display "You are healthy."
end
```

---

## 5. Web and APIs (Fetch)
You can directly fetch data from live web servers and parse JSON objects.

```text
fetch "https://api.github.com/users/evl-arkitech" into response
parse JSON from response into userData
get "name" from userData into githubName

display "Found user: {githubName}"
```

---

## 6. The 2D Arcade Engine
Liquid Matter has a built-in 2D physics engine. You can spawn vectors, move them, and bind them to keys.

```text
|| Spawn a Red Circle
paint Player "red"
shape Player "circle"
spawn Player at 0 0

|| Move it
define action moveUp
    move Player up
end
bind "w" to moveUp
```

---

## 7. The 3D High-Def Engine (Ursina)
Liquid Matter Enterprise v2.0 includes a fully native 3D engine. You can build 3D worlds, run game loops, and track collisions.

```text
|| Boot 3D Engine
IntentionTO "Start 3D Engine"

paint Car "cyan"
shape Car "cube"
spawn Car at 0 0

|| Procedural Engine Update Loop (60 FPS)
define action gameLoop
    move Car forward
    
    || Random Generation
    set randomX to random between -5 and 5
    paint Obstacle "red"
    shape Obstacle "cube"
    spawn Obstacle at randomX 50
end

on update perform gameLoop

IntentionTO "Keep 3D Engine Running"
```

---

## 8. Package Management (WATER)
Liquid Matter includes the **WATER** package manager. You can pull code directly from the global registry (hosted by `evl-arkitech`).

To install a package, open your terminal and run:
`python water.py install package_name`

---
*Liquid Matter Engine is governed by the EVL Public License (EPL 1.0).*

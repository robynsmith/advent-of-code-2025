# Day 1 Solutions Analysis

A review of approaches shared in the [r/adventofcode solutions thread](https://www.reddit.com/r/adventofcode/comments/1pb3y8p/2025_day_1_solutions/).

---

## Two Main Approaches

### Approach A: Simulation (Click-by-Click)

Simulate each individual click of the dial:

```python
for _ in range(distance):
    position = (position + direction) % 100
    if position == 0:
        count += 1
```

- Straightforward to implement
- No edge cases to reason about
- Slower for large distances, but fast enough for this puzzle's input

### Approach B: Mathematical (Division-Based)

Calculate zeros crossed using integer division:

```python
# For right movement
zeros = (position + distance) // 100
```

- O(n) time complexity (n = number of instructions)
- Requires careful handling of edge cases
- More elegant once working

---

## The `divmod` Technique

Several Python solutions used `divmod()` to separate full rotations from partial rotations:

```python
full, partial = divmod(distance, 100)
zero_count += full  # Full rotations definitely cross zero

# Then handle the partial rotation separately
```

This splits the problem into two simpler sub-problems.

---

## Common Challenges (Part 2)

| Challenge | Description |
|-----------|-------------|
| **Negative modulo** | Some languages return negative values for `(-5) % 100`. Python returns `95`. |
| **Double counting** | Starting at 0 and moving away—does that count as "passing through" 0? |
| **Landing vs passing** | Does landing exactly on 0 count differently than passing through? |
| **Large rotations** | `R1000` from position 50 crosses 0 ten times—easy to miss this case |

Many developers reported struggling with edge cases:

> *"100000 off by one errors later..."*

> *"I tried to be clever... but I couldn't get it to work, so I just did the naive approach"*

> *"My original algorithm didn't work at all, but the incorrect individual results ended up with the correct total"*

---

## Alternative Languages

People solved this puzzle in a wide variety of languages:

| Language | Notes |
|----------|-------|
| SQL (DuckDB) | Solved entirely with SQL queries |
| Uiua | Array programming language |
| AWK | Unix text processing |
| Vim keystrokes | Solved by editing the input file directly |
| Google Sheets | Spreadsheet formulas |
| m4 | The macro processor |
| Brainfuck | No signed numbers made left rotations difficult |

---

## Tricks and Observations

- **Treating 0 as 100:** Some avoided edge cases by internally representing position 0 as 100

- **Bucket thinking:** One solver thought of ranges like `-99:-1`, `1:99`, `101:199` as "buckets"—counting bucket crossings equals counting zeros

- **Symmetry exploitation:** When the dial hits zero and reverses direction, it either counts twice or not at all—some solutions exploited this symmetry

- **Test-driven debugging:** Several people wrote brute-force solutions first, then used them to verify their mathematical solutions

---

## Takeaways

- Part 1 was straightforward for most
- Part 2's edge cases tripped up many experienced developers
- Both simulation and mathematical approaches are valid
- When in doubt, a working brute-force solution can help verify a more elegant one

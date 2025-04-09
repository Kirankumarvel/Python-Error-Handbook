# 🐍 Python Error Handbook

> A beginner-friendly guide to the most common Python errors — what they mean, why they happen, and how to fix them — with examples.  

## 🚀 Overview

If you're new to Python or even an intermediate dev, chances are you've seen errors that left you scratching your head. This repo is your quick reference guide for:

- Understanding common Python errors
- Identifying their root causes
- Learning how to fix them effectively

---

## 🧠 Error Cheat Sheet

| S.No | Error Type                          | What It Means                                     | Example                                | How to Fix                                                  |
|------|-------------------------------------|--------------------------------------------------|----------------------------------------|-------------------------------------------------------------|
| 1    | `SyntaxError`                      | Python can't understand the code syntax          | `if x > 5`                              | Add `:` → `if x > 5:`                                       |
| 2    | `NameError`                        | Using a variable/function that doesn’t exist     | `print(score)`                          | Define it first → `score = 10`                              |
| 3    | `TypeError`                        | Wrong data type used in an operation             | `"Age: " + 25`                          | Convert type → `"Age: " + str(25)`                          |
| 4    | `ValueError`                       | Right type, but invalid value                    | `int("abc")`                            | Use valid value → `int("123")`                              |
| 5    | `IndexError`                       | Accessing an invalid list index                  | `nums = [1,2,3]; nums[5]`               | Check length before access                                  |
| 6    | `KeyError`                         | Dictionary key doesn’t exist                     | `data['b']`                             | Use `.get()` or check with `in`                             |
| 7    | `AttributeError`                   | Object lacks the method/attribute                | `5.append(10)`                          | Use correct object type → e.g., `list.append()`             |
| 8    | `ImportError / ModuleNotFoundError`| Python can’t find the module                     | `import numppy`                         | Fix name / install → `pip install numpy`                    |
| 9    | `ZeroDivisionError`                | Division by zero                                 | `10 / 0`                                | Check denominator before dividing                           |
| 10   | `IndentationError`                 | Improper code indentation                        | `def f():\nprint("Hi")`                 | Use consistent spaces (4 spaces or a tab)                   |

---

## 🛠️ How to Use

You can:
- Bookmark this repo as your quick reference
- Copy-paste the error examples to test yourself
- Use it in your team onboarding or tutorials
- Expand it with your own examples and PRs

---

## 💡 Contributing

Found a weird error or want to add more examples?

- Fork this repo
- Add your error and explanation
- Submit a Pull Request ✅

---

## 📚 Related Resources

- [Python Official Docs](https://docs.python.org/3/)
- [Real Python](https://realpython.com)
- [w3schools Python Tutorial](https://www.w3schools.com/python/)

---

## 📜 License

MIT License. Use, modify, share freely.

---

## 🙌 Let's Connect

Created by [Kiran Kumar](https://github.com/Kirankumarvel) — SEO guy turned Python enthusiast 🐍

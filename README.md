# What's in the Drawer?

A Python program that simulates managing the contents of a drawer using a list. You can search for items, add new ones, remove existing ones, and count everything inside.

## What It Does

- Search for any item in the drawer
- List everything currently inside
- Add new items (with duplicate detection)
- Remove items
- Count total items
- Built-in help guide with the `?` command

## How to Run

```bash
python WhatsInTheDrawer.py
```

## Commands

| Command | What It Does |
|---------|-------------|
| `LIST`  | Show all items in the drawer |
| `COUNT` | Count how many items are inside |
| `PUT`   | Add a new item |
| `GET`   | Remove an item |
| `STOP`  | Exit the program |
| `?`     | Show the help guide |
| anything else | Search for that item |

## Example

```
What's in the drawer?
Type '?' to get a full guide of the program.
What are you looking for? keys

There is a keys in the drawer

What are you looking for? LIST
1 : pens
2 : pencils
3 : eraser
...
```

## Why I Built It

Built as a Grade 11 CS project to practice Python lists, functions, input validation, and building interactive command-line programs.

## Built With

Python 3

# Insert to Column
_Insert to Column_ is a simple package that allows you to insert a character (or characters) of your choice up to a certain column on all selected lines.

## Installation
The recommended way to install this package is through [Package Control](https://packagecontrol.io/), but you can also download this repository or the `sublime-package` file from the [latest release](https://github.com/abluescarab/sublime_insert-to-column/releases/latest) and drop it into your _Installed Packages_ folder.

## Command
You can access "Insert to Column" from the command palette or bind a key to the command `insert_to_column`.

### Arguments
The script takes only two arguments:
* `character_to_insert`: _optional._ A character of your choice to insert. If not supplied, it will ask before continuing.
* `column_index`: _optional._ The column index to insert to. If not supplied, it will ask before continuing.
    * Example: if the cursor is at the beginning of a line, a value of `20` will insert 19 characters and place the cursor at column 20

### Keybinding
    {
        "keys": ["ctrl+alt+c"],
        "command": "insert_to_column",
        "args":
            {
                "character_to_insert": " ",
                "column_index": 20
            }
    }

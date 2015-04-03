# Insert to Column
_Insert to Column_ is a simple package that allows you to insert a character of your choice up to a certain column on all selected lines.

## Command
You can bind a key to the command `insert_to_column` to use the script.

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
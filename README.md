# Insert to Column
_Insert to Column_ is a simple package that allows you to insert a character of your choice up to a certain column on all selected lines.

## Command
You can bind a key to the command `insert_to_column` to use the script.

### Arguments
The script takes only two arguments:
* `character_to_insert`: required. A character of your choice to insert.
* `column_index`: optional. If not supplied, it will ask before continuing. The column index to insert to.
    * Example: if the cursor is at the beginning of a line, a value of `50` will insert 49 characters and place the cursor at column 50

### Keybinding
    {
        "keys": ["ctrl+alt+c"],
        "command": "insert_to_column",
        "args":
            {
                "character_to_insert": " ",
                "column_index": 50
            }
    }
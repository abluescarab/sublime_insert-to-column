import sublime, sublime_plugin

class InsertToColumnCommand(sublime_plugin.WindowCommand):
    def run(self, character_to_insert="", column_index=0):
        # create class-wide variables
        self.character_to_insert = character_to_insert
        self.column_index = column_index
        
        if(len(character_to_insert) == 1):
            self.on_character_to_insert(character_to_insert)
        else:
            self.window.show_input_panel(
                "Character to insert:",
                "",
                self.on_character_to_insert,
                None,
                None)
        pass

    def on_character_to_insert(self, character_to_insert):
        self.character_to_insert = character_to_insert

        if(self.column_index > 0):
            self.insert(character_to_insert, self.column_index)
        else:
            self.window.show_input_panel(
                "Column index:",
                "",
                self.on_column_index,
                None,
                None)
        pass

    def on_column_index(self, column_index):
        self.insert(self.character_to_insert, column_index)

    def insert(self, character_to_insert, column_index):
        try:
            if(self.window.active_view()):
                self.window.active_view().run_command(
                    "do_insert_to_column",
                    {
                        "character_to_insert": character_to_insert,
                        "column_index": int(column_index)
                    })
        except ValueError:
            pass

class DoInsertToColumnCommand(sublime_plugin.TextCommand):
    def run(self, edit, character_to_insert, column_index):
        # iterates through all cursors
        for region in self.view.sel():
            # gets the column number of the selection start
            reg_index = self.view.rowcol(region.begin())[1]

            # if we are still ahead of the provided column index,
            if(reg_index < column_index):
                # then calculate it
                count = column_index - reg_index - 1 # -1 for zero-base
                # and insert it.
                self.view.insert(edit, region.begin(), self.repeat(
                    character_to_insert, count))

    def repeat(self, str, count):
        return str * count
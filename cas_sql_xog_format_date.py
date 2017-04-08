import sublime, sublime_plugin

class CasSqlXogFormatDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            randomized_text = "to_char(" + region_text + ", 'YYYY-MM-DD\"T\"HH24:MI:SS')"
            self.view.replace(edit, region, randomized_text)
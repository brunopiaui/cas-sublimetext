import sublime, sublime_plugin

class CasSqlLowerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            randomized_text = "lower(" + region_text + ")"
            self.view.replace(edit, region, randomized_text)
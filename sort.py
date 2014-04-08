import sublime
import sublime_plugin
from isort.isort import SortImports


class PysortCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        old_content = self.view.substr(sublime.Region(0, self.view.size()))
        new_content = SortImports(file_contents=old_content).output
        self.view.replace(edit, sublime.Region(0, self.view.size()), new_content)
        sublime.status_message("Python sort import complete.")
        sublime.run_command('sub_notify', {'title': 'ISort', 'msg': 'Python sort import complete.', 'sound': False})

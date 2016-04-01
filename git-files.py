import sublime, sublime_plugin, os, subprocess

class ExampleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sublime.run_command("new_window")
        sublime.active_window().set_layout({
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 0.5, 1.0],
            "cells": [[0, 0, 1, 1], [1, 0, 2, 1], [0, 1, 1, 2], [1, 1, 2, 2]]
        })
        settings = sublime.load_settings("Preferences.sublime-settings")

        proc = subprocess.Popen(["cd " + settings.get("git_folder") + "; git diff master --name-only"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        files = out.splitlines();

        fileExtensions = self.splitUpByFileExtension(files)

        group_num = 0;
        for k, v in fileExtensions:
            sublime.active_window().focus_group(group_num)
            for file in v:
                sublime.active_window().open_file(settings.get("git_folder") + file);
            if group_num <= 3:
                group_num = group_num + 1
        
    def splitUpByFileExtension(self, files):
        results = []

        for file in files:
            filename, file_extension = os.path.splitext(file.decode("utf-8"))
            print (filename);
            print (file_extension);
            found = False;
            for k, v in results:
                if file_extension == k:
                    v.append(file.decode('utf-8'))
                    found = True;

            if not found:
                results.append((file_extension, [file.decode("utf-8")]))

        results.sort(key=lambda t: len(t[1]), reverse=True)
        
        return results;
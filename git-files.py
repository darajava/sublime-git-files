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

        proc = subprocess.Popen(["cd " + settings.get("git_folder") + "; git diff --name-only"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        files = out.splitlines();

        for file in files:
            print (file)
            sublime.active_window().open_file(settings.get("git_folder") + file.decode("utf-8"));
        

import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.run_command("new_window")
		sublime.active_window().set_layout({
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 0.5, 1.0],
            "cells": [[0, 0, 1, 1], [1, 0, 2, 1], [0, 1, 1, 2], [1, 1, 2, 2]]
        })

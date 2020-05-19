import time

from talon.voice import Key, Context, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
from talon import ctrl, ui

from ..utils import parse_words, text, is_in_bundles, insert
from .. import config
from ..misc.switcher import switch_app
from ..bundle_groups import TERMINAL_BUNDLES

ctx = Context("iterm", bundle="com.googlecode.iterm2")

keymap = {
    "drill":"../",
    "head": "head ",

	"opower":"opower",
	"out":"out",
	"ops":"ops",
    "broadcaster": Key("cmd-alt-i"),
    "password": Key("cmd-alt-f"),
    # Pane creation and navigation
    "split horizontal": Key("cmd-shift-d"),
    "split vertical": Key("cmd-d"),
    "rivers": "../",
    "search":Key("ctrl-r"),
    "cancel":Key("ctrl-c"), 
    "pane next": Key("cmd-]"),
    "pane last": Key("cmd-["),

    "direct": "pwd ",
    "shell home": "~/",
    "lefty": Key("ctrl-a"),
    "ricky": Key("ctrl-e"),
    "clear back": Key("ctrl-u"),
    "clear line": [Key("ctrl-e"), Key("ctrl-u")],
    "(pain new | split vertical)": Key("cmd-d"),
    # "new [S S H] [tab] {global_terminal.servers}": new_server,
    # talon
    "tail talon [log]": "tail -f ~/.talon/talon.log",
    "talon reple": "~/.talon/bin/repl",
    "reverse": Key("ctrl-r"),
    "rerun": [Key("up"), Key("enter")],
    "go": ["cd ; ls", Key("left"), Key("left"), Key("left"), Key("left")],
    "cd wild": [
        "cd **; ls",
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
    ],
    "cd wild [<dgndictation>]": [
        "cd **; ls",
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        # text,
    ],
    # "cd {terminal.directory_shortcuts}": cd_directory_shortcut,
    # "directory {terminal.directory_shortcuts}": name_directory_shortcuts,
    "(spill | run ellis | run alice)": "ls",
    "(la | run la)": "ls -la\n",
    # "durrup": "cd ..; ls\n",
    "go back": "cd -\n",
    # "dash <dgndictation> [over]": dash,
    "pseudo": "sudo ",
    "(redo pseudo | pseudo [make me a] sandwich)": [
        Key("up"),
        Key("ctrl-a"),
        "sudo ",
        Key("enter"),
    ]
}

ctx.keymap(keymap)
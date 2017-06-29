define config.name = _("To Libertad")
define gui.show_name = True
define config.version = "1.1.11"
define gui.about = _("")
define build.name = "To_Libertad"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.main_menu_music = audio.main_menu_music
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve
define config.window = "auto"
define config.window_show_transition = Dissolve(.1)
define config.window_hide_transition = Dissolve(.1)
default preferences.text_cps = 40
default preferences.afm_time = 15
define config.save_directory = "To Libertad"
define config.window_icon = "gui/window_icon.webp"
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy', None)
    build.classify('game/saves/**', None)
    build.classify('game/tl/**.rpym', None)
    build.archive('senpai')
    build.classify('game/tl/**.rpymc', 'senpai')
    build.classify('game/**.webp', 'senpai')
    build.classify('game/**.jpg', 'senpai')
    build.classify('game/**.png', 'senpai')
    build.classify('game/**.rpyc', 'senpai')
    build.classify('game/sounds/**.ogg', 'senpai')
    build.classify('game/**.ttf', 'senpai')
    build.documentation('*.html')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

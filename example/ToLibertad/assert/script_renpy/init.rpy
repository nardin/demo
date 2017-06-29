init python early:
    def callback_transition(event, interact=True, **kwargs):
        if interact and event == "begin":
            renpy.transition(Dissolve(0.1), layer='master')
define adv2 = Character(None, callback=callback_transition)
define slave = Character(_('Рабыня'), image="ada", kind=adv2)
define warrior = Character(_('Воин'), image="martha", kind=adv2)
define s1 = Character(_('Работорговец 1'), kind=adv2)
define s2 = Character(_('Работорговец 2'), kind=adv2)
define s3 = Character(_('Работорговец 3'), kind=adv2)
define g1 = Character(_('Гоблин 1'), kind=adv2)
define g2 = Character(_('Гоблин 2'), kind=adv2)
define a = Character(_('Ада'), image="ada", kind=adv2)
define m = Character(_('Марта'), image="martha", kind=adv2)
define monster = Character(_('Монстр'), kind=adv2)
define ogre = Character(_('Огр'), kind=adv2)
define locksmith = Character(_('Слесарь'), kind=adv2)
define narrator = Character(None, show_two_window=False, kind=adv2)
transform change_transform(old, new):
    contains:
        old
        xalign gui.side_sprite_xalign
        yalign 1.0
        alpha 1.0
        linear 0.2 alpha 0.0
    contains:
        new
        xalign gui.side_sprite_xalign
        yalign 1.0
        alpha 0.0
        linear 0.2 alpha 1.0
transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)
define config.side_image_same_transform = same_transform
define config.side_image_change_transform = change_transform
image white = '#EEE'
image martha_closeup = LiveCrop((1100, 850, 1920, 2160), 'cg_s1_martha_intro')
default martha_shield = 'shield'
default ada_clean = False
default ada_collar = True
default ada_cloak = False
default back_button = ['mouseup_3', 'K_ESCAPE', 'K_AC_BACK']
define generator = ParticleGenerator(Image('gui/particle.webp'),y=config.screen_height/3*2+100, max_age=15.0, count=64)
define interface_font_size = 38
init python:
    _game_menu_screen = None
    current_scene = 'scene_1'
    renpy.music.register_channel('ambient', 'music')
    config.keymap['help'] = None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

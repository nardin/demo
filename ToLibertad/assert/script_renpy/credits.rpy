image credits_bg = '#f7f6eb'
transform cred_fade(d):
    on show:
        alpha 0.0
        linear d alpha 1.0
    on hide:
        alpha 1.0
        linear 1.0 alpha 0.0
screen creds(header, txt, d):
    vbox:
        at cred_fade(d)
        xalign 0.5
        yalign 0.5
        text header xalign 0.5 size 64 color '#a69578'
        for i in txt:
            text i xalign 0.5 size 72 color '#bdb4a5'
transform fin_image:
    alpha 0.0
    linear 10.0 alpha 1.0
screen fin():
    add 'fin' at fin_image
    key 'mouseup_1' action Return()
    key 'K_ESCAPE' action Return()
label credits:
    show credits_bg
    show credits:
        xalign 0.5
        yalign 0.5
        alpha 0
        linear 3.0 alpha 1.0
    $ renpy.pause(5.0,hard=True)
    queue music audio.healing_begins
    hide credits with Dissolve(5)
    show screen creds('История от:', ['Sendo'], 1)
    $ renpy.pause(6, hard=True)
    hide screen creds
    $ renpy.pause(1, hard=True)
    show screen creds('Написано:', ['Zetsubou'], 1)
    $ renpy.pause(6, hard=True)
    hide screen creds
    $ renpy.pause(1, hard=True)
    show screen creds('Арт & Программирование:', ['Sendo'], 1)
    $ renpy.pause(6, hard=True)
    hide screen creds
    $ renpy.pause(1, hard=True)
    show screen creds('Производство:', ['Studio Camelot'], 1)
    $ renpy.pause(6, hard=True)
    hide screen creds
    $ renpy.pause(1, hard=True)
    show screen creds('Музыка:', ['Грегуар Лурме', 'Epic Soul Factory', 'ANtarcticbreeze', 'Avel Glas', 'JTiKey'], 1)
    $ renpy.pause(10, hard=True)
    hide screen creds
    $ renpy.pause(1, hard=True)
    show screen creds('Звуки:', ['Sound Effect Lab'], 1)
    $ renpy.pause(6, hard=True)
    hide screen creds
    $ renpy.pause(1, hard=True)
    show screen creds('Команда Русификаторов Gardares:', ['Воин Света Гардарик', 'Девушка-Дракон Риа', 'Бард Миса', 'и многие другие…'], 1)
    $ renpy.pause(6, hard=True)
    hide screen creds
    $ renpy.pause(1, hard=True)
    show screen creds('Сделано с помощью:', ['Ren\'py'], 1)
    $ renpy.pause(6, hard=True)
    hide screen creds
    $ renpy.pause(1, hard=True)
    show screen creds('Сделано для:', ['YuriJam 2016'], 1)
    $ renpy.pause(6, hard=True)
    hide screen creds
    $ renpy.pause(1, hard=True)
    show screen creds('Спасибо вам за игру!', [' '], 1)
    pause 5
    hide screen creds
    $ renpy.pause(1, hard=True)
    call screen fin
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

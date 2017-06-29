init -1 style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
init -1 style input:
    color gui.accent_color
init -1 style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True
init -1 style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size
init -1 style button:
    properties gui.button_properties("button")
init -1 style button_text is gui_text:
    properties gui.button_text_properties("button")
    outlines [(0,'#181310',-1,1)]
    yalign 0.5
init -1 style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size
init -1 style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size
init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)
init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)
init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"
init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"
init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)
init -501 screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            add 'gui/textbox_nameplate.webp' xoffset 220 yoffset 40
            text who.upper() id "who" font gui.default_font
        if who is None:
            text what id "what"
        else:
            text what id "what" yoffset 50
    add SideImage() xalign gui.side_sprite_xalign yalign 1.0
    use quick_menu
init -501 screen ctc():
    frame:
        at ctc_transform
        xalign 0.5
        yalign 1.0
        background None
        add 'gui/ctc.webp'
transform -1 ctc_transform:
    alpha 0.0
    pause 0.7
    block:
        linear 0.5 alpha 1.0
        pause 0.75
        ease 0.25 yoffset 10
        ease 0.25 yoffset 0
        repeat
init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue
init -1 style namebox is default
init -1 style namebox_label is say_label
init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)
init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
init -1 style say_label:
    color '#dbd5b9'
    font gui.name_font
    size 47
    xpos 510
    ypos 47
init -1 style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")
    outlines [(0,'#181310',-1,1)]
init -501 screen input(prompt):
    style_prefix "input"
    window:
        has vbox:
            xpos gui.text_xpos
            xanchor gui.text_xalign
            ypos gui.text_ypos
        text prompt style "input_prompt"
        input id "input"
init -1 style input_prompt is default
init -1 style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign
init -1 style input:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign
init -501 screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action
define -1 config.narrator_menu = True
init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text
init -1 style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing
init -1 style choice_button is default:
    properties gui.button_properties("choice_button")
init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
init -501 screen quick_menu():
    grid 2 3:
        xalign 1.0
        xoffset -50
        yalign 1.0
        yoffset -20
        spacing 10
        textbutton _("авто") action Preference("auto-forward", "toggle") text_font gui.interface_font
        textbutton _("проп") action Skip() alternate Skip(fast=True, confirm=True) text_font gui.interface_font
        textbutton _("сохр") action [FileTakeScreenshot(), Show('save')] text_font gui.interface_font
        textbutton _("загр") action Show('load') text_font gui.interface_font
        textbutton _("меню") action Show('preferences') text_font gui.interface_font
        textbutton _("мут") action Preference("all mute", "toggle") text_font gui.interface_font
init -501 screen modal():
    add 'gui/modal.webp' at modal_bg_transform
transform -1 modal_bg_transform():
    xalign 0.5
    yalign 0.5
    on show:
        alpha 0.0
        zoom 2.0
        parallel:
            easein 0.35 alpha 1.0
        parallel:
            easein 0.35 zoom 1.0
    on hide:
        alpha 1.0
        zoom 1.0
        parallel:
            easein 0.5 alpha 0.0
        parallel:
            easein 0.5 zoom 2.0
init -501 screen my_help():
    use modal
    use modal
    modal True
    hbox:
        xalign 0.5
        yalign 0.5
        style_prefix "my_help"
        vbox:
            label _("Клавиатура") text_font gui.interface_font
            null height 10
            hbox:
                label _("Enter") text_font gui.interface_font
                text _("Прохождение диалогов и активация интерфейса.") font gui.interface_font
            hbox:
                label _("Пробел") text_font gui.interface_font
                text _("Прохождение диалогов, но не позволяет делать выбор.") font gui.interface_font
            hbox:
                label _("Стрелки") text_font gui.interface_font
                text _("Навигация по интерфейсу.") font gui.interface_font
            hbox:
                label _("Esc") text_font gui.interface_font
                text _("Вход в игровое меню.") font gui.interface_font
            hbox:
                label _("Ctrl") text_font gui.interface_font
                text _("Пропускает диалоги, пока зажат.") font gui.interface_font
            hbox:
                label _("Tab") text_font gui.interface_font
                text _("Включает режим пропуска.") font gui.interface_font
            hbox:
                label _("Page Up") text_font gui.interface_font
                text _("Возврат назад по сюжету игры.") font gui.interface_font
            hbox:
                label _("Page Down") text_font gui.interface_font
                text _("Откатывает предыдущее действие вперёд.") font gui.interface_font
            hbox:
                label "H" text_font gui.interface_font
                text _("Скрывает интерфейс пользователя.") font gui.interface_font
            hbox:
                label "S" text_font gui.interface_font
                text _("Делает снимок экрана.") font gui.interface_font
            hbox:
                label "V" text_font gui.interface_font
                text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.") font gui.interface_font
            null height 10
            label _("Мышь") text_font gui.interface_font
            null height 10
            hbox:
                label _("Левый клик") text_font gui.interface_font
                text _("Прохождение диалогов и активация интерфейса.") font gui.interface_font
            hbox:
                label _("Средний клик") text_font gui.interface_font
                text _("Скрывает интерфейс пользователя.") font gui.interface_font
            hbox:
                label _("Правый клик") text_font gui.interface_font
                text _("Вход в игровое меню.") font gui.interface_font
            hbox:
                label _("Колёсико вверх\nКлик на сторону отката") text_font gui.interface_font
                text _("Возврат назад по сюжету игры.") font gui.interface_font
            hbox:
                label _("Колёсико вниз") text_font gui.interface_font
                text _("Откатывает предыдущее действие вперёд.") font gui.interface_font
            null height 10
            label _("Геймпад") text_font gui.interface_font
            hbox:
                label _("Правый триггер\nA/Нижняя кнопка") text_font gui.interface_font
                text _("Прохождение диалогов и активация интерфейса.") font gui.interface_font
            hbox:
                label _("Левый Триггер\nЛевый Бампер") text_font gui.interface_font
                text _("Возврат назад по сюжету игры.") font gui.interface_font
            hbox:
                label _("Правый бампер") text_font gui.interface_font
                text _("Откатывает предыдущее действие вперёд.") font gui.interface_font
            hbox:
                label _("Крестовина, Стики") text_font gui.interface_font
                text _("Навигация по интерфейсу.") font gui.interface_font
            hbox:
                label _("Start, Guide") text_font gui.interface_font
                text _("Вход в игровое меню.") font gui.interface_font
            hbox:
                label _("Y/Верхняя кнопка") text_font gui.interface_font
                text _("Скрывает интерфейс пользователя.") font gui.interface_font
            textbutton _("Калибровка") action GamepadCalibrate() text_font gui.interface_font
            null height 20
            textbutton "back" action Hide('my_help') xalign 0.5 text_size 48 text_font gui.interface_font
    for i in back_button:
        key i action Hide('my_help')
    key 'mouseup_1' action Hide('my_help')
    key 'K_F1' action Hide('my_help')
init -1 style my_help_text:
    color '#e0d4c0'
    size 32
init -1 style my_help_label_text:
    color '#e0d4c0'
    size 32
init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text
init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
transform -1 logo:
    alpha 0
    xalign 0.5
    yalign 0.5
    ease 1.0 alpha 1.0
    pause 2
    ease 1.0 alpha 0.0
transform -1 splash:
    alpha 1
    pause 3.0
    ease 1.0 alpha 0
init 499 image splash_title = 'gui/title.jpg'
init 499 image splash_logo = 'gui/logo.webp'
init 499 image splash_white = '#FFF'
init 499 image splash_logogard = 'gui/LogoGard.webp'
label splashscreen:
    show splash_title
    show splash_white
    show splash_logogard at logo with Dissolve(2)
    $ renpy.pause(3, hard=True)
    hide splash_logogard with dissolve
    show splash_logo at logo
    $ renpy.pause(5, hard=True)
    hide splash_white with dissolve
    $ renpy.pause(0.5, hard=True)
    return
transform -1 mm_button:
    alpha 0.0
    ease 1.0 alpha 1.0
init -501 screen main_menu() tag menu:
    style_prefix "main_menu"
    add 'gui/title.jpg'
    add generator
    hbox:
        xalign 0.5
        ypos 865
        spacing 100
        style_prefix "main_menu"
        textbutton _("Начать") action Start() text_font gui.interface_font at mm_button
        textbutton _("Загрузить") action ShowMenu("load") text_font gui.interface_font at mm_button
        textbutton _("Настройки") action Show("preferences") text_font gui.interface_font at mm_button
        if persistent.extras_unlocked:
            textbutton _("Экстра") action ShowMenu("extras") text_font gui.interface_font at mm_button
        else:
            textbutton _("Экстра") action None text_font gui.interface_font at mm_button
        textbutton _("Выход") action Quit(confirm=True) text_font gui.interface_font at mm_button
init -1 style main_menu_button_text:
    outlines []
    hover_color '#AAA'
init -501 screen game_menu(title, scroll=None):
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    style_prefix "game_menu"
    frame:
        style "game_menu_outer_frame"
        has hbox
        frame:
            style "game_menu_navigation_frame"
        frame:
            style "game_menu_content_frame"
            if scroll == "viewport":
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_yfill True
                    has vbox
                    transclude
            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    yinitial 1.0
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_yfill True
                    transclude
            else:
                transclude
    use navigation
    textbutton _("Вернуться"):
        style "return_button"
        action Return()
    label title
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar
init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text
init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text
init -1 style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/game_menu.webp"
init -1 style game_menu_navigation_frame:
    xsize 420
    yfill True
init -1 style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15
init -1 style game_menu_viewport:
    xsize 1380
init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable
init -1 style game_menu_side:
    spacing 15
init -1 style game_menu_label:
    xpos 75
    ysize 180
init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
define -1 gui.about = ""
init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text
init -1 style about_label_text:
    size gui.label_text_size
init -501 screen save():
    modal True
    use modal
    use file_slots(_("save"))
init -501 screen load():
    modal True
    use modal
    use file_slots(_("load"))
init -501 screen file_slots(title):
    add 'gui/ui_modal_frame.webp' xalign 0.5 yalign 0.5 at ystretch(0.1)
    add 'gui/ui_modal_frame_borders.webp' xalign 0.5 yalign 0.5 at ystretch(0.2)
    text title.upper() xpos 500 ypos 315 color gui.hover_color size 55 at delayed_fade(0.2, 0.2)
    text _('Страница ') + FilePageName() xpos 940 ypos 400 style 'pref_label' size 32 at delayed_fade(0.2, 0.2)
    hbox:
        at delayed_fade(0.2, 0.2)
        yalign 0.5
        xalign 0.5
        xoffset 10
        yoffset -10
        for i in range(3):
            $ slot = i + 1
            frame:
                background None
                xsize 340
                ysize 200
                has button:
                    xsize 294
                    ysize 168
                    add 'gui/ui_file_slot.webp'
                    add FileScreenshot(slot) xoffset 3 yoffset 3
                    text FileTime(slot, format="{#file_time}%d %b %Y, %H:%M", empty="") style 'pref_label' size 22 yalign 1.0 xoffset -290 yoffset 40
                    key "save_delete" action FileDelete(slot)
                    action FileAction(slot)
    hbox:
        at delayed_fade(0.2, 0.2)
        xalign 0.5
        yalign 0.60
        yoffset 15
        spacing 10
        imagebutton idle 'gui/ui_prev_button.webp' hover 'gui/ui_prev_button.webp' action FilePagePrevious() yoffset 12
        for page in range(1, 6):
            textbutton " [page] " action FilePage(page)
        imagebutton idle 'gui/ui_next_button.webp' hover 'gui/ui_next_button.webp' action FilePageNext() yoffset 12
    hbox:
        at delayed_fade(0.2, 0.2)
        xalign 0.5
        ypos 710
        spacing 40
        textbutton _("назад") action Hide(title) style 'pref_buttons'
    key 'K_LEFT' action FilePagePrevious()
    key 'repeat_K_LEFT' action FilePagePrevious()
    key 'K_RIGHT' action FilePageNext()
    key 'repeat_K_RIGHT' action FilePageNext()
    use common_hide(title)
init -501 screen file_slots2(title):
    default page_name_value = FilePageNameInputValue()
    use game_menu(title):
        fixed:
            order_reverse True
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("пустой слот")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                textbutton _("{#auto_page}А") action FilePage("auto")
                textbutton _("{#quick_page}Б") action FilePage("quick")
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()
init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text
init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text
init -1 style page_label:
    xpadding 75
    ypadding 5
init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
init -1 style page_button:
    properties gui.button_properties("page_button")
init -1 style page_button_text:
    properties gui.button_text_properties("page_button")
init -1 style slot_button:
    properties gui.button_properties("slot_button")
init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")
init -501 screen common_hide(hide_screen):
    for i in back_button:
        key i action Hide(hide_screen)
init -501 screen preferences():
    modal True
    use modal
    add 'gui/ui_modal_frame.webp' xalign 0.5 yalign 0.5 at ystretch(0.1)
    add 'gui/ui_modal_frame_borders.webp' xalign 0.5 yalign 0.5 at ystretch(0.2)
    text _("НАСТРОЙКИ") xpos 500 ypos 315 color gui.hover_color size 55 at delayed_fade(0.2, 0.2)
    hbox:
        at delayed_fade(0.2, 0.2)
        yalign 0.5
        xalign 0.5
        xoffset -50
        yoffset -5
        spacing 50
        vbox:
            xalign 1.0
            text _('Громкость музыки') style 'pref_label'
            text _('Громкость звука') style 'pref_label'
            text _('Скорость текста') style 'pref_label'
            text _('Скорость авто-чтения') style 'pref_label'
            text _('Сменить режим экрана') style 'pref_label'
        vbox:
            yoffset 25
            spacing 42
            bar value Preference("music volume") style 'pref_bars'
            bar value Preference("sound volume") style 'pref_bars'
            bar value Preference("text speed") style 'pref_bars'
            bar value Preference("auto-forward time") style 'pref_bars'
            if store._preferences.fullscreen:
                imagebutton idle 'gui/ui_checkbox_inactive.webp' hover 'gui/ui_checkbox_checked.webp' action [Preference("display", "toggle")]
            else:
                hbox:
                    spacing 10
                    imagebutton idle 'gui/ui_checkbox_checked.webp' hover 'gui/ui_checkbox_inactive.webp' action [Preference("display", "toggle")]
    hbox:
        at delayed_fade(0.2, 0.2)
        xalign 0.5
        ypos 710
        spacing 40
        textbutton _("назад") action Hide('preferences') style 'pref_buttons'
        if not main_menu:
            textbutton _("меню") action MainMenu(confirm=True) style 'pref_buttons'
            textbutton _("выход") action Quit(confirm=True) style 'pref_buttons'
    use common_hide('preferences')
transform -1 delayed_fade(d, fd):
    on show:
        alpha 0.0
        pause d
        linear fd alpha 1.0
    on hide:
        alpha 1.0
        pause d
        linear fd alpha 0.0
transform -1 pop(d, z=0.75):
    on show:
        alpha 0.0
        zoom z
        pause d
        parallel:
            easein 0.35 zoom 1.0
        parallel:
            easein 0.35 alpha 1.0
    on hide:
        alpha 1.0
        zoom 1.0
        pause d
        parallel:
            easeout 0.35 zoom z
        parallel:
            easeout 0.35 alpha 0.0
transform -1 ystretch(d):
    on show:
        alpha 0.0
        yzoom 1.5
        pause d
        parallel:
            ease 0.5 yzoom 1.0
        parallel:
            ease 0.5 alpha 1.0
    on hide:
        alpha 1.0
        yzoom 1.0
        pause d
        parallel:
            ease 0.5 yzoom 1.5
        parallel:
            ease 0.5 alpha 0.0
init -1 style pref_bars:
    right_bar 'gui/ui_bar_empty.webp'
    left_bar 'gui/ui_bar_full.webp'
    thumb None
    xsize 427
    ysize 17
    xpadding 0
    ypadding 0
    xmargin 0
    ymargin 0
    left_gutter 0
    right_gutter 0
init -1 style pref_buttons is say_button:
    properties gui.button_properties('say_button')
init -1 style pref_buttons_text is say_button_text:
    properties gui.button_text_properties('say_button_text')
    size 48
init -1 style pref_label:
    font gui.interface_font
    color gui.hover_color
    size 48
    text_align 1.0
    min_width 500
init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox
init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox
init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox
init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox
init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text
init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3
init -1 style pref_label_text:
    yalign 1.0
init -1 style pref_vbox:
    xsize 338
init -1 style radio_vbox:
    spacing gui.pref_button_spacing
init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.webp"
init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")
init -1 style check_vbox:
    spacing gui.pref_button_spacing
init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.webp"
init -1 style check_button_text:
    properties gui.button_text_properties("check_button")
init -1 style slider_slider:
    xsize 525
init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")
init -1 style slider_vbox:
    xsize 675
init -501 screen history() tag menu:
    predict False
    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"
        for h in _history_list:
            window:
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                text h.what
        if not _history_list:
            label _("История диалогов пуста.")
init -1 style history_window is empty
init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text
init -1 style history_text is gui_text
init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text
init -1 style history_window:
    xfill True
    ysize gui.history_height
init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
init -1 style history_label:
    xfill True
init -1 style history_label_text:
    xalign 0.5
init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text
init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 12
init -1 style help_button_text:
    properties gui.button_text_properties("help_button")
init -1 style help_label:
    xsize 375
    right_padding 30
init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
init -501 screen confirm(message, yes_action, no_action):
    modal True
    use modal
    add 'gui/ui_confirm_frame.webp' xalign 0.5 yalign 0.5 at pop(0.05)
    add 'gui/ui_confirm_borders.webp' xalign 0.5 yalign 0.5 at pop(0.1)
    frame:
        at delayed_fade(0.20, 0.20)
        background None
        xalign 0.5
        yalign 0.5
        xsize 1030
        ysize 420
        text _("ПОДТВЕРДИТЕ") xoffset 60 yoffset 20 color gui.hover_color size 55
        text message yalign 0.5 xalign 0.5
        hbox:
            xalign 0.5
            yoffset 325
            spacing 40
            textbutton _("да") action yes_action text_size 48 text_font gui.interface_font
            textbutton _("нет") action no_action text_size 48 text_font gui.interface_font
    key "game_menu" action no_action
init -501 screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        has hbox:
            spacing 9
        text _("Пропускаю  ") font gui.interface_font
        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
transform -1 delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
init -1 style skip_frame is empty
init -1 style skip_text is gui_text:
    color '#FFF'
init -1 style skip_triangle is skip_text
init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding
init -1 style skip_text:
    size gui.notify_text_size
init -1 style skip_triangle:
    font "DejaVuSans.ttf"
init -501 screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text message
    timer 3.25 action Hide('notify')
transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
init -1 style notify_frame is empty
init -1 style notify_text is gui_text
init -1 style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
init -1 style notify_text:
    size gui.notify_text_size
init -501 screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing
        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)
        else:
            use nvl_dialogue(dialogue)
        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"
    add SideImage() xalign 0.0 yalign 1.0
init -501 screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            has fixed:
                yfit gui.nvl_height is None
            if d.who is not None:
                text d.who:
                    id d.who_id
            text d.what:
                id d.what_id
define -1 config.nvl_list_length = 6
init -1 style nvl_window is default
init -1 style nvl_entry is default
init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue
init -1 style nvl_button is button
init -1 style nvl_button_text is button_text
init -1 style nvl_window:
    xfill True
    yfill True
    background "gui/nvl.webp"
    padding gui.nvl_borders.padding
init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height
init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign
init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign
init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
init -1 style pref_vbox:
    variant "medium"
    xsize 675
init -501 screen quick_menu():
    variant "touch"
    zorder 100
    hbox:
        style_prefix "quick"
        xalign 1.0
        yalign 1.0
        textbutton _("Авто") action Preference("auto-forward", "toggle")
        textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Опции") action Show('preferences')
        textbutton _("Сохранить") action Show('save')
init -1 style window:
    variant "small"
    background "gui/phone/textbox.webp"
init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"
init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.webp"
init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.webp"
init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 510
init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0
init -1 style pref_vbox:
    variant "small"
    xsize 600
init -1 style slider_pref_vbox:
    variant "small"
    xsize None
init -1 style slider_pref_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

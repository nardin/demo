transform gallery_half:
    zoom 0.5
transform gallery_dissolve:
    on show:
        alpha 0
        linear 0.25 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.25 alpha 0.0
image sky_night_half = im.FactorScale("images/bg/sky night.jpg", 0.5)
image cg_01:
    im.FactorScale("images/cg/scene 1/cg_s1_martha_intro.jpg", 0.25)
image cg_02:
    'cg_slavers'
image cg_03 = LiveComposite(
      (1920,540), (0,0), 'cut goblins bg'
    , (1200,90), 'cut_goblins_1'
    , (700,34), 'cut_goblins_2'
    , (350,64), 'cut_goblins_3'
    )
image cg_04:
    'cg_goblin_chase'
image cg_05:
    'ogre_full'
image cg_06:
    'cg_lap_pillow'
image cg_07:
    im.FactorScale('images/cg/scene 4/cg_libertad.jpg', 0.5)
image cg_08:
    'cg smile'
image cg_09:
    'cg hug'
image cg_10:
    'fin'
transform image_thumb:
    alpha 0.4
    on hover:
        linear .15 alpha 1.0
    on idle:
        linear .15 alpha 0.4
transform gallery_image_transform:
    on replace:
        parallel:
            alpha 0.5
            easein 0.5 alpha 1.0
    on replaced:
        parallel:
            alpha 1.0
            easeout 0.5 alpha 0.0
init python:
    bg_gal = [  'cg_s1_running', 'bg_slums_alley', 'bg_market', 'wild forest'
                , 'clearing', 'gob_forest_day', 'gob_forest_night'
                , 'sky_night_half', 'spring', 'another_forest', 'bg_libertad'
                ]
    cg_gal = [  'cg_01','cg_02','cg_03','cg_04','cg_05'
                ,'cg_06','cg_07','cg_08','cg_09','cg_10'
                ]
    misc_gal = ['ada_concept','martha_concept','final_roughs'
                ,'bgs1','bgs2','promo2','au2','slave','comfy'
                ]
screen gallery_image(x, type=None, title=None) tag gallery_image:
    modal True
    use modal
    add x at [pop(0,0.9), gallery_image_transform]:
        xalign 0.5
        yalign 0.5
    if title:
        text title xalign 0 yalign 1.0 color '#FFF' outlines [(2,'#181310',0,0)]
    if type == 'bg':
        $ index = bg_gal.index(x)
        $ gal = bg_gal
    elif type == 'cg':
        $ index = cg_gal.index(x)
        $ gal = cg_gal
    elif type == 'misc':
        $ index = misc_gal.index(x)
        $ gal = misc_gal
    if index < len(gal)-1:
        imagebutton idle 'gui/gallery_image_button_idle.webp' hover 'gui/gallery_image_button.webp' action Show('gallery_image', x=gal[index+1], type=type) xalign 1.0 yalign 0.5
        key 'K_RIGHT' action Show('gallery_image', x=gal[index+1], type=type)
        key 'mousedown_5' action Show('gallery_image', x=gal[index+1], type=type)
    if index > 0:
        imagebutton idle 'gui/gallery_image_button_idle.webp' hover 'gui/gallery_image_button_left.webp' action Show('gallery_image', x=gal[index-1], type=type) xalign 0.0 yalign 0.5
        key 'K_LEFT' action Show('gallery_image', x=gal[index-1], type=type)
        key 'mousedown_4' action Show('gallery_image', x=gal[index-1], type=type)
    for i in back_button:
        key i action Hide('gallery_image')
screen room_bg() tag extras_room:
    frame:
        at rooms
        background None
        xoffset 430
        yalign 0.5
        has vbox:
            spacing 10
        text _('ФОНЫ')
        add 'gui/ui_extras_horizontal_bar.webp' xoffset -30
        grid 5 3:
            yoffset 20
            spacing 20
            style_prefix "extras_grid"
            imagebutton action Show('gallery_image', x='cg_s1_running', type='bg') idle 'thumb_cg_s1_running' at image_thumb
            imagebutton action Show('gallery_image', x='bg_slums_alley', type='bg') idle 'thumb_bg_slums_alley' at image_thumb
            imagebutton action Show('gallery_image', x='bg_market', type='bg') idle 'thumb_bg_market' at image_thumb
            imagebutton action Show('gallery_image', x='wild forest', type='bg') idle 'thumb_wild forest' at image_thumb
            imagebutton action Show('gallery_image', x='clearing', type='bg') idle 'thumb_clearing' at image_thumb
            imagebutton action Show('gallery_image', x='gob_forest_day', type='bg') idle 'thumb_gob_forest_day' at image_thumb
            imagebutton action Show('gallery_image', x='gob_forest_night', type='bg') idle 'thumb_gob_forest_night' at image_thumb
            imagebutton action Show('gallery_image', x='sky_night_half', type='bg') idle 'thumb_sky night' at image_thumb
            imagebutton action Show('gallery_image', x='spring', type='bg') idle 'thumb_spring' at image_thumb
            imagebutton action Show('gallery_image', x='another_forest', type='bg') idle 'thumb_another_forest' at image_thumb
            imagebutton action Show('gallery_image', x='bg_libertad', type='bg') idle 'thumb_bg_libertad' at image_thumb
            null height 1
            null height 1
            null height 1
            null height 1
screen room_cg() tag extras_room:
    frame:
        background None
        xoffset 430
        yalign 0.5
        at rooms
        has vbox:
            spacing 10
        text _('АРТ')
        add 'gui/ui_extras_horizontal_bar.webp' xoffset -30
        grid 5 2:
            yoffset 20
            spacing 20
            style_prefix "extras_grid"
            imagebutton action Show('gallery_image', x='cg_01', type='cg') idle 'thumb_cg_s1_martha_intro' at image_thumb
            imagebutton action Show('gallery_image', x='cg_02', type='cg') idle 'thumb_cg_slavers' at image_thumb
            imagebutton action Show('gallery_image', x='cg_03', type='cg') idle 'thumb_cut goblins bg' at image_thumb
            imagebutton action Show('gallery_image', x='cg_04', type='cg') idle 'thumb_cg_goblin_chase' at image_thumb
            imagebutton action Show('gallery_image', x='cg_05', type='cg') idle 'thumb_ogre_full' at image_thumb
            imagebutton action Show('gallery_image', x='cg_06', type='cg') idle 'thumb_cg_lap_pillow' at image_thumb
            imagebutton action Show('gallery_image', x='cg_07', type='cg') idle 'thumb_cg_libertad' at image_thumb
            imagebutton action Show('gallery_image', x='cg_08', type='cg') idle 'thumb_cg smile' at image_thumb
            imagebutton action Show('gallery_image', x='cg_09', type='cg') idle 'thumb_cg hug' at image_thumb
            imagebutton action Show('gallery_image', x='cg_10', type='cg') idle 'thumb_fin' at image_thumb
screen room_bonus() tag extras_room:
    frame:
        background None
        xoffset 430
        yalign 0.5
        at rooms
        has vbox:
            spacing 10
        text _('РАЗНОЕ')
        add 'gui/ui_extras_horizontal_bar.webp' xoffset -30
        grid 5 2:
            yoffset 20
            spacing 20
            style_prefix "extras_grid"
            imagebutton action Show('gallery_image', x='ada_concept' ,type='misc' ) idle 'thumb_ada_concept' at image_thumb
            imagebutton action Show('gallery_image', x='martha_concept' ,type='misc' ) idle 'thumb_martha_concept' at image_thumb
            imagebutton action Show('gallery_image', x='final_roughs' ,type='misc' ) idle 'thumb_final_roughs' at image_thumb
            imagebutton action Show('gallery_image', x='bgs1' ,type='misc' , title='Фоновые Скетчи А') idle 'thumb_bgs1' at image_thumb
            imagebutton action Show('gallery_image', x='bgs2' ,type='misc' , title='Фоновые Скетчи Б') idle 'thumb_bgs2' at image_thumb
            imagebutton action Show('gallery_image', x='promo2' ,type='misc' , title='Промо Арт') idle 'thumb_promo' at image_thumb
            imagebutton action Show('gallery_image', x='au2' ,type='misc' ,title='Альтернативная Вселенная, Ада и Марта') idle 'thumb_au' at image_thumb
            imagebutton action Show('gallery_image', x='slave' ,type='misc', title='Заключённая') idle 'thumb_slave' at image_thumb
            imagebutton action Show('gallery_image', x='comfy' ,type='misc', title='Лечение') idle 'thumb_comfy' at image_thumb
            null height 1
image au2:
    im.FactorScale('images/extras/au.jpg', 0.6)
image promo2:
    im.FactorScale('images/extras/promo.jpg', 0.6)
screen room_music() tag extras_room:
    frame:
        background None
        xoffset 430
        yalign 0.5
        at rooms
        has vbox:
            spacing 10
        text _('МУЗЫКАЛЬНАЯ')
        add 'gui/ui_extras_horizontal_bar.webp' xoffset -30
        vbox:
            yoffset 20
            spacing 5
            style_prefix "extras_grid"
            textbutton "1. Тема Главного Меню (JTikey - Lightdrop)" action Play('music', audio.main_menu_music)
            textbutton "2. Тема Работорговцев (Gregoire Lourme - City of Crime)" action Play('music', audio.streets_of_hell)
            textbutton "3. Тема Марты (Epic Soul Factory - Honor)" action Play('music', audio.escape)
            textbutton "4. Гоблины! (Gregoire Lourme - Surrendering the Castle)" action Play('music', audio.first_encounter)
            textbutton "5. Бежим!!! (Epic Soul Factory - Night Hunter)" action Play('music', audio.goblin_chase)
            textbutton "6. Выход Огра (Epic Soul Factory - Amazona)" action Play('music', audio.enter_the_ogre)
            textbutton "7. Финальная Битва (Gregoire Lourme - Swords of Fire)" action Play('music', audio.die_with_honor)
            textbutton "8. Тема Ады (Epic Soul Factory - Moonlit Night)" action Play('music', audio.after_the_battle)
            textbutton "9. В Пределах (Gregoire Lourme - My Home, My Family)" action Play('music', audio.within_reach)
            textbutton "10. Город Улыбок (Avel Glas - My Lodging's on the Cold Ground Kesh Jig)" action Play('music', audio.city_of_smiles)
            textbutton "11. Неразделённые (Epic Soul Factory - Love)" action Play('music', audio.falling_in_love)
            textbutton "12. Титры (Antarcticbreeze - Life my Life)" action Play('music', audio.healing_begins)
screen room_credits() tag extras_room:
    frame:
        background None
        xoffset 430
        yalign 0.5
        at rooms
        has vbox:
            spacing 10
        text _('РАЗРАБОТЧИКИ')
        add 'gui/ui_extras_horizontal_bar.webp' xoffset -30
        vbox:
            yoffset 20
            spacing 20
            style_prefix "credits_text"
            text _('История, Арт & Программирование - Sendo {a=https://twitter.com/sendrawz}(@sendrawz){/a}')
            text _('Писатель - Zetsubou {a=https://twitter.com/zetsubougames}(@zetsubougames){/a}')
            text _('Производство - Studio Camelot {a=https://twitter.com/studiocamelotvn}(@studiocamelotvn){/a}')
            text _('Музыка - Грегуар Лоурме, Epic Soul Factory, Antarcticbreeze, Avel Glas, JTikey')
            text _('Звуки - Sound Effect Lab {a=http://en.soundeffect-lab.info/}(en.soundeffect-lab.info){/a}')
            text _('Русификация — Gardares {a=https://vk.com/reneen}(@reneen){/a}')
            text _('Движок - Ren\'py {a=https://www.renpy.org/}(renpy.org){/a}')
            text _('Сделано для {a=https://itch.io/jam/yuri-game-jam-2016}YuriJam 2016{/a}')
style extras_grid_image_button:
    xsize 200
    ysize 113
style extras_grid_button_text:
    size 34
style extras_grid_text:
    size 36
style credits_text_text:
    size 34
init python:
    style.hyperlink             = Style(style.nvl_dialogue)
    style.hyperlink.font        = gui.default_font
    style.hyperlink.size        = 30
    style.hyperlink.color       = '#827d67'
    style.hyperlink.hover_color = "#bcb07d"
    style.hyperlink.underline   = False
    def hyperlink_styler(link):
        return style.hyperlink
    def hyperlink_clicked(link):
        try:
            import webbrowser
            webbrowser.open_new(link)
        except:
            pass
    def hyperlink_hovered(link):
        return None
    style.default.hyperlink_functions = (hyperlink_styler, hyperlink_clicked, hyperlink_hovered)
transform rooms:
    on show:
        parallel:
            alpha 0
            linear 0.5 alpha 1
        parallel:
            xoffset -25
            ease 0.5 xoffset 0
    on hide:
        parallel:
            alpha 1.0
            ease_quad 0.4 alpha 0.0
        parallel:
            xoffset 0
            ease_quad 0.4 xoffset 25
    on replace:
        parallel:
            alpha 0
            pause 0.35
            linear 0.5 alpha 1
        parallel:
            xoffset -25
            pause 0.35
            easein 0.5 xoffset 0
    on replaced:
        parallel:
            alpha 1
            linear 0.5 alpha 0
        parallel:
            xoffset 0
            easeout 0.5 xoffset 25
transform extra_vertical:
    on show:
        yzoom 0
        ease_quad 0.35 yzoom 1.0
    on hide:
        yzoom 1.0
        ease_quad 0.25 yzoom 0.0
transform extra_buttons(d=0):
    parallel:
        alpha 0.0
        pause d
        easein 0.5 alpha 1.0
    parallel:
        xoffset -50
        pause d
        easein 0.5 xoffset 0
    on hide:
        parallel:
            alpha 1.0
            pause d
            easeout 0.3 alpha 0.0
        parallel:
            xoffset 0
            pause d
            easeout 0.4 xoffset -50
transform music_player:
    alpha 0.35
    on hover:
        alpha 1.0
screen extras():
    modal True
    add '#020202' at modal_bg_transform
    add 'extras_bg' at delayed_fade(0.1, 0.5)
    add 'gui/ui_extras_vertical_bar.webp' alpha 0.5 yalign 0.5 xoffset 350 at [delayed_fade(0.1,0.1),extra_vertical]
    text _('Экстра') xoffset 100 yoffset 382 size 44 at extra_buttons
    textbutton _('Галерея Арта') action Show('room_cg') xoffset 100 yoffset 440 text_font gui.interface_font at extra_buttons(0.025)
    textbutton _('Галерея Фонов') action Show('room_bg') xoffset 100 yoffset 490 text_font gui.interface_font at extra_buttons(0.050)
    textbutton _('Галерея Разного') action Show('room_bonus') xoffset 100 yoffset 540 text_font gui.interface_font at extra_buttons(0.075)
    textbutton _('Музыкальная') action Show('room_music') xoffset 100 yoffset 590 text_font gui.interface_font at extra_buttons(0.1)
    textbutton _('Разработчики') action Show('room_credits') xoffset 100 yoffset 640 text_font gui.interface_font at extra_buttons(0.125)
    textbutton _('Назад') action [Hide('extras'), Hide('extras_room')] xoffset 100 yoffset 720 text_font gui.interface_font at extra_buttons(0.150)
    for i in back_button:
        key i action [Hide('extras'), Hide('extras_room')]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

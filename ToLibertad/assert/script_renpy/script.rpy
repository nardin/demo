screen remap:
    for i in back_button:
        key i action Show('preferences')
    key 'K_F1' action Show('my_help')
    if config.developer:
        key 'K_F5' action Jump(current_scene)
        key '`' action ShowMenu('preferences2')
label start:
    show screen remap
    if config.developer:
        menu:
            "Сцена 1":
                $ current_scene = 'scene_1'
                call scene_1 from _call_scene_1
                call scene_2 from _call_scene_2
                call scene_3 from _call_scene_3
                call scene_4 from _call_scene_4
                call scene_5 from _call_scene_5
                call credits from _call_credits
            "Сцена 2":
                $ current_scene = 'scene_2'
                call scene_2 from _call_scene_2_1
                call scene_3 from _call_scene_3_1
                call scene_4 from _call_scene_4_1
                call scene_5 from _call_scene_5_1
                call credits from _call_credits_1
            "Сцена 3":
                $ current_scene = 'scene_3'
                call scene_3 from _call_scene_3_2
                call scene_4 from _call_scene_4_2
                call scene_5 from _call_scene_5_2
                call credits from _call_credits_2
            "Сцена 4":
                $ current_scene = 'scene_4'
                call scene_4 from _call_scene_4_3
                call scene_5 from _call_scene_5_3
                call credits from _call_credits_3
            "Сцена 5":
                $ current_scene = 'scene_5'
                call scene_5 from _call_scene_5_4
                call credits from _call_credits_4
            "Титры":
                $ current_scene = 'credits'
                call credits from _call_credits_6
    else:
        $ current_scene = 'scene_1'
        call scene_1 from _call_scene_1_1
        $ current_scene = 'scene_2'
        call scene_2 from _call_scene_2_2
        $ current_scene = 'scene_3'
        call scene_3 from _call_scene_3_3
        $ current_scene = 'scene_4'
        call scene_4 from _call_scene_4_4
        $ current_scene = 'scene_5'
        call scene_5 from _call_scene_5_5
        $ current_scene = 'credits'
        call credits from _call_credits_5
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

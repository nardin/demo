image martha base = 'martha_base_[martha_shield]'
image martha neutral = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_1', (0,0), 'martha_mouth_1')
image martha neutral2 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_1', (0,0), 'martha_mouth_2')
image martha annoyed1 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_3', (0,0), 'martha_mouth_1')
image martha annoyed2 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_3', (0,0), 'martha_mouth_2')
image martha annoyed3 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_3', (0,0), 'martha_mouth_5')
image martha annoyed4 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_3', (0,0), 'martha_mouth_1')
image martha eyesclosed1 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_4', (0,0), 'martha_mouth_1')
image martha eyesclosed2 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_5', (0,0), 'martha_mouth_1')
image martha eyesclosed3 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_5', (0,0), 'martha_mouth_2')
image martha eyesclosed4 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_7', (0,0), 'martha_mouth_1')
image martha eyesclosed5 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_5', (0,0), 'martha_mouth_4')
image martha worried = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_6', (0,0), 'martha_mouth_1')
image martha indifferent = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_2', (0,0), 'martha_mouth_1')
image martha smile = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_1', (0,0), 'martha_mouth_4')
image martha smile2 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_6', (0,0), 'martha_mouth_4')
image martha smile3 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_7', (0,0), 'martha_mouth_4')
image martha oh = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_1', (0,0), 'martha_mouth_6')
image martha oh2 = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_10', (0,0), 'martha_mouth_1')
image martha shocked = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_8', (0,0), 'martha_mouth_7')
image martha sad = LiveComposite((702,1045), (0,0), 'martha base', (0,0), 'martha_eye_9', (0,0), 'martha_mouth_8')
image side martha neutral = LiveCrop((145, 0, 702, 400), 'martha neutral')
image side martha neutral2 = LiveCrop((145, 0, 702, 400), 'martha neutral2')
image side martha annoyed1 = LiveCrop((145, 0, 702, 400), 'martha annoyed1')
image side martha annoyed2 = LiveCrop((145, 0, 702, 400), 'martha annoyed2')
image side martha annoyed3 = LiveCrop((145, 0, 702, 400), 'martha annoyed3')
image side martha annoyed4 = LiveCrop((145, 0, 702, 400), 'martha annoyed4')
image side martha eyesclosed1 = LiveCrop((145, 0, 702, 400), 'martha eyesclosed1')
image side martha eyesclosed2 = LiveCrop((145, 0, 702, 400), 'martha eyesclosed2')
image side martha eyesclosed3 = LiveCrop((145, 0, 702, 400), 'martha eyesclosed3')
image side martha eyesclosed4 = LiveCrop((145, 0, 702, 400), 'martha eyesclosed4')
image side martha eyesclosed5 = LiveCrop((145, 0, 702, 400), 'martha eyesclosed5')
image side martha worried = LiveCrop((145, 0, 702, 400), 'martha worried')
image side martha indifferent = LiveCrop((145, 0, 702, 400), 'martha indifferent')
image side martha smile = LiveCrop((145, 0, 702, 400), 'martha smile')
image side martha smile2 = LiveCrop((145, 0, 702, 400), 'martha smile2')
image side martha smile3 = LiveCrop((145, 0, 702, 400), 'martha smile3')
image side martha oh = LiveCrop((145, 0, 702, 400), 'martha oh')
image side martha oh2 = LiveCrop((145, 0, 702, 400), 'martha oh2')
image side martha shocked = LiveCrop((145, 0, 702, 400), 'martha shocked')
image side martha sad = LiveCrop((145, 0, 702, 400), 'martha sad')
image side martha fight1 = LiveComposite((418, 441), (0,0), 'martha_fight', (0,0), 'martha_fight eye 1', (0,0), 'martha_fight mouth 1')
image side martha fight2 = LiveComposite((418, 441), (0,0), 'martha_fight', (0,0), 'martha_fight eye 1', (0,0), 'martha_fight mouth 2')
image side martha fight3 = LiveComposite((418, 441), (0,0), 'martha_fight', (0,0), 'martha_fight eye 1', (0,0), 'martha_fight mouth 3')
image side martha fight4 = LiveComposite((418, 441), (0,0), 'martha_fight', (0,0), 'martha_fight eye 1', (0,0), 'martha_fight mouth 4')
image side martha surprised = LiveComposite((418, 441), (0,0), 'martha_fight', (0,0), 'martha_fight eye 2', (0,0), 'martha_fight mouth 5')
init python:
    def ada_sprite(st, at):
        return LiveComposite(
            (362, 380),
            (0,0), 'ada_base_clean',
            (0,0), ConditionSwitch(
                'ada_clean == False', 'ada_base_dirt',
                'ada_clean == True', Null(),
                ),
            (0,0), ConditionSwitch(
                'ada_collar == True', 'ada_base_collar',
                'ada_collar == False', Null(),
                ),
            (0,0), ConditionSwitch(
                'ada_cloak == True', 'ada_base_cloak',
                'ada_cloak == False', Null(),
                ),
            ), .1
image ada base = DynamicDisplayable(ada_sprite)
image side ada neutral = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_10', (0,0), 'ada_mouth_1')
image side ada neutral2 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_10', (0,0), 'ada_mouth_6')
image side ada neutral3 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_13', (0,0), 'ada_mouth_1')
image side ada tired = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_2', (0,0), 'ada_mouth_2')
image side ada tired2 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_2', (0,0), 'ada_mouth_1')
image side ada surprised = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_12', (0,0), 'ada_mouth_9')
image side ada surprised2 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_10', (0,0), 'ada_mouth_8')
image side ada scared = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_4', (0,0), 'ada_mouth_2')
image side ada scared2 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_4', (0,0), 'ada_mouth_1')
image side ada scared3 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_4', (0,0), 'ada_mouth_5')
image side ada angry = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_6', (0,0), 'ada_mouth_4')
image side ada angry2 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_6', (0,0), 'ada_mouth_1')
image side ada angry3 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_6', (0,0), 'ada_mouth_6')
image side ada sad = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_8', (0,0), 'ada_mouth_1')
image side ada sad2 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_8', (0,0), 'ada_mouth_2')
image side ada sad3 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_8', (0,0), 'ada_mouth_6')
image side ada sad4 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_11', (0,0), 'ada_mouth_1')
image side ada sad5 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_11', (0,0), 'ada_mouth_5')
image side ada sad6 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_11', (0,0), 'ada_mouth_9')
image side ada idea = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_1', (0,0), 'ada_mouth_3')
image side ada smile = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_10', (0,0), 'ada_mouth_7')
image side ada smile2 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_10', (0,0), 'ada_mouth_5')
image side ada smile3 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_17', (0,0), 'ada_mouth_5')
image side ada pleading = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_8', (0,0), 'ada_mouth_10')
image side ada lookaway = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_16', (0,0), 'ada_mouth_5')
image side ada lookaway2 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_11', (0,0), 'ada_mouth_5')
image side ada eyesclosed1 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_3', (0,0), 'ada_mouth_1')
image side ada eyesclosed2 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_3', (0,0), 'ada_mouth_2')
image side ada eyesclosed3 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_9', (0,0), 'ada_mouth_1')
image side ada eyesclosed4 = LiveComposite((362, 380), (0,0), 'ada base', (0,0), 'ada_eye_9', (0,0), 'ada_mouth_5')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

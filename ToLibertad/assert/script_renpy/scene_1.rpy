label scene_1:
    show splash_title
    scene black with dissolve
    stop music fadeout 1.0
    pause 1.0
    play music audio.streets_of_hell
    pause 1.0
    show cg_s1_running:
        parallel:
            alpha 0.0
            linear 3.0 alpha 1.0
    pause 2.5
    slave eyesclosed2 "{i}хаа… хаа… хаа…{/i}"
    slave tired2 "Ещё… Ещё немного… {i}хаа…{/i}"
    "Дыша так тяжко, что я думала, что потерплю крах в любой момент, я продолжала заставлять себя бежать."
    "Мои ноги почти отказали, а моё сердцебиение было очень громким. Мне срочно было нужно отдохнуть, но я знала, что не могу позволить себе такой роскоши."
    "Сейчас я зашла слишком далеко, чтобы сдаться. Если меня поймают, я буду убита, если не хуже."
    scene white with Dissolve(2)
    pause 1
    scene bg_slums_alley with dissolve
    s1 "Быстрее, за ней! Не дайте ей сбежать!"
    s3 "Да, да, знаю я. Схватить маленькую крыску, прежде чем она сбежит."
    s2 "Ох, я удостоверюсь, что эта маленькая шваль получит по заслугам!"
    s2 "Никто не сбежит из моей хватки так легко. А когда я её поймаю… Хехехе…"
    s1 "Заткнись и сосредоточься, идиот! Она направилась туда!"
    "Я продолжала бежать так быстро, как позволяли нести меня ноги."
    "Голодная и лишённая сна, через моё тело текло достаточно адреналина, чтобы убежать из этого ужасного города."
    "И сейчас ничего другого не требуется. Если я смогу выбраться из города и дойти до Либертада, я наконец-то буду свободна."
    s2 "Попалась!"
    slave surprised "Ва?!"
    "Один из моих преследователей внезапно выбежал передо мной."
    "Я повернулась, чтобы ускользнуть в противоположном направлении, но в момент, когда я это сделала, ещё двое мужчин встало у меня на пути."
    scene bg_slums_alley_blurred with dissolve
    show cg_slavers:
        alpha 0
        yalign 0.5
        yoffset 50
        parallel:
            ease 2.0 alpha 1.0
        parallel:
            ease 2.0 yoffset 0
    s3 "Хех. Как мышку в мышеловке, а?"
    s3 "Ты хорошо постаралась, маленькая девочка, убежав так далеко. Смотря на тебя, никто бы не заподозрил, что ты перережешь охраннику глотку и обберёшь его труп."
    s3 "Была бы моя похвала, если бы ты не выбрала убить моего друга. Какая жалость."
    "Один из моих преследователей начал идти ко мне."
    slave pleading "Н..Нет… Пожалуйста! Не надо!"
    s3 "Ох, тихо. Такой жалобный вид не подходит к такой красотке, как ты."
    s3 "Если ты успокоишься, возможно, я вознагражу тебя в последний раз, ммм? Хочешь ли ты насладиться жизнью в последний раз?"
    slave angry "Хватит! Уберите от меня свои грязные руки!"
    s2 "Фьюх. Она драчливая, я же говорил тебе."
    s1 "Заткнитесь и держите её. Я буду первым!"
    s3 "Гх. Отличный способ испортить настроение, болтающие придурки!"
    s3 "Ба, забудь. В любом случае, никакой романтики в таком переулке."
    s3 "А теперь… Что скажешь, девочка? Хочешь сделать это легко и снимешь свою одежду без лишней борьбы?"
    "Я держала себя за поясницу, пока отступала назад к стене."
    slave angry3 "Я… "
    extend angry "Я лучше умру!"
    s3 "Пф. Это можно устроить."
    s3 "Но сначала… Вы, двое, встаньте позади. Я покажу этой девочке, как нарушать права её хозяина."
    "Самый разговорчивый из мужчин приблизился ко мне и схватил моё запястье."
    "Я пыталась вырваться, но он был слишком силён. И даже если бы мне это удалось, я была безоружна и окружена."
    "Моя попытка освободиться кончилась."
    slave sad "(Почему… Почему всё должно быть так?)"
    slave "(Почему я продолжаю страдать, пока злым людям позволительно делать что угодно?)"
    slave "(Если этот мир правда настолько сгнил, может мне лучше из него уйти…)"
    stop music fadeout 3.0
    scene black with Dissolve(2)
    "Я закрыла глаза, ожидая неизбежного."
    "Если я в любом случае умру, нет причин бороться. Ещё один момент страданий и оскорблений ничего не изменит."
    "К лучшему или к худшему, я укрепила свою решимость и подготовился ко всему, что может придти затем."
    pause 2
    play music audio.escape fadein 1.0
    slave scared "(Хах..?)"
    show cg_s1_martha_intro:
        xalign 0.5
        parallel:
            alpha 0
            linear 3.0 alpha 1.0
        parallel:
            zoom 0.5
            yalign 1.0
            ease 8.0 yalign 0.2
    show martha_closeup:
        alpha 0.0
        yoffset -540
        pause 5.5
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            easein 6.0 yoffset 0
    window hide
    pause 5.5
    "Я медленно открыла свои глаза, когда хватка на моей руке ослабла."
    "Сопровождаемый звуком чего-то упавшего на землю, вид, который меня ожидал, оказался одной из самых неожиданных, но всё же желанных сечь."
    "Передо мной на земле лежали трупы моих преследователей, каждый в луже собственной крови, упавшие без звука."
    slave surprised "Что… Как это..?"
    "Ошарашенная, мои глаза кидались в стороны, пока я пыталась осознать смысл того, что предстало предо мной."
    "Трое мужчин были мгновенно убиты, а рядом с их трупами стоит… женщина."
    "Вооружённая мечом и щитом, сильная женщина, без сомнения воин, свирепо смотревшая на трёх мужчин."
    "Я не видела ни признака сочувствия, ни раскаяния в её глазах. Для неё трое мужчин, которых она убила, были дикими животными, о которых никто не будет скучать."
    "И в этот момент я точно знала, что мне нужно сделать."
    scene bg_slums_alley with dissolve
    show martha neutral with dissolve
    slave angry "Пожалуйста! Пожалуйста, возьмите меня в Либертад!"
    "Женщина подняла взгляд с трупов в её ногах и взглянула на меня."
    warrior eyesclosed1 "Хм. Даже не поблагодаришь?"
    slave scared "А..Аа… Мои извинения. Я приношу вам глубочайшую благодарность за спасение моей жизни."
    slave "Пожалуйста, мне может быть грубо такое говорить, но везде работорговцы, и я…"
    warrior annoyed2 "Остановись на этом месте."
    "Женщина протянула ладонь, жестом говоря мне остановиться."
    warrior annoyed1 "Не пойми неправильно. Я убила этих трёх не потому, что ты нуждалась в помощи, но просто по своей прихоти."
    warrior eyesclosed1 "Я не образчик справедливости. Я не помогаю тем, кто в нужде, без причины."
    slave scared "Т..Тогда..!"
    "Я достала золотые монеты, которые я украла у стражника, которого убила во время первоначального побега."
    slave angry "Вот, возьмите всё! Это всё ваше!"
    slave angry2 "Взамен, пожалуйста, возьмите меня в Либертад!"
    "Женщина взяла золотые монеты от меня и мельком осмотрела их."
    warrior neutral "Довольно значительная сумма. Намного больше чем такая, как ты, должна иметь."
    warrior eyesclosed2 "…И всё же, я должна прекратить с этого моё вмешательство."
    slave scared "Н..Но почему?"
    warrior neutral "Как я и сказала, моё участие было только по моей прихоти."
    warrior "Этот разговор окончен. Если ты хочешь дойти до Либертада, тебе лучше уйти."
    "Возвращая мне золотые монеты, женщина повернулась и начала уходить."
    slave scared "Ты не серьёзно…"
    slave angry2 "Если всё так пойдёт, тогда зачем вообще ты меня спасла?!"
    warrior annoyed2 "…Прости?"
    slave angry "Я бы была уже мертва, если бы ты меня не спасла!"
    slave sad2 "Моё страдание наконец бы закончилось! Я могла бы стать свободной от этой жалкой жизни!"
    slave eyesclosed1 "Но теперь, благодаря тебе, я всё ещё здесь, живя в страхе того, что я ничего не могу сделать."
    slave angry "Если ты мне не поможешь, меньшее что ты можешь сделать — меня добить!"
    warrior annoyed3 "Какой фарс."
    warrior "Я только что спасла твою жизнь. Будь благодарна!"
    slave "Благодарна за что? Всё что ты сделала — отсрочила неизбежное!"
    slave sad2 "Придут ещё работорговцы. "
    extend sad3 "Меня тут же поймают, "
    extend sad "и я вернусь туда, где я была…"
    "Я чувствую слёзы, образовывающиеся на уголках глаз."
    "Смотря на трупы подо мной, я чувствую и сожаление и зависть."
    slave eyesclosed3 "…Как глупо. Я должна была понимать, что я не выберусь живой."
    slave sad "Я думала, если я продолжу бежать, одна, тогда, может, я в одиночку смогу сбежать."
    slave "Но это просто невозможно. Даже если я сбегу из этого города, меня снова схватят в мгновение ока."
    "Я снова посмотрела на женщину передо мной."
    slave angry "Так что прими ответственность и убей меня сейчас же!"
    slave angry2 "И даже не думай сбегать. Заверши то, что начала, трусиха!"
    warrior eyesclosed1 "{w=0.2}{nw}"
    warrior annoyed2 "Т..Трусиха? {w=0.7}{nw}"
    extend annoyed3 "Я..?"
    warrior "Чтобы сказать, что это я убегала… {w=0.9}{nw}Ты действительно хочешь, чтобы я тебя убила.{w}"
    warrior annoyed4 "Но зачем? Какой логикой ты достигаешь таких абсурдных выводов?"
    warrior "Я спасла тебя, поэтому я должна тебя убить?"
    warrior annoyed2 "Я вмешалась, поэтому моя ответственность?"
    warrior annoyed4 "Я нисколько тебя не понимаю."
    "Несмотря на свои слова, женщина достала меч."
    warrior eyesclosed1 "Быть может, что смерть это то, что ты действительно хочешь, тогда…"
    warrior annoyed1 "…Хмм?"
    "Остановившись на середине предложения, воин внезапно отвела свой взгляд."
    "Она, казалось, сосредоточилась на чём-то невидимом, а затем быстро схватила мою руку и утащила меня в сторону."
    slave neutral2 "Э..Эй, что ты…"
    warrior annoyed3 "Шшш!"
    "Со ртом, закрытым рукой моей спасительницы, после того как она вложила свой меч в ножны, я тихо наблюдала, как пара фигур проходит мимо."
    "Только на мгновение остановившись, чтобы осмотреть своих павших товарищей, знакомые лица моих похитителей прошли мимо."
    warrior annoyed1 "{i}*кивнула*{/i}"
    "Моя сообщница кивнула в сторону, затем повела меня за руку, не сказав ни слова."
    scene black with dissolve
    pause 1
    "Когда мы ушли от трущоб и достигли оживлённого рынка, моя рука освободилась."
    stop music fadeout 3.0
    scene bg_market with Dissolve(2)
    pause 0.5
    show martha neutral with dissolve
    warrior "Ты не шутила. Те работорговцы намного ревностней, чем я думала."
    warrior "…{w=0.8}{nw}Девочка, какое у тебя имя?{w}"
    slave neutral2 "Моё имя?"
    a neutral "Я Ада."
    warrior eyesclosed2 "Ада, а?"
    m neutral "Хорошо, Ада. Моё имя Марта и впредь я буду сопровождать тебя в Либертад."
    a neutral2 "Т..Ты будешь?!"
    a neutral "Но почему? Я думала, ты против этой затеи."
    "Столкнувшись со своим прошлым утверждением, Марта отвела взгляд."
    m eyesclosed2 "Это просто прихоть."
    a eyesclosed4 "Х..Хорошо. Я не буду заставлять тебя отвечать."
    a smile2 "Ну тогда… Полагаю, я под твоей защитой, Марта."
    "Я взглянула на свою новую компаньоншу с улыбкой на лице."
    "Увидя её, Марта быстро зашагала прочь."
    m neutral "Сохрани это до момента, когда мы прибудем в Либертад."
    scene black with Dissolve(2)
    pause 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

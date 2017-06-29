transform light_anim:
    yalign 0.0
    alpha 0.0
    xoffset 0
    xalign renpy.random.random()
    pause renpy.random.randint(0, 2)
    block:
        parallel:
            easeout renpy.random.randint(1,3) alpha 0.7
            easeout renpy.random.randint(1,3) alpha 0.0
        parallel:
            linear 5 xoffset renpy.random.choice([-100,100])
    repeat
label scene_3:
    scene black
    stop music
    play music audio.ambient_forest fadein 1.0
    play ambient audio.ambient_creek fadein 1.0
    scene spring with Dissolve(2)
    $ renpy.random.seed()
    show spring_light_1 at light_anim
    $ renpy.random.seed()
    show spring_light_2 at light_anim
    $ renpy.random.seed()
    show spring_light_3 at light_anim
    $ renpy.random.seed()
    show spring_light_1 as l1 at light_anim
    $ renpy.random.seed()
    show spring_light_2 as l2 at light_anim
    $ renpy.random.seed()
    show spring_light_3 as l3 at light_anim
    "Когда мы с Мартой осознали, что гоблины ушли, мы уже зашли намного дальше, чем планировали."
    "Мы обе упали, истощённые и лишённые сна, наблюдая за занимающимся восходом солнца, наконец положившим конец нашей беспокойной ночи."
    "Сначала мы оставались бдительны. В конце концов, гоблины могли показаться в любой момент, а мы не хотели слишком рано ослаблять бдительность."
    "Но пока солнце продолжало вставать, а преимущество гоблинов, их отличное ночное зрение, исчезло, мы наконец позволили себе время отдохнуть."
    show martha eyesclosed5 with dissolve
    m smile "Фью… Намного лучше."
    m "Нет ничего лучше ванной после потной работы."
    a lookaway "Д..Да, может быть, ты права… Хотя я бы предпочла для себя спокойную ночь."
    m neutral "Мы сможем отдохнуть, когда достигнем Либертада. Пока мы в этом лесу, хороший сон ночью — роскошь, которую мы не можем позволить."
    a eyesclosed1 "Да… Думаю, так."
    "Я уступчиво вздохнула, отказавшись от идеи хорошего отдыха."
    "Вынужденная бежать с того момента, как я решилась на побег от моих похитителей, я была истощена больше, чем делала вид."
    "Убийство человека, преследование работорговцами, преследуемая гоблинами, отказ от отдыха… Вчера был трудный день для меня, и ванна совсем мне не поможет."
    m smile2 "Ох, взбодрись. Какая девушка не насладится хорошей большой ванной?"
    m "Даже если только глубокая весна, многим отказано даже в таком удовольствии. Наслаждайся, Ада."
    a lookaway "…Понятно."
    "Я продолжала смывать грязь с тела, пока Марта говорила."
    "Пока Марта без колебаний погрузила своё тело в воду, я тщательно очищала что-то одно за раз, пытаясь оставаться одетой."
    "В результате, моя мойка заняла намного больше времени, чем у Марты. Хотя судя по выражению на её лице, моё время было потрачено не зря."
    $ ada_clean = True
    m oh "Ого… Ты удивительно хорошо помылась, Ада."
    m smile "Оказывается, на самом деле ты довольно красивая. У тебя не должно быть проблем с нахождением мужа, когда мы дойдём до Либертада."
    a "Нет, я… У меня нет таких намерений…"
    a "Прямо сейчас, находить мужа — последнее, что у меня на уме."
    m smile2 "Ох? Ты более амбициозна, верно?"
    m smile "Для тебя же лучше. Не буду осуждать счастливых замужних домохозяек, но я знаю радость свободы лучше кого бы то ни было."
    "Я потрясла головой в ответ на предположение Марты."
    a lookaway2 "Это тоже не это."
    m oh "Тогда что? Тебя не интересуют… мужчины..?"
    a sad6 "……"
    "Слова Марта слетели у неё с уст, когда она увидела моё исказившееся лицо."
    "Из того, как широко открывались её рот и глаза, я знала, что она уже поняла ошибку в своих мыслях."
    "Тем не менее я чувствую себя вынужденной разделить с ней правду."
    show martha worried
    a "Когда я была свободна, я интересовалась мужчинами так же как и любая другая девушка моего возраста."
    a "Кроме того, из-за моей приятной внешности, я пользовалась популярностью у многих мужчин. Подарки были блестящи, и даже если я не отвечала на их привязанность, похвал было в изобилии."
    a eyesclosed1 "Но когда меня похитили… моя внешность стала проклятьем."
    "Я держалась за живот и дрожала, вспоминая время в заключении."
    a sad3 "Нет ничего приятного в том, чтобы быть красивой рабыней… Вообще ничего."
    a sad "И те мужчины… Вещи, которые бы они сделали с похищенными женщинами, особенно если найдут их привлекательными…"
    a eyesclosed3 "Я не думаю, что я когда-либо снова смогу думать о них положительно."
    "Марта посмотрела на меня с выражением горечи и раскаяния."
    "Что началось как комплимент, закончилось воспоминаниями, о которых было лучше забыть."
    "Даже если она не знает, что такое жизнь рабыни, Марта почувствовала очевидную вину за свои беспечные слова."
    m "Я… Я прошу прощения, Ада."
    m "Я не хотела вызвать у тебя такие неприятные воспоминания."
    a lookaway "Нет… Всё в порядке. Я знаю, ты не имела в виду ничего плохого."
    "Я натянула улыбку на своё лицо, пытаясь подумать о другой теме."
    "К счастью, с уже чистой Мартой, ещё и промокшей насквозь после купания, смена направления моего разговора стала очевидна."
    a smile2 "Знаешь, Марта… у тебя самой довольно приятное лицо."
    m oh "…Пардон?"
    a smile "Твоё лицо. И тело тоже."
    a smile2 "Ты довольно красивая девушка, Марта."
    m smile2 "Ха… Уверена, ты шутишь."
    m smile3 "Я понимаю твоё желание вернуть мне комплимент, но у меня нет никаких иллюзий о моей внешности."
    m smile "Как женщина, я мускульный зверь, и это совершенно меня не беспокоит."
    a surprised2 "…\"Зверь\", говоришь…"
    "Я криво улыбнулась, когда неожиданные особенности тела Марта показались на свет."
    m smile3 "В любом случае, достаточно болтовни. Мы должны отправляться."
    m neutral "Ты отдохнула? Готова уходить?"
    a "Ох, д..да. Я готова, когда ты не… Ах!"
    m "Мм? Что такое?"
    a scared "Его нет…"
    m "Чего?"
    a "Моего кошелька! Я, должно быть, обронила его, пока нас преследовали те гоблины!"
    m eyesclosed3 "Хах, не могу сказать, что удивлена. Та погоня была несомненно интенсивна."
    m eyesclosed2 "Всё же, кошелёк — малая цена за наши жизни."
    "По-видимому, не зная, сколько денег было потеряно или что значит моя утрата, Марта засмеялась, выставив свою грудь."
    a "Да, но… Марта, ты не понимаешь, что это значит?"
    a "Те монеты — всё, что у меня было. Без них я ничем не могу с тобой расплатиться."
    m neutral "Хмм? Ох, {i}это{/i} тебя беспокоит?"
    m eyesclosed3 "Ба, забудь об этом кошельке. Я отведу нас в Либертад с монетами или без."
    "Я в изумлении уставилась на Марту, когда она просто отбросила свою потерянную плату."
    "В отличие от впечатления, данного при нашей первой встрече, Марта на удивление добрая и она кажется менее заинтересованной материальными благами, чем я думала."
    "Пока мои спасители мной заинтересованы, я не могу быть более удачна."
    a smile2 "…Знаешь, Марта, ты правда хороший человек."
    m eyesclosed2 "Хм. Ещё комплименты?"
    m indifferent "Если у меня нет интереса к твоим монетам, что заставило тебя думать, что я желаю твоей хвалы?"
    a scared3 "Ох, ладно уже. Просто прими мою благодарность."
    a surprised2 "…Ах!"
    m eyesclosed3 "{i}*вздох*…{/i} Что на этот раз?"
    a "Кошелёк… Ты не думаешь, что те гоблины остановились, потому что они его нашли?"
    "Марта подняла одну брось и, мешкаясь, начала на меня смотреть."
    m indifferent "Столько гоблинов после потери стольких своих собратьев остановилось из-за одного кошелька?"
    m eyesclosed2 "Думаю, нет. Глупо было бы так думать, гоблины всё ещё предпочитают горячий обед из мяса и костей блестящим кускам металла."
    m neutral "…Хотя…"
    "Когда она прекратила говорить, Марта затихла."
    "Она положила руку под подбородок и наклонила голову, погрузившись в раздумья."
    m "Странно… Если не из-за твоего кошелька, тогда почему гоблины {i}остановили{/i} своё продвижение?"
    a "Хмм… Может, они поняли, что им не сравниться с тобой?"
    a "Или они могли решить попировать над своими собратьями, вместо нас."
    m smile2 "Ха! Гоблины-каннибалы?"
    m smile3 "Я бы не удивилась. Я определённо убила их на целый банкет."
    m smile "Хорошо, без разницы. Мы спаслись, это всё, что…"
    show martha shocked
    stop ambient
    stop music
    play sound audio.monster_footstep
    monster "{size=+10}РРРРРАААААААРРРРР!!!{/size}" with Shake((0, 0, 0, 0), 1.0, dist=30)
    play sound audio.monster_footstep
    pause 1
    play sound audio.monster_footstep
    a "…Марта..?"
    play music audio.enter_the_ogre
    scene white with Dissolve(1.5)
    scene ogre_bg:
        yalign 1.0
        ease 6.0 yalign 0.0
    show ogre:
        yanchor 1.0
        ypos config.screen_height
        yoffset 0
        xpos 50
        parallel:
            ease 6.0 yoffset 547
        parallel:
            linear 4.0 xpos 0
    show ogre_martha:
        yanchor 1.0
        ypos config.screen_height
        yoffset 0
        xpos 700
        parallel:
            ease 6.0 yoffset 547
        parallel:
            linear 4.0 xpos 900
    with Dissolve(0.2)
    pause 3.0
    "Видя оцепеневшее лицо Марты, я повернулась лицом к жуткому звуку, возникшему за мной."
    "Почти в три раза выше Марты, там стоял огр."
    "Отвратительное существо, заполненное мускулами с головы до ног и сжимавшее в одной руке искорёженный труп хобгоблина."
    "Его ужасающий рёв, утверждение его господства, заморозил Марту на месте, пока она смотрела на его ужасающий облик."
    "Марта не ожидала увидеть здесь огра. Она была уверена, что мы столкнёмся только с парой гоблинов; не армией гоблинов и определённо не огром."
    m fight3 "А… А…"
    m fight1 "Ада! Б..Беги!"
    "Марта наконец пришла в себя, но когда она прокричала моё имя, было слишком поздно."
    "Смотря на фигуру, которая напугала даже Марту, я застыла. Мой ум остановился, и я не могла пошевелиться."
    "Каждый нерв моего естества говорил меня бежать. Пара нейронов всё ещё обстреливала мой мозг командами спасаться."
    "Но я не могла."
    "Мой разум отключился, а моё тело угрожало упасть. Столкнувшись с такой громадной силой, я не могла сделать ничего, кроме как оставить надежду."
    "Я наконец встретила свой конец."
    m "Чёрт тебя, Ада! Убирайся оттуда!"
    m "Я сказала тебе, что доведу тебя до Либертада, разве нет?"
    "Марта кричала, пока бежала ко мне."
    "Огр, оценивавший меня, сдвинулся в то же время, отбросив свою мёртвую добычу и установившись на свою истинную."
    "Они оба бежали ко мне в одно и то же время, участвуя в гонке с моей жизнью на кону."
    "И победитель… "
    extend "Марта."
    m fight3 "Чёрт, Ада…"
    m fight1 "ЖИВИ!"
    "В долю секунду перед тем, как огр смог бы меня схватить, Марта врезалась в меня со всей силы."
    "Огр еле упустил нас двоих, и шок от внезапного удара наконец вернул меня в реальность."
    "Я подскочила на ноги и убежала так быстро как могла, не медля ни секунды, чтобы поблагодарить Марту или прокричать её имя."
    m fight2 "Хех… Теперь только ты и я, уродливый гад."
    m "Сделаем это."
    scene black with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

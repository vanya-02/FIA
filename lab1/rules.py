from production import IF, AND, THEN, OR, DELETE, NOT, FAIL


# TODO: implement your own rules according to the defined goal tree
# HINT: see an example in the file rules_example_zookeeper.py


TOURIST_RULES = (

    # 1
    IF(
        AND('(?x) uses a vpn', '(?x) uses public wifi'),
        THEN('(?x) is Tourist type 1, the broke one')
    ),
    # 2 
    IF(
        AND('(?x) visits museums', '(?x) takes pictures, a LOT of pictures; 10pics/hour'),
        THEN('(?x) is Tourist type 2, the cultured one')
    ),
    # 3
    IF(
       AND('(?x) has accent', '(?x) doesnt speak luna'),
       THEN('(?x) Tourist type 3, the foreigner') 
    ),
    # 4
    IF(
        AND('(?x) came out of an airport', '(?x) took the first waiting taxi'),
        THEN('(?x) is Tourist tytpe 4, the newbie')
    ),
    # 5
    IF(
        AND(
            OR('(?x) has sunglasses', '(?x) has hawaii t-shirts'), # -> on vacation
            '(?x) stays at a hotel'
        ),
        THEN('(?x) is Tourist type 5, the archetype')
    )
)


TOURIST_DATA = (
    'ion uses a vpn',
    'ion uses public wifi',
    'ion has sunglasses',
    'ion has hawaii t-shirts',
    'ion stays at a hotel',

    'maria uses a vpn',
    'maria uses public wifi',
    'maria has sunglasses',
    'maria has hawaii t-shirts',
    'maria stays at a hotel'
)

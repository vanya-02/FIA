from production import IF, AND, THEN, OR, DELETE, NOT, FAIL


# TODO: implement your own rules according to the defined goal tree
# HINT: see an example in the file rules_example_zookeeper.py


TOURIST_RULES = (

    # 1
    IF(
        AND('Uses a VPN', 'Uses public Wi-Fis'),
        THEN('Tourist type 1, the broke one')
    ),
    # 2 
    IF(
        AND('Visits museums', 'Takes pictures, a LOT of pictures; 10pics/hour'),
        THEN('Tourist type 2, the cultured one')
    ),
    # 3
    IF(
       AND('Has accent', 'Doesnt speak luna'),
       THEN('Tourist type 3, the foreigner') 
    ),
    # 4
    IF(
        AND('Came out of an airport', 'Took the first waiting taxi'),
        THEN('Tourist tytpe 4, the newbie')
    ),
    # 5
    IF(
        AND(
            OR('Has sunglasses', 'Has Hawaii t-shirts'), # -> on vacation
            'Stays at a hotel'
        ),
        THEN('Tourist type 5, the archetype')
    )
)


TOURIST_DATA = (
    'tim has feathers',
    'tim is a good flyer',
    'mark flies',
    'mark does not fly',
    'mark lays eggs',
    'mark swims',
    'mark has black and white color',
)

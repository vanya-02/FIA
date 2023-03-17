# TODO: add your imports here:
# from rules import my_rules



if __name__=='__main__':
    from rules import *
    from production import *
    from utils import *
    # from rules_example_zookeeper import ZOO_DATA, ZOOKEEPER_RULES

    print('FW Chain:\n')
        
    
    # res = forward_chain(TOURIST_RULES, TOURIST_DATA, apply_only_one=False, verbose=True)
    # print(res)

    res2 = backward_chain(TOURIST_RULES, 'vasea is Tourist type 5, the archetype', list_rules=None)
    print(res2)



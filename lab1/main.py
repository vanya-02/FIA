# TODO: add your imports here:
# from rules import my_rules



if __name__=='__main__':
    from production import *
    from rules import TOURIST_RULES, TOURIST_DATA

    print('FW Chain:')
        
    from rules_example_zookeeper import ZOO_DATA, ZOOKEEPER_RULES
    forward_chain(ZOOKEEPER_RULES, ZOO_DATA, apply_only_one=True)
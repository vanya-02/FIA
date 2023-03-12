# TODO: add your imports here:
# from rules import my_rules



if __name__=='__main__':
    from production import forward_chain
    from rules import TOURIST_RULES, TOURIST_DATA

    print('FW Chain:\n')
        
    from rules_example_zookeeper import ZOO_DATA, ZOOKEEPER_RULES
    res = forward_chain(TOURIST_RULES, TOURIST_DATA, apply_only_one=False)
    print(res)


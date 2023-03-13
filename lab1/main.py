# TODO: add your imports here:
# from rules import my_rules



if __name__=='__main__':
    from production import forward_chain, backward_chain
    from rules import TOURIST_RULES, TOURIST_DATA
    # from rules_example_zookeeper import ZOO_DATA, ZOOKEEPER_RULES

    print('FW Chain:\n')
        
    
    res = forward_chain(TOURIST_RULES, TOURIST_DATA, apply_only_one=False, verbose=True)
    print(res)

    res1 = backward_chain(TOURIST_RULES, TOURIST_DATA, verbose=True)
    print(res1)


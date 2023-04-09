# TODO: add your imports here:
# from rules import my_rules

if __name__=='__main__':
    from rules import *
    from production import *
    from utils import *


    def bw_system(then_conclusions=then_conclusions, possible_facts=possible_facts):
        tourist_name = input('Introduce tourist name: ')
        
        
        for i in range(len(then_conclusions)):
            then_conclusions[i] = then_conclusions[i].replace('(?x)', tourist_name)
            print(i, then_conclusions[i])

        hyposhesis = possible_facts[int(input('Select hypothesis number to check: '))]
        
        
        counter = 0
        print(f'\nPossible facts about {tourist_name}')
        for i in possible_facts:
            _ = i.replace('(?x)', tourist_name)
            print(f"{counter}, {_}")
            counter += 1
        
        facts = input('Selects the facts true from above: eg: (2 3 4) \n').split(' ')
        # print(facts)
        data = []
        for i in facts:
            data.append(possible_facts[int(i)])

        result = forward_chain(TOURIST_RULES, data, apply_only_one=True,verbose=False)
   
        return result



    bw_system(then_conclusions)
    

    


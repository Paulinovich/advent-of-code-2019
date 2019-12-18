'''
1. store input in list

2. save all different object (key) and orbits (values) in a list of dictionaries.

3. while len(list)!=1: 
    3.1. go over all dictionaries in the list and check if it's value is a key in one of the other dictionaries.
        3.1.1: yes: - make that value key in a new nested dictionary and append the orbitting dictionary as a value.
                    - pop that copied dictionary out of the list
        3.1.2: no: continue
    3.2. repeat the same process with the values of the nested dictionaries.
    3.3. and so on

4. iterate over the whole nested dictionary and count 'how deep' every value is and add this numbers together.
'''
# =================================================================================================
# Description: Using substrings in notebook
# Sha'Rya Weaver 5/12/2026
# Date: 5/12/2026
# =================================================================================================

test_name = "John Doe" 

def parse_and_display (name):
    for i in range(len(name)): 
        if name [i] == ' ': 
            first = name[:i] 
            last = name[i+1:] 
            print(f"Full name: {name}") 
            print(f"First name: {first}") 
            print(f"Last name: {last}")

parse_and_display(test_name)



test_list = ['Grace Flores', 'JB Oninonen', 'Ken Penn']

parse_and_display(test_list[0])



parse_and_display(test_list[2])



parse_and_display("Sha'Rya Weaver")

































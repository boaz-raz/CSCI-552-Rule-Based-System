## Step 1: Define the Working Memory and Rules
# Working memory: a list of facts
working_memory = ['hungry', 'food_available']

# Rules: a list of tuples (antecedents, consequent)
rules = [
    (('hungry', 'food_available'), 'eat'),
]

## Step 2: Implement the Rule Application Function
def apply_rule(rule, working_memory):
    antecedents, consequent = rule
    if all(item in working_memory for item in antecedents):
        if consequent not in working_memory:
            working_memory.append(consequent)
            return True
    return False


## Step 3: Implement the Forward-Chaining Mechanism
def run_ps(working_memory, rules):
    new_info_added = True
    while new_info_added:
        new_info_added = False
        for rule in rules:
            if apply_rule(rule, working_memory):
                new_info_added = True
                print(f"Applied rule: {rule} | New working memory: {working_memory}")
    return working_memory


## Step 4: Run the Production System
final_working_memory = run_ps(working_memory, rules)
print("Final working memory:", final_working_memory)


## Example Output
#Applied rule: (('hungry', 'food_available'), 'eat') | New working memory: ['hungry', 'food_available', 'eat']
#Final working memory: ['hungry', 'food_available', 'eat']
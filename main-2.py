## Step 1: Define the Working Memory and Rules
# Working memory: a list of observed symptoms and facts
working_memory = [
    'fever', 'cough', 'sore_throat', 'travelled_recently', 'contact_with_infected_person'
]

# Rules: a list of tuples (antecedents, consequent)
rules = [
    (('fever', 'cough', 'sore_throat'), 'common_cold'),
    (('fever', 'cough', 'difficulty_breathing'), 'possible_pneumonia'),
    (('fever', 'cough', 'sore_throat', 'travelled_recently'), 'possible_flu'),
    (('fever', 'cough', 'sore_throat', 'contact_with_infected_person'), 'possible_covid19'),
    (('common_cold',), 'advise_rest_and_fluids'),
    (('possible_pneumonia',), 'advise_see_doctor_immediately'),
    (('possible_flu', 'possible_covid19'), 'advise_test_for_covid19_and_flu'),
    (('advise_test_for_covid19_and_flu', 'advise_see_doctor_immediately'), 'high_risk_patient'),
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
print("*********************************************\n")
print("Final working memory:", final_working_memory)




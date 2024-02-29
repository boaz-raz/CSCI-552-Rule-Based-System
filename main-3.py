## Step 1: Define the Working Memory and Rules
# Working memory: a list of observed symptoms and facts
# working_memory = [
#     'warm_weather','cold_weather','winter' 'kids', 'over_7_days', 'quiet_vacation', 'active_vacation', 'nature', 'urban','flying','less_7_days'
# ]

working_memory = [
    'warm_weather', 'active_vacation', 'nature', 'over_7_days', 'flying'
]
# Rules: a list of tuples (antecedents, consequent)
rules = [
    # Rule for warm, active, nature vacations over 7 days
    (('warm_weather', 'active_vacation', 'nature', 'over_7_days'), 'Costa Rica - Explore rainforests and beaches'),

    # Rule for quiet, urban vacations in cold weather
    (('cold_weather', 'quiet_vacation', 'urban'), 'Vienna in winter - Enjoy museums and coffee houses'),

    # Rule for family vacations with kids in warm weather
    (('warm_weather', 'kids'), 'Orlando, Florida - Theme parks and family fun'),

    # Rule for short, active vacations in urban settings
    (('urban', 'active_vacation', 'less_7_days'), 'New York City - A fast-paced city adventure'),

    # Rule for nature vacations in cold weather
    (('cold_weather', 'nature'), 'Banff, Canada - Winter sports and stunning landscapes'),

    # Rule for quiet vacations in nature
    (('quiet_vacation', 'nature'), 'Sedona, Arizona - Relaxing desert retreat'),

    # Rule for winter vacations with kids
    (('winter', 'kids'), 'Lapland, Finland - Meet Santa and see the Northern Lights'),

    # Rule for flying to exotic locations for more than a week
    (('flying', 'over_7_days'), 'Maldives - Overwater bungalows and scuba diving'),
]

## Step 2: Implement the Rule Application Function
def apply_rule(rule, working_memory):
    antecedents, consequent = rule
    if all(item in working_memory for item in antecedents):
        return consequent
    return None

## Step 3: Implement the Forward-Chaining Mechanism
def recommend_destinations(working_memory, rules):
    recommendations = []
    for rule in rules:
        recommendation = apply_rule(rule, working_memory)
        if recommendation:
            recommendations.append(recommendation)
    return recommendations

## Step 4: Run the Production System
recommendations = recommend_destinations(working_memory, rules)
print("Recommended Vacation Destinations:")
for recommendation in recommendations:
    print(f"- {recommendation}")




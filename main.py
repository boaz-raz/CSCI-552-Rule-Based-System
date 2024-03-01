import argparse

def apply_rule(rule, working_memory):
    """Check if the rule's antecedents are all in the working memory."""
    antecedents, consequent = rule
    if all(item in working_memory for item in antecedents):
        return consequent
    return None

def recommend_destinations(working_memory):
    """Recommend vacation destinations based on the working memory."""
    rules = [
        (('warm_weather', 'active_vacation', 'nature', 'over_7_days'), 'Costa Rica - Explore rainforests and beaches'),
        (('cold_weather', 'quiet_vacation', 'urban'), 'Vienna in winter - Enjoy museums and coffee houses'),
        (('warm_weather', 'kids'), 'Orlando, Florida - Theme parks and family fun'),
        (('urban', 'active_vacation', 'less_7_days'), 'New York City - A fast-paced city adventure'),
        (('cold_weather', 'nature'), 'Banff, Canada - Winter sports and stunning landscapes'),
        (('quiet_vacation', 'nature'), 'Sedona, Arizona - Relaxing desert retreat'),
        (('winter', 'kids'), 'Lapland, Finland - Meet Santa and see the Northern Lights'),
        (('flying', 'over_7_days'), 'Maldives - Overwater bungalows and scuba diving'),
    ]

    recommendations = []
    for rule in rules:
        recommendation = apply_rule(rule, working_memory)
        if recommendation:
            recommendations.append(recommendation)
    return recommendations

def main():
    # Prompt the user for their preferences
    print("All options: 'warm_weather','cold_weather','winter' 'kids', 'over_7_days', 'quiet_vacation', 'active_vacation', 'nature', 'urban','flying','less_7_days'\n")

    print("Enter your vacation preferences separated by commas (e.g., warm_weather, kids, over_7_days):")

    user_input = input()
    preferences = [pref.strip() for pref in user_input.split(',')]  # Convert string to list and remove any extra whitespace

    # Generate recommendations
    recommendations = recommend_destinations(preferences)
    print("\nRecommended Vacation Destinations based on your preferences:")
    for recommendation in recommendations:
        print(f"- {recommendation}")

if __name__ == "__main__":
    main()

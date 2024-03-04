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
        (('warm_weather', 'over_7_days', 'nature', 'quiet_vacation'), 'Belize - Explore ancient Mayan ruins and lush rainforests'),
        (('cold_weather', 'winter', 'kids', 'nature'), 'Aspen, Colorado - Family-friendly ski resort with activities for all ages'),
        (('urban', 'less_7_days', 'flying'), 'London, England - A quick urban getaway with rich history and modern attractions'),
        (('active_vacation', 'winter', 'flying'), 'Chamonix, France - Thrilling winter sports and mountaineering'),
        (('quiet_vacation', 'cold_weather', 'less_7_days'), 'Reykjavik, Iceland - Relax in geothermal spas and explore Viking history'),
        (('nature', 'over_7_days', 'kids'), 'Yellowstone National Park, USA - Family camping and wildlife watching'),
        # Family-friendly vacations in warm weather
        (('warm_weather', 'kids', 'over_7_days'), 'San Diego, California - Enjoy beaches and zoos'),

        # Active winter vacations
        (('cold_weather', 'winter', 'active_vacation'), 'Whistler, Canada - Skiing and snowboarding adventures'),

        # Quiet urban retreats
        (('quiet_vacation', 'urban', 'less_7_days'), 'Charleston, South Carolina - Historic city with a relaxed pace'),

        # Nature escapes with warm weather
        (('warm_weather', 'nature', 'over_7_days'), 'Costa Rica - Rainforests, volcanoes, and beaches'),

        # Short, urban, and active vacations
        (('urban', 'active_vacation', 'less_7_days'), 'Barcelona, Spain - Explore the city by bike or on foot'),

        # Flying to a cold, adventurous destination
        (('flying', 'cold_weather', 'active_vacation'), 'Reykjavik, Iceland - Glacier hikes and hot springs'),

        # Warm urban vacations for more than a week
        (('warm_weather', 'urban', 'over_7_days'), 'Miami, Florida - Vibrant city life and warm beaches'),

        # Quiet vacations in nature during winter
        (('quiet_vacation', 'nature', 'winter'), 'Banff, Alberta - Serene snowy landscapes and hot springs'),

        # Active vacations in nature for families
        (('active_vacation', 'nature', 'kids'), 'Yellowstone National Park, USA - Geysers and wildlife'),

        # Urban adventures in cold weather
        (('cold_weather', 'urban', 'active_vacation'), 'New York City, USA - Winter in the city with ice skating'),

        # Warm weather vacations for nature lovers
        (('warm_weather', 'nature'), 'Galápagos Islands, Ecuador - Unique wildlife and pristine beaches'),

        # Quiet, urban vacations in warm weather
        (('quiet_vacation', 'urban', 'warm_weather'), 'Savannah, Georgia - Warm hospitality and historic charm'),

        # Active vacations in cold urban settings
        (('active_vacation', 'urban', 'cold_weather'), 'Chicago, Illinois - Winter activities and city tours'),

        # Nature-focused vacations in cold weather
        (('cold_weather', 'nature'), 'Alaska, USA - Northern Lights and wildlife expeditions'),

        # Urban cultural vacations for families
        (('urban', 'kids', 'culture'), 'London, England - Museums and historical sights for all ages'),

        # Active, short vacations in warm weather
        (('active_vacation', 'warm_weather', 'less_7_days'), 'Key West, Florida - Water sports and sunsets'),

        # Quiet, nature retreats in warm weather
        (('quiet_vacation', 'nature', 'warm_weather'), 'Kauai, Hawaii - Tranquil beaches and gardens'),

        # Family vacations in urban winter settings
        (('urban', 'winter', 'kids'), 'Vienna, Austria - Winter markets and snow-covered palaces'),

        # Flying to nature destinations in winter
        (('flying', 'nature', 'winter'), 'Patagonia, Argentina - Dramatic glaciers and mountain treks'),

        # Short, active, nature vacations in cold weather
        (('active_vacation', 'nature', 'cold_weather', 'less_7_days'), 'Lake Tahoe, California/Nevada - Skiing and snowboarding'),

        # Warm, urban vacations under a week
        (('urban', 'warm_weather', 'less_7_days'), 'Las Vegas, Nevada - Entertainment and poolside relaxation'),

        # Quiet, short vacations in cold urban settings
        (('quiet_vacation', 'urban', 'cold_weather', 'less_7_days'), 'Quebec City, Canada - European charm in North America'),

        # Warm weather, active vacations for families
        (('warm_weather', 'active_vacation', 'kids'), 'Orlando, Florida - Theme parks and entertainment'),

        # Nature vacations in warm weather for over a week
        (('nature', 'warm_weather', 'over_7_days'), 'Madagascar - Explore unique biodiversity and landscapes'),

        # Cold, quiet vacations in nature
        (('cold_weather', 'quiet_vacation', 'nature'), 'Lapland, Finland - Quiet snowscapes and cozy cabins'),

        # Urban adventures for more than a week
        (('urban', 'over_7_days'), 'Tokyo, Japan - Dive into a vibrant and diverse metropolis'),

        # Active, nature-based vacations flying to destination
        (('active_vacation', 'nature', 'flying'), 'Nepal - Trekking in the Himalayas'),

        # Short, warm, quiet urban vacations
        (('quiet_vacation', 'urban', 'warm_weather', 'less_7_days'), 'Seville, Spain - Warm climate and rich history'),

        # Family vacations flying to warm destinations
        (('flying', 'warm_weather', 'kids'), 'Maui, Hawaii - Beaches and family-friendly adventures'),

        # Active winter vacations in urban settings
        (('active_vacation', 'urban', 'winter'), 'Montreal, Canada - Ice skating and festivals in a vibrant city'),

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

    print("Enter your vacation preferences separated by commas (e.g., warm_weather,over_7_days,nature,quiet_vacation):")

    user_input = input()
    preferences = [pref.strip() for pref in user_input.split(',')]  # Convert string to list and remove any extra whitespace

    # Generate recommendations
    recommendations = recommend_destinations(preferences)
    print("\nRecommended Vacation Destinations based on your preferences:")
    for recommendation in recommendations:
        print(f"- {recommendation}")

if __name__ == "__main__":
    main()

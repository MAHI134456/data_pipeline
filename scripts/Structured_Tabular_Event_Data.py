import pandas as pd

# Define your event data
events = [
    {"Date": "1990-08-02", "Event Description": "Gulf War oil shock begins"},
    {"Date": "1998-12-10", "Event Description": "Asian Financial Crisis drives prices to record low"},
    {"Date": "2008-07-11", "Event Description": "Oil hits record high (~$147) before crash"},
    {"Date": "2008-12-20", "Event Description": "Global Financial Crisis oil price collapse"},
    {"Date": "2011-02-01", "Event Description": "Arab Spring creates oil market volatility"},
    {"Date": "2014-06-20", "Event Description": "Oil crash starts due to oversupply"},
    {"Date": "2016-01-20", "Event Description": "Oil hits low ($27) due to continued surplus"},
    {"Date": "2020-04-01", "Event Description": "COVID-19 pandemic causes price collapse"},
    {"Date": "2022-03-01", "Event Description": "Russia-Ukraine war spikes oil prices"}
]

# Convert to DataFrame
event_df = pd.DataFrame(events)

# Save as CSV
event_df.to_csv("data/oil_market_events.csv", index=False)

print("Event data saved to 'data/oil_market_events.csv'")

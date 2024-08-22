import pandas as pd
import plotly.graph_objects as go

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0080__Day76_Beautiful_Plotly_Charts_&_Android_Store__240820\NewProject\r00-r09 START\r00_env_START\apps.csv'
df = pd.read_csv(file_path)

# Group the data by 'Category' and 'Type' (Free or Paid), and count the number of apps in each group
category_type_counts = df.groupby(['Category', 'Type'], as_index=False).agg({'App': 'count'})

# Rename the 'App' column to 'Count' to reflect the number of apps
category_type_counts.rename(columns={'App': 'Count'}, inplace=True)

# Calculate the total number of apps (free + paid) for each category
category_totals = category_type_counts.groupby('Category')['Count'].sum().sort_values(ascending=False)

# Select the top 20 categories based on total app count
top_categories = category_totals.head(20).index

# Filter the original dataframe to include only these top categories
category_type_counts_top = category_type_counts[category_type_counts['Category'].isin(top_categories)]

# Create the dual bar graph
fig = go.Figure()

# Add bars for Free apps
fig.add_trace(go.Bar(
    x=category_type_counts_top[category_type_counts_top['Type'] == 'Free']['Category'],
    y=category_type_counts_top[category_type_counts_top['Type'] == 'Free']['Count'],
    name='Free',
    marker_color='blue'
))

# Add bars for Paid apps
fig.add_trace(go.Bar(
    x=category_type_counts_top[category_type_counts_top['Type'] == 'Paid']['Category'],
    y=category_type_counts_top[category_type_counts_top['Type'] == 'Paid']['Count'],
    name='Paid',
    marker_color='red'
))

# Update the layout with titles and labels
fig.update_layout(
    title='Free vs Paid Apps by Category',
    xaxis_title='Category',
    yaxis_title='Number of Apps',
    barmode='group'  # Group bars together
)

# Ensure the categories are sorted by the total number of apps from highest to lowest
fig.update_xaxes(categoryorder='total descending')

# Show the plot
fig.show()

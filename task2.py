import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


df = pd.read_csv('C:/Users/DELL/Desktop/data.csv')

df['date'] = pd.to_datetime(df['date'])

columns_to_plot = [
    'date', 'price', 'bedrooms', 'bathrooms',
    'sqft_living', 'sqft_lot', 'floors', 'waterfront',
    'view', 'condition'
]

custom_bins = {
    'date': 10,
    'price': 20,
    'bedrooms': range(0, 11),
    'bathrooms': range(0, 9),
    'sqft_living': 30,
    'sqft_lot': 30,
    'floors': [1, 1.5, 2, 2.5, 3, 3.5],
    'waterfront': [0, 1],
    'view': [0, 1, 2, 3, 4],
    'condition': [1, 2, 3, 4, 5]
}

sns.set_style("whitegrid")

fig, axes = plt.subplots(2, 5, figsize=(25, 8))
axes = axes.flatten()

for i, col in enumerate(columns_to_plot):
    ax = axes[i]
    bins = custom_bins.get(col, 10)

    if col == 'date':
        sns.histplot(df[col], ax=ax, bins=bins, color='darkblue')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.tick_params(axis='x', rotation=45)
    else:
        sns.histplot(df[col], ax=ax, bins=bins, color='darkblue')
        ax.tick_params(axis='x', rotation=0)

    ax.set_title(f'# {col}', fontsize=11)

plt.tight_layout()
plt.show()

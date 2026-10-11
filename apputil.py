import plotly.express as px
import pandas as pd
import numpy as np

# update/add code below ...
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')
df_column_rename= df.columns.str.lower().str.replace(' ', '_')
df.columns = df_column_rename


def survival_demographics():
    # Categorize passengers by age
    df['age_group'] = pd.cut(
        df['age'],
        bins=[0, 13, 20, 60, np.inf],
        labels=['Child', 'Teen', 'Adult', 'Senior'],
        right=False
    )
# Group by passenger class, sex, and age category
   
    grouped = df.groupby(['pclass', 'sex', 'age_group'],observed=False)

    n_passengers = grouped['pclass'].count()
    n_survivors = grouped['survived'].sum()

    survival_rate = n_survivors / n_passengers * 100

    df2 = pd.DataFrame({
        'n_passengers': n_passengers,
        'n_survivors': n_survivors,
        'survival_rate': survival_rate
    })

    df2 = df2.reset_index()
    df2 = df2.sort_values(by=['pclass', 'sex', 'age_group'])
# Return the results
    return df2
results = survival_demographics()
print(results)


# Filter for child passengers only
child_only=results[results['age_group']=='Child']
# Calculate survival rate for child passengers
grouped_children = child_only.groupby('pclass')

# Calculate survival rate for child passengers
child_survival_rate = (
    grouped_children['n_survivors'].sum()
    /grouped_children['n_passengers'].sum()
    * 100

)
# Create a DataFrame with the child survival rates
child_survival_index = child_survival_rate.reset_index()
child_survival_index_df= pd.DataFrame(child_survival_index)
child_survival_rename=child_survival_index_df.rename(columns={0: 'child_survival_rate'})

print(child_survival_rename)

def visualize_demographic():
    # Create a bar chart for child survival rates by passenger class
    child_survival_rate_fig=child_survival_rename

# Create a bar chart for child survival rates by passenger class
    child_survival_rate_fig['pclass']=child_survival_rate_fig['pclass'].astype(str)
    fig=px.bar( child_survival_rate_fig,
            x='pclass',
            y='child_survival_rate',
            hover_data=['child_survival_rate'],
            template='simple_white',
            labels={'pclass': 'Passenger Class', 'child_survival_rate': 'Child Survival Rate'}

)
    return fig


def family_groups():
    
  # Create a new column for family size
   df['family_size']=df['sibsp'] + df['parch'] + 1
    # Group by family size and passenger class
   family_groupby=df.groupby(['family_size','pclass']).agg(
        n_passengers=('pclass', 'count'),
        avg_fare=('fare', 'mean'),
        max_fare=('fare', 'max'),
        min_fare=('fare', 'min')
    ) 
   # Sort the results
   family_sort=family_groupby.sort_values(['pclass','family_size']).reset_index()
   return family_sort
print(family_groups())


def last_names():

    # Extract last names from the 'name' column
    last_name_extraction= df['name'].str.split(',').str[0].value_counts()
    return last_name_extraction
print(last_names())


def visualize_families():
    family_size_fare = family_groups()

    fig2 = px.line(
        family_size_fare,
        x='family_size',
        y='avg_fare',
        color='pclass',
        template='simple_white',
        title='Average Fare by Family Size and Passenger Class',
        labels={
            'family_size': 'Family Size',
            'avg_fare': 'Average Fare ($)'
        }
    )

    return fig2
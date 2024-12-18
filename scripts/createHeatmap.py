from datetime import datetime
import calendar
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def parse_movie_dates(file_path='./media/rating.md'):
    """
    Parse movie dates from the markdown file using line-by-line parsing.
    
    :param file_path: Path to the markdown file
    :return: List of dates when movies were watched
    """
    dates = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Look for the line that starts with "- **Date** : "
            if line.strip().startswith("- **Date** : "):
                # Extract the date by removing the prefix
                date_str = line.strip().replace("- **Date** : ", "").strip()
                dates.append(date_str)
    
    return dates

def create_yearly_monthly_heatmap(dates, years=None):
    """
    Create a heatmap of movie counts by month and year.
    
    :param dates: List of dates when movies were watched
    :param years: Optional list of years to include (defaults to all found years)
    """
    # Convert string dates to datetime objects using flexible parsing
    parsed_dates = [datetime.strptime(date, '%d %B %Y') for date in dates]
    
    # Create a DataFrame with year, month, and count
    df_dates = pd.DataFrame({
        'year': [date.year for date in parsed_dates],
        'month': [date.month for date in parsed_dates]
    })
    
    # Determine years to include
    if years is None:
        years = sorted(df_dates['year'].unique(), reverse=True)  # Sort in descending order
    
    # Filter DataFrame to include only specified years
    df_dates = df_dates[df_dates['year'].isin(years)]
    
    # Group by year and month, count movies
    movie_counts = df_dates.groupby(['year', 'month']).size().reset_index(name='count')
    # return movie_counts

    movie_counts = movie_counts.sort_values(by=['year', 'month'], ascending=[False, False])
    
    # Pivot the data for heatmap
    heatmap_data = movie_counts.pivot(index='year', columns='month', values='count').fillna(0).sort_values(
        by = ['year'], ascending = False
    )

    
    
    # Reorder columns to match calendar months
    heatmap_data = heatmap_data.reindex(columns=range(1, 13))
    
    heatmap_data  =heatmap_data.fillna(0)

    plt.figure(figsize=(15, 4))
    
    custom_cmap = sns.light_palette("forestgreen", as_cmap=True)
    
    ax = sns.heatmap(
        heatmap_data, 
        cmap=custom_cmap,  
        annot=True,        
        fmt='g',           
        cbar_kws={'label': 'Number of Movies Watched'}
    )
    
    
    # plt.title('Movie Viewing Heatmap', fontsize=15)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Year', fontsize=12)
    
    # Replace month numbers with month names
    month_names = [calendar.month_abbr[i] for i in range(1, 13)]
    plt.xticks(ticks=np.arange(12) + 0.5, labels=month_names, rotation=45)
    
    # Save the heatmap
    plt.tight_layout()
    plt.savefig('scripts/movieCountbyMonth.png')
    plt.close()
    
    print("Heatmap saved as 'movieCountbyMonth.png'")
    
    print()
    print("Movie Counts by Year and Month:")
    print(heatmap_data)
    
    return heatmap_data

def main():
    movie_dates = parse_movie_dates()
    
    # Create heatmap with latest year on top
    print(
        create_yearly_monthly_heatmap(movie_dates, years=[2024, 2023])
    )

if __name__ == "__main__":
    main()
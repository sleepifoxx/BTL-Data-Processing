# YouTube Trending Videos Analysis

This project analyzes YouTube trending videos data to extract insights and visualize trends.

## Documentation

https://docs.google.com/document/d/1KujHJcI8381W0r-KqD1GsFH3SgMF77iM/edit?usp=sharing&ouid=100271396827143112782&rtpof=true&sd=true

## Project Structure

- Data:
    + api_data.csv 
    + trending_videos_unique.csv
    + trending_videos.csv 
    + VN_trending_videos.csv 
- DataCrawling.ipynb 
- DataModeling.ipynb 
- DataVisualization.ipynb 
- README.md

## Notebooks

- **DataCrawling.ipynb**: Crawls and processes YouTube trending videos data.
- **DataModeling.ipynb**: Builds and evaluates models to predict trends.
- **DataVisualization.ipynb**: Visualizes the data and trends using various plots.

## Data

- **api_data.csv**: Data fetched from YouTube API.
- **trending_videos.csv**: Processed trending videos data.
- **trending_videos_unique.csv**: Unique trending videos data.
- **VN_trending_videos.csv**: Trending videos data specific to Vietnam.

## Setup

1. Clone the repository.
2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the notebooks in the following order:
    1. `DataCrawling.ipynb`
    2. `DataModeling.ipynb`
    3. `DataVisualization.ipynb`

## Usage

- **DataCrawling.ipynb**: Run this notebook to fetch and preprocess the data.
- **DataModeling.ipynb**: Run this notebook to build and evaluate predictive models.
- **DataVisualization.ipynb**: Run this notebook to visualize the data and trends.

## License

This project uses only for study.
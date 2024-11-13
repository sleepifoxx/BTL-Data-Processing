%pip install
from googleapiclient.discovery import build
from datetime import datetime
import pandas as pd

def get_trending_videos(api_key, region_code='VN', max_results=10):
    """
    Lấy thông tin về video trending trên YouTube.
    
    Args:
        api_key (str): YouTube Data API key
        region_code (str): Mã quốc gia (mặc định: 'VN' cho Việt Nam)
        max_results (int): Số lượng video muốn lấy (mặc định: 10)
    
    Returns:
        pandas.DataFrame: DataFrame chứa thông tin về các video trending
    """
    
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Lấy danh sách video trending
    request = youtube.videos().list(
        part='snippet,statistics',
        chart='mostPopular',
        regionCode=region_code,
        maxResults=max_results
    )
    response = request.execute()
    
    # Xử lý dữ liệu
    video_data = []
    for item in response['items']:
        video_info = {
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'publish_time': item['snippet']['publishedAt'],
            'view_count': item['statistics']['viewCount'],
            'like_count': item['statistics'].get('likeCount', 0),
            'comment_count': item['statistics'].get('commentCount', 0),
            'video_id': item['id']
        }
        
        # Chuyển đổi thời gian từ ISO format sang datetime
        publish_time = datetime.strptime(item['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        video_info['time_to_trending'] = (datetime.utcnow() - publish_time).total_seconds() / 3600  # Số giờ
        
        video_data.append(video_info)
    
    # Tạo DataFrame
    df = pd.DataFrame(video_data)
    
    # Sắp xếp theo thời gian lên trending
    df = df.sort_values('time_to_trending')
    
    return df

def main():
    # Thay YOUR_API_KEY bằng API key của bạn
    API_KEY = 'AIzaSyD62vGXCRcS9ZTktlFWALDb-5tmnpewW1w'
    
    try:
        # Lấy dữ liệu
        trending_videos = get_trending_videos(API_KEY)
        
        # In kết quả
        print("\nThông tin video trending trên YouTube:")
        print("=====================================")
        
        for idx, video in trending_videos.iterrows():
            print(f"\n{idx + 1}. {video['title']}")
            print(f"Kênh: {video['channel']}")
            print(f"Thời gian đăng: {video['publish_time']}")
            print(f"Thời gian để lên trending: {video['time_to_trending']:.2f} giờ")
            print(f"Lượt xem: {int(video['view_count']):,}")
            print(f"Link: https://youtube.com/watch?v={video['video_id']}")
            
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")

if __name__ == "__main__":
    main()
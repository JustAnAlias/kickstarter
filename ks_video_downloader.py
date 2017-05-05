from bs4 import BeautifulSoup
import webget
import urllib.request


def scrape_videos(url=None, savepath=None):
    res = None
    if not url:
        url = 'https://www.kickstarter.com/projects/videoanalysis/videoanalysis-for-everyone'
        print('downloading test example')
    if not savepath:
        savepath = 'test.mp4'
    data = webget.download(url)
    soup = BeautifulSoup(data, 'html.parser')
    video_tags = soup.findAll('video')
    for tag in video_tags:
        video_urls = tag.findAll('source')
        for video_url in video_urls:
            if 'base.mp4' in video_url.get('src'):
                res = video_url.get('src')
                file_name = res.split('/')[-1]
                print('downloading : {0} to {1}'.format(res, file_name))

                urllib.request.urlretrieve(res, file_name)

if __name__ == '__main__':
    scrape_videos()

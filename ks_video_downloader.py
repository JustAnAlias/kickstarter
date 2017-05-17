from bs4 import BeautifulSoup
import webget
import urllib.request
import json
import os
from tqdm import tqdm

class VideoDownloader:

    def __init__(self):
        self.data = self.load_data('data.json')
        # print(self.data)

    def run(self):
        for k in tqdm(self.data.keys()):
            vid_files = self.scrape_videos(self.data[k]['url'])
            self.data[k]['videos'] = vid_files
        self.save_data('data2.json', self.data)
            # print('{}: {}'.format(k, self.data[k]['url']))

    def create_video_dir(self, url):
        subdir = url.split('/')[-1]
        current = os.curdir
        res = os.path.join(current, 'videos', subdir)
        if os.path.isdir(res):
            # print(res, ' already exists')
            return res
        else:
            os.makedirs(res)
            # print(res, ' was created')
            return res

    def load_data(self, file_path):
        print('loading data')
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
        return data

    def save_data(self, file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def create_file_name(self, url, number):
        identifier = url.split('/')[-1]
        separator = "-"
        res = separator.join([identifier, str(number), 'base.mp4'])
        return res

    def scrape_videos(self, url):
        res = None
        savedir = self.create_video_dir(url)
        file_list = []
        data = webget.download(url)
        soup = BeautifulSoup(data, 'html.parser')
        video_tags = soup.findAll('video')
        for tag in video_tags:
            video_urls = tag.findAll('source')
            video_counter = 0
            for video_url in video_urls:
                if 'base.mp4' in video_url.get('src'):
                    video_counter += 1
                    res = video_url.get('src')
                    file_name = self.create_file_name(url, video_counter)
                    full_path = os.path.join(savedir, file_name)
                    file_list.append(full_path)
                    if video_counter >= 2:
                        print('downloading file number {0} : {1} to {2}'.format(video_counter, res, full_path))
                    if os.path.isfile(full_path):
                        # print('i already have that file')
                        continue
                    else:
                        urllib.request.urlretrieve(res, full_path)
        return file_list

if __name__ == '__main__':
    shit = VideoDownloader()
shit.run()

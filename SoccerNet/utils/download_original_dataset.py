# Codingan untuk mengunduh dataset SoccerNet untuk tugas tracking-2023.

from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="dataset/SoccerNet",)
mySoccerNetDownloader.downloadDataTask(task="tracking-2023", split=["train", "test"])
import io
import pathlib
import requests
from zipfile import ZipFile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

DOWNLOADS = '/downloads'

def create_directory_if_not_exists(path):
    pathlib.Path(path).mkdir(exist_ok=True)


def download_file(uri):
    file_name = uri.split('/')[-1].split('.')[0]
    # download zip file
    response = requests.get(uri)
    zipped = ZipFile(io.BytesIO(response.content))
    # extract zip file and save as a csv
    zipped.extractall(f'{DOWNLOADS}/{file_name}.csv')


def main():
    create_directory_if_not_exists(DOWNLOADS)
    for uri in download_uris:
        try:
            download_file(uri)
        except Exception:
            print(f"Unable to download file from {uri}")

    # print the downloaded file paths
    downloaded_files = pathlib.Path(DOWNLOADS).iterdir()
    for file in downloaded_files:
        print(file)


if __name__ == "__main__":
    main()

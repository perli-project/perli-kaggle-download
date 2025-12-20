import os
from kaggle.api.kaggle_api_extended import KaggleApi


def download_kaggle_datasets(dataset_list):
    """
    dataset_list: [(dataset_id, save_path), ...] 형태의 리스트
    """
    # kaggle.json 위치 설정 (현재 폴더)
    os.environ['KAGGLE_CONFIG_DIR'] = "."

    api = KaggleApi()
    api.authenticate()

    for dataset_name, path in dataset_list:
        print(f"다운로드 중: {dataset_name} -> {path}")
        api.dataset_download_files(dataset_name, path=path, unzip=True)
        print(f"설치 완료: {path}")
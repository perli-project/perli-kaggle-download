from modules.download.downloader import download_kaggle_datasets

def main():
    # 다운로드할 데이터셋 설정 (ID, 저장경로)
    datasets = [
        ("uciml/default-of-credit-card-clients-dataset", "./data/first_dataset"),
        ("olistbr/brazilian-ecommerce", "./data/second_dataset")
    ]

    try:
        download_kaggle_datasets(datasets)
        print("\n모든 데이터셋 다운로드 프로세스가 종료되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
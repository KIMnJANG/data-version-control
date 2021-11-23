# Data Version Control

MNIST 데이터를 제 개인 버킷에 저장했고 버전관리는 https://github.com/ssuwani/dvc-tutorial 여기에서 하고 있습니다. DVC API는 DVC에서 제공하는 Python SDK인데 제 레포에 접근해 태그 기반으로 데이터를 불러올 수 있습니다.

아무런 권한 없이 아래의 내용을 따라하면 데이터를 읽어올 수 있습니다. 이게 가능한 이유는 GCS 버킷내 해당 폴더를 allUser에게 Readable하게 설정해두었습니다. 주의!!

### Install 

```bash
pip install dvc[gs]
```



[`main.py`](main.py) 는 `tf.keras.datasets.mnist.load_data()` 를 `dvc.api`로 대체한 데모입니다.

```python
with dvc.api.open(
    'data/dataset.npz',
    repo='https://github.com/ssuwani/dvc-tutorial',
    mode="rb"
) as fd:
    dataset = np.load(fd)
    train_x = dataset["train_x"]
    train_y = dataset["train_y"]
    test_x = dataset["test_x"]
    test_y = dataset["test_y"]
```

**특정 버전의 데이터를 불러오기**

```python
with dvc.api.open(
    'data/dataset.npz',
    repo='https://github.com/ssuwani/dvc-tutorial',
    mode="rb",
    rev="refs/tags/v0.2" # v0.2 버전의 데이터 20000개의 학습용 데이터 불러올 수 있습
) as fd:
    dataset = np.load(fd)
    train_x = dataset["train_x"]
    train_y = dataset["train_y"]
    test_x = dataset["test_x"]
    test_y = dataset["test_y"]
```

- v0.1 : 10000개의 학습용 데이터
- v0.2 : 20000개의 학습용 데이터
- v0.3 : 30000개의 학습용 데이터
- v0.4 : 40000개의 학습용 데이터
- v0.5 : 50000개의 학습용 데이터
- v0.6 : 60000개의 학습용 데이터
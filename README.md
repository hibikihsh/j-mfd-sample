# J-MFD Sample

## 概要

J-MFD（Japanese Morphological and Functional Dictionary）を使用した日本語テキストの形態素解析と単語抽出を行うツール。

### 主な特徴

- CSVファイルからテキストデータを読み込み
- MeCabを使った形態素解析
- J-MFD辞書に基づく単語のカウント
- カテゴリ別の単語出現頻度分析

## 環境構築

### 必要な依存関係

#### MeCab
```bash
# macOS (Homebrew)
brew install mecab mecab-ipadic

# Ubuntu/Debian
sudo apt-get install mecab mecab-ipadic-utf8 libmecab-dev

# CentOS/RHEL
sudo yum install mecab mecab-ipadic mecab-devel
```

#### Python パッケージ
```bash
pip install mecab-python3 ipadic
```

### セットアップ

1. リポジトリをクローン
```bash
git clone <repository-url>
cd j-mfd-sample
```

2. Python仮想環境の作成（推奨）
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

4. J-MFD辞書ファイルの配置
   - `./data/J-MFD.csv` に辞書ファイルを配置してください

## command

### 形態素解析と単語の抽出

```python
python main.py -f {file_path}
```

## references
- https://github.com/soramame0518/j-mfd
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0213343
- https://confit.atlas.jp/guide/event-img/jsai2018/3O1-OS-1a-01/public/pdf?type=in

# 掃除しなくちゃ

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2021/07/JPHACKS2021_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
### 背景(製品開発のきっかけ）
#### シチュエーション１
  * 普段掃除をしようと思っててもやる気が出てこない. まだ, 大丈夫....
  それが続いている... 掃除をするやる気を奮い立たせたい
  自分の部屋の汚さを可視化してみよう！
#### シチュエーション２
* あのこちゃんと掃除してるかしら?
不安だわ... 掃除してるって言ってるけど本当かしら...
遠隔で見守りたいわ
### 汚い部屋の例
* #### 埃っぽい部屋
* #### 匂いが気になる部屋
* #### 足の踏み場がない
### 課題
### 部屋の汚さの定義
* #### 埃っぽい部屋  
   * アレルギー反応（くしゃみ、鼻水）が出る  
* #### 匂う部屋  
   * 違和感を感じる匂いの発生  
### 製品説明（具体的な製品の説明）
 * 空気品質センサや環境センサ, ダストセンサを用いて屋内の環境情報を収集しセンサの情報を独自のアルゴリズムで部屋の汚さを可視化することによって危機感を煽り, 掃除のモチベーションを上げる
### 特長

#### 1. 部屋の汚さの測定

#### 2. 測定した数値を可視化する

#### 3. データを遠隔で共有する

### 解決出来ること
   * 部屋の汚さの度合いが分かる　　
   * 掃除するモチベーションの上昇
### 今後の展望
### 注力したこと（こだわり等）
* センサを用いて周りの環境を測定した
* 好きな場所にセンサを設置する事が可能にするためにWiFiが搭載されているマイコン(esp32)を利用してサーバとの通信を確立しPCやラズパイなどが不要なマイコンとセンサのみの安価なシステム構成にした

## 開発技術
### 活用した技術
#### API・データ
* 
* 

#### フレームワーク・ライブラリ・モジュール
* Flask
 * 各ライブラリについてはdev_backendレポジトリのrequirements.txtを参照
* PostgreSQL
* NuxtJS
 * 各ライブラリについてはfrontendレポジトリのpackages.jsonを参照
* Heroku（デプロイ先として）

#### デバイス
* ESP32
* CCS811(空気品質センサ)
* GROVE-ダストセンサ

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
* 
* 


### Branch
* `frontend`, `gh-pages`: Frontend([GH Pages](https://jphacks.github.io/F_2104) にて公開中)
* `dev-es@32`: Hardware
* `dev-backend`: Backend

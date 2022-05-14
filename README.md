# auto_sushida
### 寿司打の自動入力プログラムとその使い方
# 準備
## 必要モジュール、ラッパーのインストール
### Tesseractのインストール
>#### Windowsでのインストール
>[インストーラー](https://github.com/UB-Mannheim/tesseract/wiki)
>#### debian系
>```$ sudo pat install tesseract-ocr```
>#### arch系
>```$ sudo pacman -S tesseract```
### Tkinterのインストール
>#### Windowsでのインストール
>Windows Storeから入手可能。
>#### debian系でのインストール
> ```$ sudo apt install python3-tk```
>#### arch系でのインストール
>```$ sudo pacman -S tk```
### PyAutoGUIのインストール
```$ pip install pyautogui```
### tesserocrのインストール
```$ pip install tesserocr```
### Pillowのインストール
```$ pip install pillow```
### その他にインストールが必要なモジュール、ラッパーがあると言われた場合はエラーメッセージを参考にインストールする。
## 設定
### main.pyの5行目、dir_path変数の値を任意のディレクトリのパスにする。
>#### ex. Windowsでデスクトップにスクリーンショットを保存するフォルダを作成したい場合
>```dir_path =  "C:\Users\<ユーザー名>\Desktop\"```
>#### ex. Linuxでデスクトップにスクリーンショットを保存するフォルダを作成したい場合
>```dir_path = "/home/<ユーザー名>/Desktop/"```
### sushidaフォルダのPlay.htmlをブラウザで開く。
### mouse_coordinate.pyを実行し、赤点と青点の座標をそれぞれメモする。
### main.pyの12行目、pgui.screenshotの変数を次のようにする
```sc = pgui.screenshot(region=(赤点のx座標,赤点のy座標,青点のx座標-赤点のx座標,青点のy座標-赤点のy座標))```
>#### ex. 赤点(X:315,Y:500)、青点(X:640,Y:525)の場合
>```sc = pgui.screenshot(region=(315,500,325,25))```
# 実行
```$ python main.py```
### 実行したらすぐにブラウザをクリックしてフォーカスする。
### 中断したい場合はマウスカーソルを左上に持っていく
### 中断した場合はdir_pathで指定したディレクトリにsushidaという名前のフォルダができていることがあるので削除する。

# BakeNormalForLiltoonOutline

法線データをメッシュの頂点カラーとしてベイクするBlenderアドオンです。

## 説明
カスタム法線を使用している3Dモデルは、シェーダで輪郭線がうまく表示できないという問題が発生する事があります。
lilToonシェーダでは解決策として、輪郭線の描画に使用する法線を頂点カラーから取得する機能がついています。
このアドオンを使用すると輪郭線用の法線データを頂点カラーにベイクする事ができます。

<img src="https://github.com/nukora/BakeNormalForLiltoonOutline/assets/15606184/303a16ac-7e79-4fac-837c-2d1bfbb03f00" width="512px">

## 必要条件
Blender3.5とBlender4.1で動作する事を確認しています。

## インストール
1. このリポジトリをZIPでダウンロードします。
  [Download ZIP](https://github.com/nukora/BakeNormalForLiltoonOutline/archive/refs/heads/main.zip)
2. Blenderを起動し、Edit > Preferences > Preferences > Add-ons を開きます。
3. Install...をクリックし、先ほどダウンロードしたZIPファイルを選択します。
4. Bake Normal for lilToon Outline アドオンを有効化します。

## 使用方法
1. ベイクしたいオブジェクトを複製します。
2. 複製したオブジェクトのカスタム法線を削除し、スムーズシェードを適用します。
3. 「スムーズシェードをかけたオブジェクト」→「ベイクするオブジェクト」の順番でオブジェクトを選択します。
4. View3D > Object > Bake Normal (lilToon) を実行します。
   
<img src="https://github.com/nukora/BakeNormalForLiltoonOutline/assets/15606184/2f65ae76-7af7-4405-953f-45d32d0cfe17" width="512px">
 
5. 頂点カラーに法線データがベイクされます。

<img src="https://github.com/nukora/BakeNormalForLiltoonOutline/assets/15606184/9bb7e301-e8f4-42cc-bbf1-f44e7197051a" width="512px">

6. Unityにアップロードし、lilToonのマテリアル設定から 詳細設定 > 拡張設定 > 輪郭線 > 頂点カラー をRGBA -> Normal & Width に設定してください。

<img src="https://github.com/nukora/BakeNormalForLiltoonOutline/assets/15606184/ab16e254-cb63-4e30-993c-e64d10e660fa" width="512px">

## ライセンス
このプログラムにはGPL-3.0ライセンスが適用されます。

This software is released under the GPL-3.0 License, see LICENSE.

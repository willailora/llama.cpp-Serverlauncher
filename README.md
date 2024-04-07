# llama.cpp-Serverlauncher
llama.cppのServer.exeを下記のスクショのように起動変数やモデルを選択して起動し、ページも開くようにしたコードです。別途、llama.cppの導入が必要です。
llamacppServerlauncherPyQt5.pyはGUIにPyQt5を使用したものです。
llamacppServerlauncherTkinter.pyはGUIにTkinterを使用したものです。
どちらも機能は同じなので、好きな方をご使用ください。
![スクリーンショット 2024-04-06 124526](https://github.com/willailora/llama.cpp-Serverlauncher/assets/166263028/75fb0306-b650-4918-a604-82067cce0d27)
　Server Executableは、server.exeを指定する項目です。Browse…を押すとエクスプローラーが開くので、server.exeを選択してください。
　Modelは読み込みたいモデルを指定する項目です。Browse…を押すとエクスプローラーが開くので、使用するモデルを選択してください。
　Threads (-t)は使用するCPUのコア数です、通常使用するのは物理コア数の半分らしいです。
　Portはサーバーのポート番号です。http://127.0.0.1:8080/の8080の部分を指定します。多分大丈夫ですが、他のポート番号と被らないようにする必要があります。基本デフォルトでOK。
　Max Tokens to Generate (-n)は一回の生成で作成されるトークンの最大数です。大きいほどメモリ使用量が多くなりますが、一回に出力できる文章が長くなります。画像では1024ですが、256－512で十分かと。
　Context Size (-c)はコンテクストサイズで、LLMが記憶しているトークンの最大量です。これも、大きいほどメモリ使用量が多くなります。
　GPU Layers (-ngl)はGPUに割り当てるレイヤー数で、モデルがGPUメモリのサイズ内に収まるなら、99とか200とか、大きい数値にしましょう。
Launch Serverを押すとサーバーが起動し、デフォルトブラウザーで以下の画像のようなページが開きます（サーバー起動までは表示されませんので、多少時間がかかります）。
![スクリーンショット 2024-04-06 130358](https://github.com/willailora/llama.cpp-Serverlauncher/assets/166263028/8ff2f7d3-2679-4c25-8fb7-c1596b11931c)
一回起動すると、pyがあるのと同じフォルダにllama_launcher_config.jsonというファイルが生成され、選択した項目が保存され、次回起動時にも自動的に適用されます。
windowsでしか、動作確認はしていません。　何か問題があれば、ツイッター@plionplionかディスコ@willlionまでご連絡くださいm(_ _)m
　また、自由に改変再配布をしてもらって構いませんが、ここにオリジナルがあることを明記してください。

# llama.cpp-Serverlauncher

Scroll down for English explanation.

llama.cppのServer.exeを下記のスクショのように起動変数やモデルを選択して起動し、ページも開くようにしたコードです。別途、llama.cppの導入が必要です。
llamacppServerlauncherPyQt5.pyはGUIにPyQt5を使用したものです。
llamacppServerlauncherTkinter.pyはGUIにTkinterを使用したものです。
どちらも機能は同じなので、好きな方をご使用ください。

![スクリーンショット 2024-04-06 124526](https://github.com/willailora/llama.cpp-Serverlauncher/assets/166263028/75fb0306-b650-4918-a604-82067cce0d27)

　Server Executableは、server.exeを指定する項目です。Browse…を押すとエクスプローラーが開くので、server.exeを選択してください。
 
　Modelは読み込みたいモデルを指定する項目です。Browse…を押すとエクスプローラーが開くので、使用するモデルを選択してください。
 
　Threads (-t)は使用するCPUのコア数です、通常使用するのは物理コア数の半分らしいです。
 
　Portはサーバーのポート番号です。http://127.0.0.1:8080/ の8080の部分を指定します。多分大丈夫ですが、他のポート番号と被らないようにする必要があります。基本デフォルトでOK。
 
　Max Tokens to Generate (-n)は一回の生成で作成されるトークンの最大数です。大きいほどメモリ使用量が多くなりますが、一回に出力できる文章が長くなります。画像では1024ですが、256－512で十分かと。
 
　Context Size (-c)はコンテクストサイズで、LLMが記憶しているトークンの最大量です。これも、大きいほどメモリ使用量が多くなります。
 
　GPU Layers (-ngl)はGPUに割り当てるレイヤー数で、モデルがGPUメモリのサイズ内に収まるなら、99とか200とか、大きい数値にしましょう。
 
 Launch Serverを押すとサーバーが起動し、デフォルトブラウザーで以下の画像のようなページが開きます（サーバー起動までは表示されませんので、多少時間がかかります）。

![スクリーンショット 2024-04-06 130358](https://github.com/willailora/llama.cpp-Serverlauncher/assets/166263028/8ff2f7d3-2679-4c25-8fb7-c1596b11931c)

一回起動すると、pyがあるのと同じフォルダにllama_launcher_config.jsonというファイルが生成され、選択した項目が保存され、次回起動時にも自動的に適用されます。

windowsでしか、動作確認はしていません。　何か問題があれば、ツイッター@plionplionかディスコ@willlionまでご連絡くださいm(_ _)m
また、自由に改変再配布をしてもらって構いませんが、ここにオリジナルがあることを明記してください。

The code starts the Server.exe of llama.cpp by selecting the startup variables and models as shown in the following screencast, and also opens the page. It is necessary to install llama.cpp separately.
llamacppServerlauncherPyQt5.py uses PyQt5 for the GUI.
lamacppServerlauncherTkinter.py uses Tkinter for the GUI.
Both have the same functionality, so please use whichever you prefer.

![スクリーンショット 2024-04-06 124526](https://github.com/willailora/llama.cpp-Serverlauncher/assets/166263028/75fb0306-b650-4918-a604-82067cce0d27)

Server Executable specifies server.exe; press Browse... to open the Explorer and select server.exe.

Model specifies the model you wish to load; press Browse... to open the Explorer and select the model you wish to use.

Threads (-t) is the number of CPU cores to use.

Port is the port number of the server. It is probably OK, but you need to make sure that the port number does not overlap with other port numbers. The basic default is OK.

Max Tokens to Generate (-n) is the maximum number of tokens to be created in one generation. The larger the number, the more memory is used, but the longer the text can be output at one time. In the image, the number is 1024, but 256-512 should be sufficient.

Context Size (-c) is the context size, the maximum amount of tokens stored by the LLM. Again, the larger the size, the more memory is used.

GPU Layers (-ngl) is the number of layers to allocate to the GPU. If the model fits within the GPU memory size, set it to a large number, such as 99 or 200.

Pressing Launch Server will start the server and open a page like the one in the following image in the default browser (it will not be displayed until the server is started, so it will take some time).

![スクリーンショット 2024-04-06 130358](https://github.com/willailora/llama.cpp-Serverlauncher/assets/166263028/8ff2f7d3-2679-4c25-8fb7-c1596b11931c)

Once started, a file named llama_launcher_config.json is generated in the same folder where py is located, and the selected items are saved and automatically applied the next time it is started.

We have only tested this on windows.　If you have any problems, please contact me on twitter @plionplion or disco @willlion m(_ _)m

Also, feel free to modify and redistribute the original, but please make it clear that the original is here.

---
layout: page
title: common/code (中文)
description: "跨平台且可扩展的代码编辑器。"
content_hash: 73364c9b3e4fe3b13072b7aee5723cfe606eb1c9
last_modified_at: 2024-11-28
related_topics:
  - title: Deutsch version
    url: /de/common/code.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/code.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/code.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/code.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/code.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/code.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/code.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/code.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/code.html
    icon: bi bi-globe
tldri18n_status: 2
---
# code

跨平台且可扩展的代码编辑器。
更多信息：<https://github.com/microsoft/vscode>.

- 启动 Visual Studio Code：

`code`

- 打开指定的文件或目录：

`code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录1 路径/到/文件或目录2 ...</span>

- 比较两个指定的文件：

`code --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>

- 在新窗口中打开指定的文件或目录：

`code --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录1 路径/到/文件或目录2 ...</span>

- 安装/卸载一个特定的插件：

`code --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>`-extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">插件作者.插件名</span>

- 输出已安装的插件：

`code --list-extensions`

- 输出已安装的插件及其版本：

`code --list-extensions --show-versions`

- 以超级用户（root）身份启动编辑器，同时将用户数据存储在指定目录中：

`sudo code --user-data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

---
layout: page
title: common/code (English)
description: "Cross platform and extensible code editor."
content_hash: 705c34a265b921f24223f17665ba5f6ee8c9fc80
related_topics:
  - title: Deutsch version
    url: /de/common/code.html
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
  - title: 中文 version
    url: /zh/common/code.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/code.html
    icon: bi bi-globe
---
# code

Cross platform and extensible code editor.
More information: <https://github.com/microsoft/vscode>.

- Start Visual Studio Code:

`code`

- Open specific files/directories:

`code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Compare two specific files:

`code --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Open specific files/directories in a new window:

`code --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Install/uninstall a specific extension:

`code --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>`-extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">publisher.extension</span>

- Print installed extensions:

`code --list-extensions`

- Print installed extensions with their versions:

`code --list-extensions --show-versions`

- Start the editor as a superuser (root) while storing user data in a specific directory:

`sudo code --user-data-dir {[path/to/directory</span>

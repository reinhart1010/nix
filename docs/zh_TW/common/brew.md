---
layout: page
title: common/brew (中文 (繁體, 台灣))
description: "Linux 和 macOS 的套件管理工具。"
content_hash: d11ecf13f78dbb17cd0b97788ce29fe5257df5c7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/brew.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/brew.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/brew.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/brew.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew

Linux 和 macOS 的套件管理工具。
更多資訊：<https://docs.brew.sh/Manpage>.

- 安裝最新穩定版的配方（formula）或木桶（cask），使用 `--devel` 安裝開發版：

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配方</span>

- 列出所有已安裝的配方和木桶：

`brew list`

- 更新已安裝的配方或木桶（如果沒有指定，則更新所有已安裝的配方/木桶）：

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配方</span>

- 從 Homebrew 源倉庫中獲取最新版本的 Homebrew 以及所有配方和木桶：

`brew update`

- 顯示有新版本的配方和木桶：

`brew outdated`

- 搜尋可用的配方（即套件）和木桶（即原生套件）：

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">套件名</span>

- 顯示有關配方或木桶的資訊（版本、安裝路徑、相依套件等）：

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配方</span>

- 檢查本機 Homebrew 套件是否有潛在問題：

`brew doctor`

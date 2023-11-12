---
layout: page
title: windows/clip (中文 (繁體, 台灣))
description: "將輸入的內容複製到 Windows 剪貼簿中。"
content_hash: 8c9ef96735bba04bcd6f7c7eb17bcd9a52b2508a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/clip.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/clip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/clip.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/clip.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/clip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/clip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clip

將輸入的內容複製到 Windows 剪貼簿中。
更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- 使用管道將命令輸出的內容複製到 Windows 剪貼簿中：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- 將文件內容複製到 Windows 剪貼簿中：

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>

- 將帶有換行符的內容複製到 Windows 剪貼簿中：

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字</span>` | clip`

- 將不帶換行符的內容複製到 Windows 剪貼簿中：

`echo | set /p="文字" | clip`

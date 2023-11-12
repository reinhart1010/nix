---
layout: page
title: windows/attrib (中文)
description: "显示或修改文件和目录的属性。"
content_hash: d45f46ac8814b96b19face6072c05581cc765696
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/attrib.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/attrib.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/attrib.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/attrib.html
    icon: bi bi-globe
tldri18n_status: 2
---
# attrib

显示或修改文件和目录的属性。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>.

- 显示当前目录下所有文件的属性：

`attrib`

- 显示当前目录和其子目录下所有文件的属性：

`attrib /S`

- 显示当前目录和其子目录下所有文件和目录的属性：

`attrib /S /D`

- 为一个文件增加只读属性：

`attrib +R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">document.txt</span>

- 删除一个文件的系统和隐藏属性：

`attrib -S -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">document.txt</span>

- 为一个目录增加隐藏属性：

`attrib +H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>

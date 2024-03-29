---
layout: page
title: common/file (中文)
description: "确定文件类型。"
content_hash: 80a3426227d60e383d2f84e67db90489eec8b5b6
last_modified_at: 2024-01-01
related_topics:
  - title: Deutsch version
    url: /de/common/file.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/file.html
    icon: bi bi-globe
tldri18n_status: 2
---
# file

确定文件类型。
更多信息：<https://manned.org/file>.

- 提供指定文件类型的描述，对于没有文件扩展名的文件可以正常工作：

`file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 查看压缩文件并确定其中的文件类型：

`file -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xxx.zip</span>

- 允许文件与特殊文件或设备文件一起使用：

`file -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 不要在第一个文件类型匹配时停止；继续执行直到文件结束：

`file -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 确定文件的 MIME 编码类型：

`file -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

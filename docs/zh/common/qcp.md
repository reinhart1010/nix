---
layout: page
title: common/qcp (中文)
description: "使用默认文本编辑器复制文件，以定义文件名。"
content_hash: ba9c29019df2b672c4bef4b43e152c9230512c2e
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/qcp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qcp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qcp

使用默认文本编辑器复制文件，以定义文件名。
更多信息：<https://www.nongnu.org/renameutils/>.

- 复制单个文件（在编辑器中打开左侧为源文件名，右侧为目标文件名的界面）：

`qcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源文件</span>

- 复制多个 JPEG 文件：

`qcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- 复制文件，但在编辑器中交换源文件名和目标文件名的位置：

`qcp --option swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

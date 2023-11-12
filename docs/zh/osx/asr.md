---
layout: page
title: osx/asr (中文)
description: "将磁盘映像还原（复制）到卷上。"
content_hash: afee41da4315b8f686ff64c6fcb02483cd26675a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/asr.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/asr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/asr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/asr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asr

将磁盘映像还原（复制）到卷上。
命令名称是 Apple Software Restore 的缩写。
更多信息：<https://www.unix.com/man-page/osx/8/asr/>.

- 将磁盘映像复制到目标卷：

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">映像名</span>`.dmg --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">卷路径</span>

- 在复制之前擦除目标卷：

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">映像名</span>`.dmg --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">卷路径</span>` --erase`

- 恢复后跳过验证步骤：

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">映像名</span>`.dmg --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">卷路径</span>` --noverify`

- 不使用中间磁盘映像直接复制卷中的数据：

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">卷路径</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">复制卷路径</span>

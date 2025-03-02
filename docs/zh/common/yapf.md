---
layout: page
title: common/yapf (中文)
description: "Python 风格指南检查器。"
content_hash: 46b50ef232096155be05c570dca2bf093b442eed
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yapf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yapf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/yapf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yapf

Python 风格指南检查器。
更多信息：<https://github.com/google/yapf>.

- 显示将要进行的更改的差异，但不实际更改（试运行）：

`yapf --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 就地格式化文件，并显示更改的差异：

`yapf --diff --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 递归格式化目录中的所有 Python 文件，并发执行：

`yapf --recursive --in-place --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pep8</span>` --parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

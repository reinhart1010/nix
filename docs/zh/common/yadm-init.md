---
layout: page
title: common/yadm-init (中文)
description: "初始化一个新的空的代码仓库用于跟踪点文件。"
content_hash: 53b78cd5fb10d23b9535c1e22226a357c72c472c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yadm-init.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yadm-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yadm-init

初始化一个新的空的代码仓库用于跟踪点文件。
该代码仓库存储在 `$HOME/.local/share/yadm/repo.git` 中。
更多信息：<https://yadm.io/docs/getting_started>.

- 执行：

`yadm init`

- 覆盖工作树：

`yadm init -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/工作树文件夹</span>

- 覆盖已存在的代码仓库：

`yadm init -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/本地代码仓库</span>

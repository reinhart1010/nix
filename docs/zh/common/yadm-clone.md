---
layout: page
title: common/yadm-clone (中文)
description: "功能就像 `git clone`。此外，你还可以传递额外的标志来配置你的仓库。"
content_hash: 0418a971780e9b4693fcd9e629fd32922fc8c1a5
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yadm-clone.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yadm-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yadm-clone

功能就像 `git clone`。此外，你还可以传递额外的标志来配置你的仓库。
如果仓库中有一个引导文件，将提示你执行它。
请参阅：`git clone`。
更多信息：<https://yadm.io/docs/common_commands>.

- 克隆一个已有的仓库：

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程_仓库_位置</span>

- 克隆一个已有的仓库，然后执行引导文件：

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程_仓库_位置</span>` --bootstrap`

- 克隆一个已有的仓库，并在克隆后不执行引导文件：

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程_仓库_位置</span>` --no-bootstrap`

- 更改 `yadm` 在克隆时使用的工作树：

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程_仓库_位置</span>` --w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">工作树_文件</span>

- 更改 `yadm` 用于获取文件的分支：

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程_仓库_位置</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分支</span>

- 覆盖一个已有仓库的本地分支：

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程_仓库_位置</span>` -f`

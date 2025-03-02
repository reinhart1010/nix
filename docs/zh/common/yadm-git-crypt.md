---
layout: page
title: common/yadm-git-crypt (中文)
description: "Git Crypt 能够实现 Git 仓库中文件的透明加密和解密。"
content_hash: aff3dea1640e63289fb5def028581d9fcc303da0
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yadm-git-crypt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yadm-git-crypt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yadm git-crypt

Git Crypt 能够实现 Git 仓库中文件的透明加密和解密。
请参阅：`git-crypt`。
更多信息：<https://github.com/AGWA/git-crypt>.

- 初始化仓库以使用 Git Crypt：

`yadm git-crypt init`

- 使用 GPG 共享仓库：

`yadm git-crypt add-gpg-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户_id</span>

- 克隆包含加密文件的仓库后，解锁它们：

`yadm git-crypt unlock`

- 导出对称密钥：

`yadm git-crypt export-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/密钥文件</span>

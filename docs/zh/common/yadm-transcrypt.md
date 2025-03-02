---
layout: page
title: common/yadm-transcrypt (中文)
description: "如果已安装 `transcrypt`，此命令允许直接向 `transcrypt` 传递选项。"
content_hash: 9f96f09988b0c61e68542dfbd86768fc0a54713c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yadm-transcrypt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yadm-transcrypt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yadm-transcrypt

如果已安装 `transcrypt`，此命令允许直接向 `transcrypt` 传递选项。
环境配置为使用 yadm 仓库。
Transcrypt 使 Git 仓库中的文件能够透明地加密和解密。
更多信息：<https://github.com/elasticdog/transcrypt>.

- 设置用于加密的对称加密算法：

`yadm transcrypt --cipher=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">加密算法</span>

- 提供用来派生密钥的密码：

`yadm transcrypt --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 假设所有回答为“是”并接受未指定选项的默认值：

`yadm transcrypt --yes`

- 显示当前仓库的加密算法和密码：

`yadm transcrypt --display`

- 使用新的凭证重新加密所有已加密的文件：

`yadm transcrypt --rekey`

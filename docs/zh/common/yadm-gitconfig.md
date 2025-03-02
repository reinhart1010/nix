---
layout: page
title: common/yadm-gitconfig (中文)
description: "向 `git config` 传递选项。更改由 `yadm` 管理的仓库的 `.gitconfig`。"
content_hash: eb8588511b72efe44beb9e7c66963b3f528c9d24
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yadm-gitconfig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yadm-gitconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yadm-gitconfig

向 `git config` 传递选项。更改由 `yadm` 管理的仓库的 `.gitconfig`。
请参阅：`git config`。
更多信息：<https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>.

- 更新或设置一个 Git 配置值：

`yadm gitconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键.内键</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- 从 `yadm` 的 Git 配置中获取一个值：

`yadm gitconfig --get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键</span>

- 在 `yadm` 的 Git 配置中取消设置一个值：

`yadm gitconfig --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键</span>

- 列出 `yadm` 的 Git 配置中的所有值：

`yadm gitconfig --list`

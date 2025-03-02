---
layout: page
title: common/yadm-config (中文)
description: "传递选项给 `yadm` 的配置文件。更改由 `yadm` 管理的仓库的 `.config`。"
content_hash: 82a233c7df52e65850c8d9ccb8e8f2a4c0accb9a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yadm-config.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yadm-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yadm-config

传递选项给 `yadm` 的配置文件。更改由 `yadm` 管理的仓库的 `.config`。
更多信息：<https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#configuration>.

- 设置或更新 `yadm` 的 Git 配置：

`yadm config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键.内键</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- 从 `yadm` 的 Git 配置中获取一个值：

`yadm config --get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键</span>

- 在 `yadm` 的 Git 配置中取消设置一个值：

`yadm config --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键</span>

- 列出 `yadm` 的 Git 配置中的所有值：

`yadm config --list`

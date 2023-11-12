---
layout: page
title: common/autojump (中文)
description: "快速跳转，访问次数最多的文件夹优先。"
content_hash: 1ca7a674d144cb46d93be0f007ba2f6b668edd66
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/autojump.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autojump.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/autojump.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autojump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autojump

快速跳转，访问次数最多的文件夹优先。
使用 `j`、`jc`、和 `jo` 作为别名。
更多信息：<https://github.com/wting/autojump>.

- 跳转到包含指定通配符的目录：

`j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">通配符表达式</span>

- 跳转到包含指定通配符的目录的下一级：

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">通配符表达式</span>

- 使用系统文件管理器，打开指定的目录：

`jo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">通配符表达式</span>

- 从 autojump 数据库中删除不存在的目录：

`j --purge`

- 展示 autojump 数据库数据：

`j -s`

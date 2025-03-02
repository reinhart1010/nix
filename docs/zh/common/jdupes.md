---
layout: page
title: common/jdupes (中文)
description: "一个强大的重复文件查找器，并且是 fdupes 的一个增强分支。"
content_hash: 804abe4b4ca65f88c1bf0825d5f98dba7d8a6b4d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jdupes.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jdupes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jdupes

一个强大的重复文件查找器，并且是 fdupes 的一个增强分支。
更多信息：<https://codeberg.org/jbruchon/jdupes>.

- 搜索单个目录：

`jdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 搜索多个目录：

`jdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录2</span>

- 递归地搜索所有目录：

`jdupes --recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 递归地搜索目录，并让用户选择要保留的文件：

`jdupes --delete --recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 搜索多个目录并跟随目录2下的子目录，而不是目录1：

`jdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录1</span>` --recurse: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录2</span>

- 搜索多个目录并在结果中保持目录顺序：

`jdupes -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录3</span>

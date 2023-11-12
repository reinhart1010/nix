---
layout: page
title: common/mv (中文)
description: "移动或重命名文件或目录。"
content_hash: d7284702947317ba9a3783428bcd501df761dc54
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/mv.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mv.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/mv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mv.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/mv.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mv

移动或重命名文件或目录。
更多信息：<https://www.gnu.org/software/coreutils/mv>.

- 移动文件到任意位置：

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 移动文件到其他目录，并保持文件名不变：

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源1 路径/到/来源2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>

- 覆盖现有文件前无需确认：

`mv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 无论是否有文件权限，覆盖现有文件前均需要确认：

`mv -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 不要覆盖现有的目标文件：

`mv -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 详细模式，移动后打印文件名：

`mv -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

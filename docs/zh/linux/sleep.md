---
layout: page
title: linux/sleep (中文)
description: "延迟指定的一段时间。"
content_hash: a1a6a0ab9b7211f1d74e646ff9d0fb4ec145bfdb
last_modified_at: 2024-06-20
related_topics:
  - title: English version
    url: /en/linux/sleep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/sleep.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/sleep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sleep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sleep

延迟指定的一段时间。
更多信息：<https://www.gnu.org/software/coreutils/sleep>.

- 按秒数延迟：

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>

- 延迟 [m]分钟（其他元素 [d]天，[h]小时，[s]秒，[inf]无穷 也可以使用）：

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>`m`

- 延迟 1 [d]天 3 [h]小时：

`sleep 1d 3h`

- 在 20 [m]分钟 延迟后执行指定命令：

`sleep 20m && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

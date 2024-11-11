---
layout: page
title: linux/sleep (한국어)
description: "지정된 시간만큼 지연합니다."
content_hash: 9feb6dec8b8bd6ae067c01561ff592db45463ad4
last_modified_at: 2024-11-11
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
  - title: 中文 version
    url: /zh/linux/sleep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sleep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sleep

지정된 시간만큼 지연합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/sleep>.

- 초 단위로 지연:

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>

- [m]분 단위로 지연 (다른 단위로는 [d]일, [h]시간, [s]초, [inf]무한대 사용 가능):

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분</span>`m`

- 1[d]일 3[h]시간 동안 지연:

`sleep 1d 3h`

- 20[m]분 지연 후 특정 명령 실행:

`sleep 20m && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

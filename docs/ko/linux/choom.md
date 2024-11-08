---
layout: page
title: linux/choom (한국어)
description: "OOM(Out-Of-Memory) 킬러 점수를 표시하고 변경."
content_hash: 6a51a5496f1058f7c1765271c680a00a8cb8c3e6
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/choom.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/choom.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/choom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choom

OOM(Out-Of-Memory) 킬러 점수를 표시하고 변경.
더 많은 정보: <https://manned.org/choom>.

- 특정 프로세스 ID의 OOM-킬러 점수 표시:

`choom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>

- 특정 프로세스의 OOM-킬러 점수 변경:

`choom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1000..+1000</span>

- 특정 OOM-킬러 점수로 명령 실행:

`choom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1000..+1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

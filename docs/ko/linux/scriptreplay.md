---
layout: page
title: linux/scriptreplay (한국어)
description: "`script` 명령어로 생성된 typescript를 `stdout`으로 재생."
content_hash: fe336b3ff8e3070c39c9df0765b3730bd0de3d4c
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/scriptreplay.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/scriptreplay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># scriptreplay

`script` 명령어로 생성된 typescript를 `stdout`으로 재생.
더 많은 정보: <https://manned.org/scriptreplay>.

- 기록된 속도로 typescript를 재생:

`scriptreplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타이밍_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/typescript</span>

- 원래 속도의 두 배로 typescript를 재생:

`scriptreplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타이밍_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/typescript</span>` 2`

- 원래 속도의 절반으로 typescript를 재생:

`scriptreplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타이밍_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/typescript</span>` 0.5`

---
layout: page
title: linux/compose (한국어)
description: "`run-mailcap`의 동작인 compose에 대한 별칭."
content_hash: a59800ee01240addd2421981365ed541f50899cb
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/compose.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/compose.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># compose

`run-mailcap`의 동작인 compose에 대한 별칭.
원래 `run-mailcap`은 MIME 타입/파일을 처리하는 데 사용됩니다.
더 많은 정보: <https://manned.org/compose>.

- 기본 mailcap 편집 도구에서 기존 파일이나 새 파일을 작성하는 데 compose 동작 사용:

`compose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- `run-mailcap` 사용:

`run-mailcap --action=compose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

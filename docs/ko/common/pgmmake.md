---
layout: page
title: common/pgmmake (한국어)
description: "균일한 회색 레벨로 PGM 이미지를 생성."
content_hash: 3ee73964fc1a8bef41acd476b83450d11260e42e
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pgmmake.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pgmmake.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pgmmake

균일한 회색 레벨로 PGM 이미지를 생성.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pgmmake.html>.

- 균일한 회색 레벨(0과 1 사이의 숫자로 지정)과 지정된 크기로 PGM 이미지 생성:

`pgmmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">회색_레벨</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pgm</span>

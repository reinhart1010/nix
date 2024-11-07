---
layout: page
title: common/pwgen (한국어)
description: "발음 가능한 비밀번호 생성."
content_hash: c7b0e2bdb6450b3de8a8a6ea3b1ebebcbc1d5f6a
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pwgen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pwgen.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pwgen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pwgen

발음 가능한 비밀번호 생성.
더 많은 정보: <https://github.com/tytso/pwgen>.

- 랜덤 비밀번호 생성 (특수문자 포함):

`pwgen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">길이</span>

- 보안성이 높고 기억하기 어려운 비밀번호 생성:

`pwgen -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">길이</span>

- 최소 하나의 대문자가 포함된 비밀번호 생성:

`pwgen -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">길이</span>

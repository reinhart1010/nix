---
layout: page
title: common/ya (한국어)
description: "Yazi 패키지 및 플러그인 관리."
content_hash: 0478125d027a56590e771253bd71acbdee348c65
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/ya.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ya.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ya.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ya

Yazi 패키지 및 플러그인 관리.
더 많은 정보: <https://github.com/sxyazi/yazi>.

- 패키지 추가:

`ya pack -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 모든 패키지 업그레이드:

`ya pack -u`

- 모든 원격 인스턴스로부터 메시지 구독:

`ya sub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종류</span>

- 현재 인스턴스에 문자열 본문의 메시지 발행:

`ya pub --str `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열_메시지</span>

- 현재 인스턴스에 JSON 본문의 메시지 발행:

`ya pub --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json_메시지</span>

- 지정된 인스턴스에 문자열 본문의 메시지 발행:

`ya pub-to --str `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수신자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종류</span>

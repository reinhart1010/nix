---
layout: page
title: common/peludna-prognoza (한국어)
description: "Pliva의 알레르기 데이터 API를 사용하여 터미널에서 크로아티아 도시의 꽃가루 측정 데이터를 가져옵니다."
content_hash: c680a8867fd5680063ba13a8581f559424f5443d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/peludna-prognoza.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/peludna-prognoza.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># peludna-prognoza

Pliva의 알레르기 데이터 API를 사용하여 터미널에서 크로아티아 도시의 꽃가루 측정 데이터를 가져옵니다.
더 많은 정보: <https://github.com/vladimyr/peludna-prognoza>.

- 도시를 대화형으로 검색하고 데이터를 가져오기:

`peludna-prognoza`

- 특정 도시의 데이터 가져오기:

`peludna-prognoza "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도시</span>`"`

- 기계 판독 가능한 형식으로 데이터 표시:

`peludna-prognoza "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도시</span>`" --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|xml</span>

- 기본 웹 브라우저에서 <https://plivazdravlje.hr>의 특정 도시 꽃가루 측정 페이지 표시:

`peludna-prognoza "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도시</span>`" --web`

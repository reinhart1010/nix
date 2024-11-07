---
layout: page
title: common/recsel (한국어)
description: "recfile에서 레코드를 출력: 사람이 편집할 수 있는 일반 텍스트 데이터베이스."
content_hash: 81fb98cb4e7701a1a8b2159d408fdd481a40166f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/recsel.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/recsel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># recsel

recfile에서 레코드를 출력: 사람이 편집할 수 있는 일반 텍스트 데이터베이스.
더 많은 정보: <https://www.gnu.org/software/recutils/manual/recutils.html>.

- 이름 및 버전 필드 추출:

`recsel -p name,version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.rec</span>

- "~"를 사용하여 주어진 정규 표현식과 문자열 매칭:

`recsel -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름</span>` ~ '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.rec</span>`"`

- 이름과 버전을 매칭하는 조건 사용:

`recsel -e "name ~ '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`' && version ~ '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`'" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.rec</span>

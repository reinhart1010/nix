---
layout: page
title: common/texcount (한국어)
description: "TeX 문서에서 매크로를 제외하고 단어 수를 세기."
content_hash: 9b90868cdb503838052cc2fe892556ef546de9b6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/texcount.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/texcount.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># texcount

TeX 문서에서 매크로를 제외하고 단어 수를 세기.
참고: TeX 문서가 `\include` 또는 `\input`을 사용하고 포함된 파일을 세려면, `texcount`를 루트 TeX 파일이 있는 디렉토리에서 실행해야 합니다.
더 많은 정보: <https://app.uio.no/ifi/texcount/howto.html>.

- TeX 파일의 단어 수 세기:

`texcount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tex</span>

- `\input` 또는 `\include`로 구성된 문서 및 하위 문서의 단어 수 세기:

`texcount -merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.tex</span>

- 문서 및 하위 문서의 단어 수를 세고 각 파일을 별도로 나열 (총 단어 수 포함):

`texcount -inc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.tex</span>

- 문서 및 하위 문서의 단어 수를 세고 각 챕터별로 세부 카운트 제공 (하위 섹션 대신):

`texcount -merge -sub=chapter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.tex</span>

- 자세한 출력과 함께 단어 수 세기:

`texcount -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tex</span>

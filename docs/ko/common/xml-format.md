---
layout: page
title: common/xml-format (한국어)
description: "XML 문서를 포맷합니다."
content_hash: af67150fca40852b44c7bfbbbd05103fb22d4cb5
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xml-format.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xml-format.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xml format

XML 문서를 포맷합니다.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서를 탭으로 들여쓰기하여 포맷:

`xml format --indent-tab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>

- HTML 문서를 4칸의 공백으로 들여쓰기하여 포맷:

`xml format --html --indent-spaces `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.html|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.html</span>

- 잘못된 XML 문서에서 구문 분석이 가능한 부분을 복구하고 들여쓰지 않음:

`xml format --recover --noindent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/잘못된.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/복구된.xml</span>

- `stdin`에서 XML 문서를 포맷하고 `DOCTYPE` 선언을 제거:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml</span>` | xml format --dropdtd > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>

- XML 선언을 생략하여 XML 문서를 포맷:

`xml format --omit-decl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>

- 도움말 표시:

`xml format --help`

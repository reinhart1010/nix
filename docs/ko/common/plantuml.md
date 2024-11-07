---
layout: page
title: common/plantuml (한국어)
description: "일반 텍스트 언어로 UML 다이어그램을 작성하고 다양한 형식으로 렌더링."
content_hash: 2b9a27d4fd11e3823ae8958f76126e6c2bacf231
last_modified_at: 2024-11-07
related_topics:
  - title: Deutsch version
    url: /de/common/plantuml.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/plantuml.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/plantuml.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/plantuml.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># plantuml

일반 텍스트 언어로 UML 다이어그램을 작성하고 다양한 형식으로 렌더링.
더 많은 정보: <https://plantuml.com/en/command-line>.

- 다이어그램을 기본 형식(PNG)으로 렌더링:

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다이어그램1.puml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다이어그램2.puml</span>

- 주어진 형식(예: `png`, `pdf`, `svg`, `txt`)으로 다이어그램 렌더링:

`plantuml -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다이어그램.puml</span>

- 디렉토리의 모든 다이어그램 렌더링:

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/다이어그램</span>

- 출력 디렉토리에 다이어그램 렌더링:

`plantuml -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다이어그램.puml</span>

- 다이어그램의 소스 코드를 저장하지 않고 렌더링 (참고: `-nometadata` 옵션이 지정되지 않으면 기본적으로 저장됨):

`plantuml -nometadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다이어그램.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다이어그램.puml</span>

- `plantuml` 다이어그램의 메타데이터에서 소스 코드 가져오기:

`plantuml -metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다이어그램.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다이어그램.puml</span>

- 구성 파일을 사용하여 다이어그램 렌더링:

`plantuml -config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성.cfg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다이어그램.puml</span>

- 도움말 표시:

`plantuml -help`

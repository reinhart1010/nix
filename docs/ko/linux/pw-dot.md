---
layout: page
title: linux/pw-dot (한국어)
description: "PipeWire 그래프의 `.dot` 파일 생성."
content_hash: 5ce1bec2793d34edf34a7f504543f843dd324c3e
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pw-dot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-dot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-dot

PipeWire 그래프의 `.dot` 파일 생성.
같이 보기: `dot`, 그래프 렌더링을 위해.
더 많은 정보: <https://docs.pipewire.org/page_man_pw-dot_1.html>.

- `pw.dot` 파일로 그래프 생성:

`pw-dot`

- `pw-dump` JSON 파일에서 객체 읽기:

`pw-dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-j|--json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>

- [o]utput 파일 지정, 모든 객체 유형 표시:

`pw-dot --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.dot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--all</span>

- 모든 객체 속성을 표시하며 `.dot` 그래프를 `stdout`에 출력:

`pw-dot --output - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--detail</span>

- [r]emote 인스턴스에서 그래프를 생성, 연결된 객체만 표시:

`pw-dot --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--smart</span>

- 기본적으로 dot의 위에서 아래로가 아닌 왼쪽에서 오른쪽으로 그래프 정렬:

`pw-dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--lr</span>

- 엣지를 90도 각도로 사용하여 그래프 정렬:

`pw-dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-9|--90</span>

- 도움말 표시:

`pw-dot --help`

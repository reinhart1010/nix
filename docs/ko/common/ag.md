---
layout: page
title: common/ag (한국어)
description: "The Silver Searcher."
content_hash: e0b19423a0e1f2401249f80d15c37133e5d1d182
last_modified_at: 2023-12-03
related_topics:
  - title: English version
    url: /en/common/ag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ag.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ag.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ag.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ag.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ag.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ag

The Silver Searcher.
`ack` 과 비슷하지만, 더 빠르다.
더 많은 정보: <https://github.com/ggreer/the_silver_searcher>.

- "foo"를 포함하고 있는 파일들을 찾고, 내용에서 일치하는 행을 출력:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 특정 디렉토리에서 "foo"를 포함하고 있는 파일 찾기:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/디렉토리명</span>

- "foo"를 포함하고 있는 파일을 찾되, 파일 이름만 나열:

`ag -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- "FOO"를 포함하고 있는 파일들을 사례별로 찾고, 전체 라인이 아닌 일치 라인만 인쇄:

`ag -i -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FOO</span>

- "bar" 제목과 일치하는 파일에서 "foo" 찾기:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- 내용이 정규식과 일치하는 파일 찾기:

`ag '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba(r|z)$</span>`'`

- 이름이 "foo"와 일치하는 파일 찾기:

`ag -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

---
layout: page
title: common/jq (한국어)
description: "도메인 특화 언어(DSL)를 사용하는 JSON 처리기."
content_hash: 59807f3d0362fa29023911102a1bf7a6eef7eec0
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/jq.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/jq.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/jq.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/jq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jq

도메인 특화 언어(DSL)를 사용하는 JSON 처리기.
더 많은 정보: <https://jqlang.github.io/jq/manual/>.

- 특정 표현식을 실행하여 JSON을 색상 및 포맷된 출력으로 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일.json</span>` | jq '.'`

- `jq` 바이너리를 사용하여 특정 표현식을 실행하고 JSON을 색상 및 포맷된 출력으로 표시:

`jq '.' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/파일.json</span>

- 특정 스크립트를 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일.json</span>` | jq --from-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.jq</span>

- 특정 인수 전달:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일.json</span>` | jq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--arg "name1" "value1" --arg "name2" "value2" ...</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">. + $ARGS.named</span>`'`

- 특정 키 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.key1, .key2, ...</span>`'`

- 특정 배열 항목 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.[index1], .[index2], ...</span>`'`

- 모든 배열/객체 값 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일.json</span>` | jq '.[]'`

- 특정 키 추가/제거:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일.json</span>` | jq '. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"key1": "value1", "key2": "value2", ...}</span>`'`

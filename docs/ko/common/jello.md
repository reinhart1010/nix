---
layout: page
title: common/jello (한국어)
description: "Python 구문을 사용하는 명령줄 JSON 처리기."
content_hash: bb9504452eb8ed3b4dfbf8f3d91d88de30c76465
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jello.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jello.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jello

Python 구문을 사용하는 명령줄 JSON 처리기.
더 많은 정보: <https://github.com/kellyjonbrazil/jello>.

- `stdin`에서 `stdout`으로 JSON 또는 JSON-Lines 데이터를 보기 좋게 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jello`

- `stdin`에서 `stdout`으로 JSON 또는 JSON Lines 데이터의 스키마 출력 (grep에 유용):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jello -s`

- `stdin`에서 `stdout`으로 JSON 또는 JSON-Lines 데이터의 배열의 모든 요소 (또는 객체의 모든 값) 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jello -l`

- `stdin`에서 `stdout`으로 JSON 또는 JSON-Lines 데이터의 첫 번째 요소 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jello _[0]`

- `stdin`에서 `stdout`으로 JSON 또는 JSON-Lines 데이터의 각 요소에서 주어진 키의 값 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jello '[i.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` for i in _]'`

- (입력 JSON에 `key_name1` 및 `key_name2` 키가 있다고 가정할 때) 여러 키의 값을 새 JSON 객체로 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jello '{"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키1</span>`": _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name1</span>`, "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>`": _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name2}</span>`'`

- 문자열로 주어진 키의 값 출력 (JSON 출력 비활성화):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jello -r '"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`: " + _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>`'`

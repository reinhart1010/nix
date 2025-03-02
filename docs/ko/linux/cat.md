---
layout: page
title: linux/cat (한국어)
description: "[f]파일을 출력하고 연결."
content_hash: 3fe51af841fe581c879fddac2982b70cbb08d985
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/cat.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/cat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cat.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

[f]파일을 출력하고 연결.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- [f]파일의 내용을 `stdout`에 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 여러 [f]파일을 연결하여 출력 [f]파일로 저장:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 여러 [f]파일을 출력 [f]파일에 추가:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- `stdin`을 [f]파일로 작성:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 출력 줄에 [n]번호 추가:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 비인쇄 및 공백 문자를 표시 (비ASCII의 경우 `M-` 접두사 사용):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

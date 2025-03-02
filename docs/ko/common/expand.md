---
layout: page
title: common/expand (한국어)
description: "탭을 공백으로 변환."
content_hash: 6766b2972aaf7352b2e179c5dbafd0da66d0f30a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/expand.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/expand.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/expand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# expand

탭을 공백으로 변환.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/expand-invocation.html>.

- 각 파일의 탭을 공백으로 변환하여 `stdout`에 작성:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 읽어 탭을 공백으로 변환:

`expand`

- 공백이 아닌 경우 탭을 변환하지 않음:

`expand -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 탭을 8자가 아닌 특정 수의 문자 간격으로 위치:

`expand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 명시적인 탭 위치를 쉼표로 구분한 목록을 사용:

`expand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,4,6</span>

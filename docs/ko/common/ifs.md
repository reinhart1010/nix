---
layout: page
title: common/ifs (한국어)
description: "IFS (Internal Field Separator)는 Unix쉘에서 단어 분할에 사용되는 구분 기호를 정의하는 특수 환경 변수."
content_hash: bcc2950ba2a6a91ed8e17b8721ece942f976baf1
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ifs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# IFS

IFS (Internal Field Separator)는 Unix쉘에서 단어 분할에 사용되는 구분 기호를 정의하는 특수 환경 변수.
IFS의 기본값은 공백, 탭 및 줄바꿈. 세 문자는 구분 기호 역할을 함.
더 많은 정보: <https://www.gnu.org/software/bash/manual/html_node/Word-Splitting.html>.

- 현재 IFS 값 보기:

`echo "$IFS"`

- IFS 값 변경:

`IFS="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>`"`

- IFS를 기본값으로 재설정:

`IFS=$' \t\n'`

- 서브셸에서 IFS 값을 일시적으로 변경:

`(IFS="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>`"; echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">one:two:three</span>`")`

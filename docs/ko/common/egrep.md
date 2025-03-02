---
layout: page
title: common/egrep (한국어)
description: "확장 정규식을 사용하여 파일에서 패턴을 찾음 (`?`, `+`, `{}`, `()`, 및 `|` 지원)."
content_hash: 717fc00eb8f15702aaddc044d781a0f27910b78e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/egrep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/egrep.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/egrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/egrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# egrep

확장 정규식을 사용하여 파일에서 패턴을 찾음 (`?`, `+`, `{}`, `()`, 및 `|` 지원).
더 많은 정보: <https://manned.org/egrep>.

- 파일 내에서 패턴 검색:

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 여러 파일 내에서 패턴 검색:

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 패턴에 대한 `stdin` 검색:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | egrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>

- 각 일치 항목의 파일 이름과 줄 번호를 출력:

`egrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 바이너리 파일을 무시하고 디렉터리에서 반복적으로 모든 파일의 패턴을 검색:

`egrep --recursive --binary-files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">without-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 패턴과 일치하지 않는 라인 검색:

`egrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

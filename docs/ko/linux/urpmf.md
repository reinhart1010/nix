---
layout: page
title: linux/urpmf (한국어)
description: "파일을 패키지에서 찾고 Mageia에서 해당 정보를 조회."
content_hash: f59450fc597ba015f8063508b88bbccea2d0708c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/urpmf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# urpmf

파일을 패키지에서 찾고 Mageia에서 해당 정보를 조회.
같이 보기: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmi.update`, `urpmq`.
더 많은 정보: <https://wiki.mageia.org/en/URPMI#urpmi.removemedia>.

- 파일을 포함하는 패키지 검색:

`urpmf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 요약에 특정 키워드 [a]그리고 다른 키워드를 모두 포함하는 패키지 검색:

`urpmf --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드1</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드2</span>

- 설명에 특정 키워드 [o]또는 다른 키워드를 포함하는 패키지 검색:

`urpmf --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드1</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드2</span>

- 이름에 특정 키워드를 대소문자 구분 없이 포함하지 않는 패키지를 ":" 대신 "|"를 [F]ield 구분자로 사용하여 검색:

`urpmf --description ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>` -F'|'`

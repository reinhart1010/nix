---
layout: page
title: common/diffstat (한국어)
description: "`diff` 명령어의 결과로부터 히스토그램을 생성한다."
content_hash: 3bf21d15e9b60acb1cd6efc02a9d9234c612deac
related_topics:
  - title: English version
    url: /en/common/diffstat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/diffstat.html
    icon: bi bi-globe
---
# diffstat

`diff` 명령어의 결과로부터 히스토그램을 생성한다.
더 많은 정보: <https://manned.org/diffstat>.

- 히스토그램에서 변경점들 표시:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명2</span>` | diffstat`

- 삽입, 삭제 및 수정된 변경점들을 테이블로 표시:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명2</span>` | diffstat -t`

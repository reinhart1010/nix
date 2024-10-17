---
layout: page
title: common/f3fix (한국어)
description: "가짜 플래시 드라이브의 파티션 테이블 편집."
content_hash: 69b70884503f6388d324b03630e0107c158a4518
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/f3fix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# f3fix

가짜 플래시 드라이브의 파티션 테이블 편집.
참고: `f3probe`, `f3write`, `f3read`.
더 많은 정보: <https://oss.digirati.com.br/f3/>.

- 실제 용량과 일치하는 단일 파티션으로 가짜 플래시 드라이브를 채우기:

`sudo f3fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/장치_이름</span>

- 파티션을 부팅 가능한 것으로 표시:

`sudo f3fix --boot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/장치_이름</span>

- 파일 시스템을 지정:

`sudo f3fix --fs-type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템_타입</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/장치_이름</span>

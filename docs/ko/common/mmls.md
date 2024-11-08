---
layout: page
title: common/mmls (한국어)
description: "볼륨 시스템의 파티션 레이아웃을 표시."
content_hash: ba1ba41cc830e2743f36c7ab15c45ee18dcc58c8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mmls.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mmls

볼륨 시스템의 파티션 레이아웃을 표시.
더 많은 정보: <https://wiki.sleuthkit.org/index.php?title=Mmls>.

- 이미지 파일에 저장된 파티션 테이블 표시:

`mmls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일</span>

- 파티션 크기를 포함한 추가 열과 함께 파티션 테이블 표시:

`mmls -B -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일</span>

- 분할된 EWF 이미지에서 파티션 테이블 표시:

`mmls -i ewf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.e01</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.e02</span>

- 중첩된 파티션 테이블 표시:

`mmls -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">중첩_테이블_유형</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오프셋</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일</span>

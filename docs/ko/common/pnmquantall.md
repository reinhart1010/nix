---
layout: page
title: common/pnmquantall (한국어)
description: "여러 파일에 대해 공통 색상표를 사용하여 `pnmquant`를 실행."
content_hash: 7a56a5acb984f97dc468c5576b3c70fcd824c17b
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmquantall.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pnmquantall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmquantall

여러 파일에 대해 공통 색상표를 사용하여 `pnmquant`를 실행.
같이 보기: `pnmquant`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmquantall.html>.

- 지정된 매개 변수로 여러 파일에 `pnmquant`를 실행하여 원본 파일에 덮어쓰기:

`pnmquantall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input1.pnm 경로/대상/input2.pnm ...</span>

- 양자화된 이미지를 입력 파일과 동일한 이름으로 저장하되, 지정된 확장을 추가하여 저장:

`pnmquantall -ext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input1.pnm 경로/대상/input2.pnm ...</span>

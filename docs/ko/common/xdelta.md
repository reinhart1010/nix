---
layout: page
title: common/xdelta (한국어)
description: "델타 인코딩 유틸리티."
content_hash: ee50b3e32fb01b4b0b27f3020dd79bdcc2c5d544
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xdelta.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xdelta

델타 인코딩 유틸리티.
주로 바이너리 파일에 패치를 적용하는 데 사용됩니다.
더 많은 정보: <https://github.com/jmacd/xdelta>.

- 패치 적용:

`xdelta -d -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/델타_파일.xdelta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 패치 생성:

`xdelta -e -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이전_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xdelta</span>

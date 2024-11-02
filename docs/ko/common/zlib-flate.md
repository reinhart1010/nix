---
layout: page
title: common/zlib-flate (한국어)
description: "원시 zlib 압축 및 압축 해제 프로그램."
content_hash: 53b905fa32d5a0fb59809b607326a29b304f6e27
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zlib-flate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zlib-flate

원시 zlib 압축 및 압축 해제 프로그램.
`qpdf`의 일부.
더 많은 정보: <https://manned.org/zlib-flate>.

- 파일 압축:

`zlib-flate -compress < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된.zlib</span>

- 파일 압축 해제:

`zlib-flate -uncompress < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된.zlib</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 지정된 압축 수준으로 파일 압축. 0=가장 빠름 (최악), 9=가장 느림 (최고):

`zlib-flate -compress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축_수준</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된.zlib</span>

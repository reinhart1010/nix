---
layout: page
title: common/cjxl (한국어)
description: "이미지를 JPEG XL로 압축."
content_hash: 86337e1e28a2f864792b89905331b3eea1703e5f
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cjxl.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cjxl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cjxl

이미지를 JPEG XL로 압축.
허용되는 입력 확장자는 PNG, APNG, GIF, JPEG, EXR, PPM, PFM, PAM, PGX 및 JXL입니다.
더 많은 정보: <https://github.com/libjxl/libjxl>.

- 이미지를 JPEG XL로 변환:

`cjxl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.jxl</span>

- 품질에 손실이 없게하고 결과 이미지의 압축을 최대화함:

`cjxl --distance 0 --effort 9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.jxl</span>

- 매우 상세한 도움말 페이지를 표시:

`cjxl --help --verbose --verbose --verbose --verbose`

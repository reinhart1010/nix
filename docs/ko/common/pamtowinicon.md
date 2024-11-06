---
layout: page
title: common/pamtowinicon (한국어)
description: "PAM 이미지를 Windows ICO 파일로 변환."
content_hash: 7779de6ca6d09e8413ef0db5b2cb73fc9958df87
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamtowinicon.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamtowinicon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamtowinicon

PAM 이미지를 Windows ICO 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamtowinicon.html>.

- PAM 이미지 파일을 ICO 파일로 변환:

`pamtowinicon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ico</span>

- 해상도가 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">t</span>`보다 작은 이미지는 BMP 형식으로, 그 외 이미지는 PNG 형식으로 인코딩:

`pamtowinicon -pngthreshold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ico</span>

- 불투명하지 않은 영역 외의 모든 픽셀을 검정색으로 설정:

`pamtowinicon -truetransparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ico</span>

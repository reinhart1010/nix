---
layout: page
title: common/ppmtoarbtxt (한국어)
description: "PPM 이미지를 템플릿에 따라 임의의 텍스트 형식으로 변환."
content_hash: 49e2282fefb5168f49bfc518c5353db7255568fa
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtoarbtxt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtoarbtxt

PPM 이미지를 템플릿에 따라 임의의 텍스트 형식으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoarbtxt.html>.

- 주어진 템플릿에 따라 PPM 이미지를 텍스트로 변환:

`ppmtoarbtxt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/템플릿</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.txt</span>

- 주어진 템플릿에 따라 PPM 이미지를 텍스트로 변환하고, 지정한 헤드 템플릿의 내용을 앞에 추가:

`ppmtoarbtxt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/템플릿</span>` -hd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/헤드_템플릿</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.txt</span>

- 주어진 템플릿에 따라 PPM 이미지를 텍스트로 변환하고, 지정한 테일 템플릿의 내용을 뒤에 추가:

`ppmtoarbtxt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/템플릿</span>` -hd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/테일_템플릿</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.txt</span>

- 버전 표시:

`ppmtoarbtxt -version`

---
layout: page
title: linux/asciiart (한국어)
description: "이미지를 ASCII로 변환합니다."
content_hash: c5862de582dc9bbe286029a289d2edb66f7dc9b0
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/asciiart.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/asciiart.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/asciiart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/asciiart.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/asciiart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/asciiart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciiart

이미지를 ASCII로 변환합니다.
더 많은 정보: <https://github.com/nodanaonlyzuul/asciiart>.

- 파일에서 이미지를 읽어와 ASCII로 출력:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>

- URL에서 이미지를 읽어와 ASCII로 출력:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com/image.jpg</span>

- 출력 너비 선택 (기본값은 100):

`asciiart --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>

- ASCII 출력에 색상 적용:

`asciiart --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>

- 출력 형식 선택 (기본 형식은 텍스트):

`asciiart --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>

- 문자 맵을 반전:

`asciiart --invert-chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>

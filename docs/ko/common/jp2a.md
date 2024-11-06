---
layout: page
title: common/jp2a (한국어)
description: "JPEG 이미지를 ASCII로 변환."
content_hash: 86b42de0977ead256f724155c49154bcf1fb7c41
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jp2a.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jp2a

JPEG 이미지를 ASCII로 변환.
더 많은 정보: <https://csl.name/jp2a/>.

- 파일에서 JPEG 이미지를 읽어 ASCII로 출력:

`jp2a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpeg</span>

- URL에서 JPEG 이미지를 읽어 ASCII로 출력:

`jp2a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com/image.jpeg</span>

- ASCII 출력을 색상화:

`jp2a --colors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpeg</span>

- ASCII 출력에 사용할 문자 지정:

`jp2a --chars='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">..-ooxx@@</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpeg</span>

- ASCII 출력을 파일에 작성:

`jp2a --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpeg</span>

- 웹 브라우저에서 볼 수 있도록 HTML 파일 형식으로 ASCII 출력 작성:

`jp2a --html --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpeg</span>

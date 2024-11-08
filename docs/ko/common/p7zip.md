---
layout: page
title: common/p7zip (한국어)
description: "높은 압축률을 자랑하는 7-Zip 파일 압축기의 래퍼."
content_hash: ea1662c824ebd062bbaa83592bcee0c9dad19612
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/p7zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# p7zip

높은 압축률을 자랑하는 7-Zip 파일 압축기의 래퍼.
내부적으로 7za 또는 7zr 명령을 실행합니다.
더 많은 정보: <https://p7zip.sourceforge.net>.

- 파일을 아카이브하고 7z로 압축된 버전으로 대체:

`p7zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 아카이브하고 입력 파일 유지:

`p7zip -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 해제압축하고 원본 비압축 버전으로 대체:

`p7zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축된_파일.ext</span>`.7z`

- 파일을 해제압축하고 입력 파일 유지:

`p7zip -d -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축된_파일.ext</span>`.7z`

- 일부 검사를 건너뛰고 압축 또는 해제압축 강제 실행:

`p7zip -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

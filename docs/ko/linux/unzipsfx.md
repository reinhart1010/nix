---
layout: page
title: linux/unzipsfx (한국어)
description: "Zip 파일에 자동 추출 스텁을 추가하여 자동 추출 압축 바이너리 파일을 생성합니다."
content_hash: c740d5e1e92d862fff6e08b5eab735f251ec7520
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/unzipsfx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/unzipsfx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unzipsfx

Zip 파일에 자동 추출 스텁을 추가하여 자동 추출 압축 바이너리 파일을 생성합니다.
더 많은 정보: <https://manned.org/unzipsfx>.

- Zip 아카이브의 자동 추출 바이너리 파일 생성:

`cat unzipsfx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>` && chmod 755 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 현재 디렉토리에서 자동 추출 바이너리 추출:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./경로/대상/바이너리)</span>

- 오류가 있는지 자동 추출 바이너리 테스트:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./경로/대상/바이너리)</span>` -t`

- 추출 없이 자동 추출 바이너리 내 파일의 내용 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./경로/대상/바이너리)</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명</span>

- 자동 추출 바이너리 내 Zip 아카이브의 주석 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./경로/대상/바이너리)</span>` -z`

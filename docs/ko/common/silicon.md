---
layout: page
title: common/silicon (한국어)
description: "소스 코드의 이미지를 생성."
content_hash: 6db7c3967c236c3e5110149c14bd6f70c3993e22
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/silicon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# silicon

소스 코드의 이미지를 생성.
더 많은 정보: <https://github.com/Aloxaf/silicon>.

- 특정 소스 파일에서 이미지 생성:

`silicon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지</span>

- 특정 프로그래밍 언어 구문 강조를 사용하여 소스 파일에서 이미지 생성 (예: `rust`, `py`, `js` 등):

`silicon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지</span>` --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어|확장자</span>

- `stdin`에서 이미지 생성:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | silicon --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지</span>

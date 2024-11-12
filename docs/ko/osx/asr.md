---
layout: page
title: osx/asr (한국어)
description: "디스크 이미지를 볼륨에 복원(복사)합니다."
content_hash: 8b2c763b4bc08d96eb9e07c9e63211021baff2cf
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/asr.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/asr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/asr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/asr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/asr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asr

디스크 이미지를 볼륨에 복원(복사)합니다.
명령어 이름은 Apple Software Restore를 의미합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/asr.8.html>.

- 디스크 이미지를 대상 볼륨에 복원:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_파일.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/볼륨_파일</span>

- 복원하기 전에 대상 볼륨 지우기:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_파일.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/볼륨_파일</span>` --erase`

- 복원 후 검증 건너뛰기:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_파일.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/볼륨_파일</span>` --noverify`

- 중간 디스크 이미지를 사용하지 않고 볼륨 복제:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/볼륨_파일</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/볼륨_파일</span>

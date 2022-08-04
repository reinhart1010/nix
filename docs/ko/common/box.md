---
layout: page
title: common/box (한국어)
description: "Phar의 빌드 및 관리를 위한 PHP 어플리케이션."
content_hash: 992cad0f9b90cb64cf23c89d8a0779a3f0b96216
related_topics:
  - title: English version
    url: /en/common/box.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/box.html
    icon: bi bi-globe
---
# box

Phar의 빌드 및 관리를 위한 PHP 어플리케이션.
더 많은 정보: <https://github.com/box-project/box>.

- 새 Phar 파일 작성:

`box build`

- 특정 구성 파일을 사용하여 새 Phar 파일 작성:

`box build -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config/의/경로</span>

- PHAR PHP 확장에 대한 정보 표시:

`box info`

- 특정 Phar 파일에 대한 정보 표시:

`box info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">phar_파일/의/경로</span>

- 현재 작업 디렉토리에서 처음으로 발견된 구성 파일 확인:

`box validate`

- 특정 Phar 파일의 서명 확인:

`box verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">phar_파일/의/경로</span>

- 사용 가능한 모든 명령 및 옵션 표시:

`box help`

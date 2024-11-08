---
layout: page
title: common/phan (한국어)
description: "PHP용 정적 분석 도구."
content_hash: a2d8fd081b8a619610a6c41d8da554e9471a8d0e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/phan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phan

PHP용 정적 분석 도구.
더 많은 정보: <https://github.com/phan/phan>.

- 현재 디렉터리에 `.phan/config.php` 생성:

`phan --init`

- 특정 레벨을 사용하여 Phan 구성 파일 생성 (1이 가장 엄격하고 5가 가장 덜 엄격함):

`phan --init --init-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레벨</span>

- 현재 디렉터리 분석:

`phan`

- 하나 이상의 디렉터리 분석:

`phan --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/다른_폴더</span>

- 구성 파일 지정 (기본값은 `.phan/config.php`):

`phan --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.php</span>

- 출력 모드 지정:

`phan --output-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|verbose|json|csv|codeclimate|checkstyle|pylint|html</span>

- 병렬 프로세스 수 지정:

`phan --processes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_수</span>

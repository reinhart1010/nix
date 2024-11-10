---
layout: page
title: common/smalltalkci (한국어)
description: "GitHub Actions, Travis CI, AppVeyor, GitLab CI 등과 함께 Smalltalk 프로젝트를 테스트하기 위한 프레임워크."
content_hash: fbd7a2b34c10a9497bf1c3df4b2b969ca2c9083d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/smalltalkci.html
    icon: bi bi-globe
tldri18n_status: 2
---
# smalltalkci

GitHub Actions, Travis CI, AppVeyor, GitLab CI 등과 함께 Smalltalk 프로젝트를 테스트하기 위한 프레임워크.
더 많은 정보: <https://github.com/hpi-swa/smalltalkCI>.

- 구성 파일에 대한 테스트 실행:

`smalltalkci `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/.smalltalk.ston</span>

- 현재 디렉토리의 `.smalltalk.ston` 구성에 대한 테스트 실행:

`smalltalkci`

- GUI 모드에서 테스트 디버그 (VM 창 표시):

`smalltalkci --headful`

- 테스트를 위한 잘 알려진 Smalltalk 이미지 다운로드 및 준비:

`smalltalkci --smalltalk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Squeak64-Trunk</span>

- 사용자 지정 Smalltalk 이미지 및 VM 지정:

`smalltalkci --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Smalltalk.image</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/vm</span>

- 캐시 정리 및 빌드 삭제:

`smalltalkci --clean`

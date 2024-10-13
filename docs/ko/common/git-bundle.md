---
layout: page
title: common/git-bundle (한국어)
description: "객체와 참조를 아카이브로 패키징합니다."
content_hash: 8ee6ddda3a412ae12c5d9f93639d7853e62a265f
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-bundle.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bundle.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bundle.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bundle.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bundle

객체와 참조를 아카이브로 패키징합니다.
더 많은 정보: <https://git-scm.com/docs/git-bundle>.

- 특정 브랜치의 모든 객체와 참조를 포함하는 번들 파일 생성:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 모든 브랜치의 번들 파일 생성:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bundle</span>` --all`

- 현재 브랜치의 마지막 5개의 커밋을 포함하는 번들 파일 생성:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bundle</span>` -5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- 최근 7일간의 커밋을 포함하는 번들 파일 생성:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bundle</span>` --since 7.days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- 번들 파일이 유효하고 현재 저장소에 적용될 수 있는지 확인:

`git bundle verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bundle</span>

- 번들에 포함된 참조 목록을 `stdout`에 출력:

`git bundle unbundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bundle</span>

- 번들 파일에서 특정 브랜치를 현재 저장소로 언번들:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 번들에서 새 저장소 생성:

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bundle</span>

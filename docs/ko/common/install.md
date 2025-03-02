---
layout: page
title: common/install (한국어)
description: "파일 복사 및 속성 설정."
content_hash: 7814a1e0fb1bc320ac30b40ca44a053b0e027f83
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# install

파일 복사 및 속성 설정.
파일 (자주 실행 가능)을 시스템 위치 (예: `/usr/local/bin`)에 복사하고 적절한 권한/소유권을 부여합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>.

- 파일들을 목표에 복사:

`install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일1 경로/대상/원본_파일2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표</span>

- 파일들을 목표에 복사하고 소유권 설정:

`install --owner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일1 경로/대상/원본_파일2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표</span>

- 파일들을 목표에 복사하고 그룹 소유권 설정:

`install --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일1 경로/대상/원본_파일2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표</span>

- `mode`를 설정하고 파일들을 목표에 복사:

`install --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일1 경로/대상/원본_파일2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표</span>

- 파일들을 목표에 복사하고 원본의 접근/수정 시간 적용:

`install --preserve-timestamps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일1 경로/대상/원본_파일2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표</span>

- 파일들을 목표에 복사하고 목표 디렉토리가 없으면 생성:

`install -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일1 경로/대상/원본_파일2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표</span>

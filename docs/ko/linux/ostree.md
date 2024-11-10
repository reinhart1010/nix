---
layout: page
title: linux/ostree (한국어)
description: "운영 체제 루트 파일 시스템에 최적화된 바이너리 파일의 버전 관리 도구로, `git`과 유사합니다."
content_hash: 2823e5c1d067141437a2384ca2c49cfae6f699f1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ostree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ostree

운영 체제 루트 파일 시스템에 최적화된 바이너리 파일의 버전 관리 도구로, `git`과 유사합니다.
OSTree는 Fedora Silverblue, Fedora IoT, Fedora CoreOS와 같은 불변 이미지 기반 운영 체제의 기초입니다.
더 많은 정보: <https://ostreedev.github.io/ostree>.

- `$PWD`의 파일을 `$PWD/path/to/repo`의 메타데이터와 함께 저장소로 초기화:

`ostree init --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>

- 파일의 커밋(스냅샷) 생성:

`ostree commit --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>` --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 커밋 내 파일 표시:

`ostree ls --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_ID</span>

- 커밋의 메타데이터 표시:

`ostree show --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_ID</span>

- 커밋 목록 표시:

`ostree log --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 저장소 요약 표시:

`ostree summary --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>` --view`

- 사용 가능한 참조(브랜치) 표시:

`ostree refs --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>

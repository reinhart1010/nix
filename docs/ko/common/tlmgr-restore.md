---
layout: page
title: common/tlmgr-restore (한국어)
description: "`tlmgr backup`으로 생성된 패키지 백업 복원."
content_hash: f18d316acb4f20545e04023f962651168afc9aa2
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/tlmgr-restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr restore

`tlmgr backup`으로 생성된 패키지 백업 복원.
기본 백업 디렉토리는 `backupdir` 옵션에 의해 지정되며, `tlmgr option`으로 확인할 수 있습니다.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 모든 패키지에 대한 사용 가능한 모든 백업 리비전 나열:

`tlmgr restore`

- 특정 패키지에 대한 사용 가능한 모든 백업 리비전 나열:

`tlmgr restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지의 특정 리비전 복원:

`tlmgr restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>

- 백업된 모든 패키지의 최신 리비전 복원:

`tlmgr restore --all`

- 사용자 지정 백업 디렉토리에서 패키지 복원:

`tlmgr restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>` --backupdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/백업_디렉토리</span>

- 수행된 모든 작업을 출력하고 실제로 수행하지는 않음 (드라이런):

`tlmgr restore --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>

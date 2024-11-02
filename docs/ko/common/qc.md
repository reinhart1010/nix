---
layout: page
title: common/qc (한국어)
description: "QOwnNotes 노트에 저장된 명령 스니펫을 관리하고 실행."
content_hash: a5522e90d10bbea83b1b5340d8cf30a651338c02
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/qc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/qc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qc

QOwnNotes 노트에 저장된 명령 스니펫을 관리하고 실행.
같이 보기: `qownnotes`.
더 많은 정보: <https://www.qownnotes.org/getting-started/command-line-snippet-manager.html>.

- 스니펫 관리자를 설정, 예: QOwnNotes에서 보안 토큰 설정:

`qc configure`

- `Commands.md` 노트와 `commands` 태그가 붙은 모든 노트에서 명령 스니펫을 검색하고 출력:

`qc search`

- 스니펫을 실행하고 실행 전에 명령 표시:

`qc exec --command`

- 마지막 스니펫을 실행하고 실행 전에 명령 표시:

`qc exec --command --last`

- QOwnNotes에서 노트 폴더 전환:

`qc switch`

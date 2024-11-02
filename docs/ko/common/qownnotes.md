---
layout: page
title: common/qownnotes (한국어)
description: "Markdown 노트 작성 애플리케이션."
content_hash: 971ecb2a73c235deb02ec43ee4512a26842b00c4
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/qownnotes.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/qownnotes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qownnotes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qownnotes

Markdown 노트 작성 애플리케이션.
선택적으로 Nextcloud 및 ownCloud의 노트 작성 애플리케이션과 통합됩니다.
같이 보기: `qc`, 명령 스니펫 관리용.
더 많은 정보: <https://www.qownnotes.org/getting-started/cli-parameters.html>.

- 포터블 모드로 실행:

`QOwnNotes --portable`

- 설정 및 애플리케이션 환경에 대한 정보를 GitHub Markdown으로 덤프:

`QOwnNotes --dump-settings`

- 설정 및 내부 파일에 대한 다른 컨텍스트 지정:

`QOwnNotes --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트</span>

- 애플리케이션 시작 후 메뉴 동작 트리거:

`QOwnNotes --action `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">actionShow_Todo_List</span>

---
layout: page
title: osx/dockutil (한국어)
description: "macOS Dock 항목 관리 도구."
content_hash: 9ef8b5110d12577bc377aa62da348bbc18911291
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/dockutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/dockutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dockutil

macOS Dock 항목 관리 도구.
더 많은 정보: <https://github.com/kcrawford/dockutil>.

- 현재 사용자 Dock 끝에 애플리케이션 추가:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/애플리케이션</span>

- 현재 사용자 Dock에서 한 애플리케이션을 다른 애플리케이션으로 교체:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/애플리케이션</span>` --replacing '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dock_item_label</span>`'`

- 보기 옵션과 함께 폴더를 추가하고 폴더 아이콘 또는 스택으로 표시:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/폴더</span>` --view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grid|fan|list|auto</span>` --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">folder|stack</span>

- 다른 항목 뒤에 URL Dock 항목 추가:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vnc://example_server.local</span>` --label '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example VNC</span>`' --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dock_item_label</span>

- Dock에서 주어진 Dock 라벨 이름의 애플리케이션 제거:

`dockutil --remove '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dock_item_label</span>`'`

- 애플리케이션 뒤에 구분자를 추가:

`dockutil --add '' --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spacer|small-spacer|flex-spacer</span>` --section `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apps</span>` --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dock_item_label</span>

- 모든 구분자 타일 제거:

`dockutil --remove spacer-tiles`

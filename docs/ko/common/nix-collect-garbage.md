---
layout: page
title: common/nix-collect-garbage (한국어)
description: "사용되지 않거나 접근할 수 없는 nix 저장소 경로 삭제."
content_hash: 24d9e25a3cf59c8fd7ede88d3b22f1ab7bdd78cb
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/nix-collect-garbage.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nix-collect-garbage.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix-collect-garbage.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nix-collect-garbage

사용되지 않거나 접근할 수 없는 nix 저장소 경로 삭제.
세대는 `nix-env --list-generations` 명령어로 나열할 수 있습니다.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/nix-collect-garbage.html>.

- 각 프로필의 현재 세대에서 사용되지 않는 모든 저장소 경로 삭제:

`sudo nix-collect-garbage --delete-old`

- 오래된 저장소 경로 삭제 시뮬레이션:

`sudo nix-collect-garbage --delete-old --dry-run`

- 30일보다 오래된 모든 저장소 경로 삭제:

`sudo nix-collect-garbage --delete-older-than 30d`

---
layout: page
title: linux/pve-firewall (한국어)
description: "Proxmox VE 방화벽 관리."
content_hash: a38e3f59aa32647eb06b7981b0b7b94ea3445d8c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pve-firewall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pve-firewall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pve-firewall

Proxmox VE 방화벽 관리.
더 많은 정보: <https://pve.proxmox.com/wiki/Firewall>.

- 모든 방화벽 규칙을 컴파일하고 출력:

`pve-firewall compile`

- 로컬 네트워크 정보 표시:

`pve-firewall localnet`

- Proxmox VE 방화벽 서비스 재시작:

`pve-firewall restart`

- Proxmox VE 방화벽 서비스 시작:

`pve-firewall start`

- Proxmox VE 방화벽 서비스 중지:

`pve-firewall stop`

- 모든 방화벽 규칙 시뮬레이션:

`pve-firewall simulate`

- Proxmox VE 방화벽 상태 표시:

`pve-firewall status`

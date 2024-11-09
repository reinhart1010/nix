---
layout: page
title: linux/needrestart (한국어)
description: "라이브러리 업그레이드 후 다시 시작해야 하는 데몬 확인."
content_hash: ff849291e9ea88cb5f4bef6e81c7788a51629e50
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/needrestart.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/needrestart.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># needrestart

라이브러리 업그레이드 후 다시 시작해야 하는 데몬 확인.
더 많은 정보: <https://github.com/liske/needrestart>.

- 오래된 프로세스 나열:

`needrestart`

- 상호작용 모드로 서비스 다시 시작:

`sudo needrestart`

- [v]자세히 또는 [q]조용히 모드에서 오래된 프로세스 나열:

`needrestart -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v|q</span>

- [k]커널이 오래되었는지 확인:

`needrestart -k`

- CPU 마이크로코드가 오래되었는지 확인:

`needrestart -w`

- [b]배치 모드에서 오래된 프로세스 나열:

`needrestart -b`

- 특정 [c]구성 파일을 사용하여 오래된 프로세스 나열:

`needrestart -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정</span>

- 도움말 표시:

`needrestart --help`

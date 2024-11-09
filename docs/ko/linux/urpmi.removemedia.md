---
layout: page
title: linux/urpmi.removemedia (한국어)
description: "Mageia에서 미디어 제거."
content_hash: 7489763c6e0b2f39fab32c235b67f3038bc4de3e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/urpmi.removemedia.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/urpmi.removemedia.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># urpmi.removemedia

Mageia에서 미디어 제거.
참고: Mageia 문서에서는 미디엄과 저장소를 동의어로 사용합니다.
같이 보기: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.update`, `urpmf`, `urpmq`.
더 많은 정보: <https://wiki.mageia.org/en/URPMI#urpmi.removemedia>.

- 미디엄 제거:

`sudo urpmi.removemedia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미디엄</span>

- 모든 미디어 제거:

`sudo urpmi.removemedia -a`

- 미디어 이름에 대해 유사하게 일치하는 미디어 제거:

`sudo urpmi.removemedia -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

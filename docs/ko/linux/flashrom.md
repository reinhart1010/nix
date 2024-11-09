---
layout: page
title: linux/flashrom (한국어)
description: "플래시 칩을 읽고, 쓰고, 검증하고, 지웁니다."
content_hash: 98533d5a397fa13f8ac0d8c5e566d4b221ae9f30
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/flashrom.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/flashrom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flashrom

플래시 칩을 읽고, 쓰고, 검증하고, 지웁니다.
더 많은 정보: <https://manned.org/flashrom>.

- 칩을 검사하여 배선이 올바른지 확인:

`flashrom --programmer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그래머</span>

- 플래시를 읽고 파일로 저장:

`flashrom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그래머</span>` --read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 플래시에 쓰기:

`flashrom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그래머</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 플래시를 파일과 대조하여 검증:

`flashrom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그래머</span>` --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- Raspberry Pi를 사용하여 칩 검사:

`flashrom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux_spi:dev=/dev/spidev0.0</span>

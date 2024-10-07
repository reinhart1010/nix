---
layout: page
title: linux/systemd-machine-id-setup (한국어)
description: "설치 시 `/etc/machine-id`에 저장된 머신 ID를 프로비저닝된 ID 또는 무작위로 생성된 ID로 초기화."
content_hash: 4124ff56b08a69adfa30c9a40da0dd1e674916e3
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-machine-id-setup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-machine-id-setup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-machine-id-setup

설치 시 `/etc/machine-id`에 저장된 머신 ID를 프로비저닝된 ID 또는 무작위로 생성된 ID로 초기화.
참고: 이러한 명령은 높은 권한이 필요하므로 항상 `sudo`를 사용하여 실행해야 합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-machine-id-setup.html>.

- 생성되거나 커밋된 머신 ID 출력:

`systemd-machine-id-setup --print`

- 이미지 정책 지정:

`systemd-machine-id-setup --image-policy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_policy</span>

- 출력을 JSON 형식으로 표시:

`sudo systemd-machine-id-setup --json=pretty`

- 디렉터리 트리 대신 디스크 이미지에서 작업 수행:

`systemd-machine-id-setup --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/이미지</span>

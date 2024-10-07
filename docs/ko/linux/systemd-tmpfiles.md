---
layout: page
title: linux/systemd-tmpfiles (한국어)
description: "휘발성 및 임시 파일과 디렉토리를 생성, 삭제 및 정리합니다."
content_hash: d575a362b0cce2b6fbcfd2b1bdc2c8e0c90d6751
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-tmpfiles.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systemd-tmpfiles.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-tmpfiles.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-tmpfiles

휘발성 및 임시 파일과 디렉토리를 생성, 삭제 및 정리합니다.
이 명령어는 시스템 부팅 시 systemd 서비스에 의해 자동으로 호출되며, 수동으로 실행할 필요는 거의 없습니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html>.

- 설정에 따라 파일과 디렉토리 생성:

`systemd-tmpfiles --create`

- 나이 매개변수가 설정된 파일과 디렉토리 정리:

`systemd-tmpfiles --clean`

- 설정에 따라 파일과 디렉토리 제거:

`systemd-tmpfiles --remove`

- 사용자별 설정 적용:

`systemd-tmpfiles --create --user`

- 초기 부팅 시 실행할 라인 실행:

`systemd-tmpfiles --create --boot`

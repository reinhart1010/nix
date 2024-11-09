---
layout: page
title: common/tye (한국어)
description: "마이크로서비스와 분산 애플리케이션을 쉽게 개발, 테스트 및 배포."
content_hash: 0ef852b3b832f2838975e59762bf203d78d21e49
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tye.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tye.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tye

마이크로서비스와 분산 애플리케이션을 쉽게 개발, 테스트 및 배포.
더 많은 정보: <https://github.com/dotnet/tye>.

- 애플리케이션을 나타내는 `tye.yaml` 파일 스캐폴드:

`tye init`

- 애플리케이션을 로컬에서 실행:

`tye run`

- 애플리케이션의 컨테이너 빌드:

`tye build`

- 애플리케이션의 컨테이너 푸시:

`tye push`

- 애플리케이션을 Kubernetes에 배포:

`tye deploy`

- Kubernetes에서 배포된 애플리케이션 제거:

`tye undeploy`

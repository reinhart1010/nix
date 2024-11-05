---
layout: page
title: common/nvidia-smi (한국어)
description: "NVIDIA GPU 장치의 관리 및 모니터링 도구."
content_hash: 01969bd4645c54db354e36762b41940d3db9a948
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nvidia-smi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nvidia-smi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nvidia-smi

NVIDIA GPU 장치의 관리 및 모니터링 도구.
더 많은 정보: <https://developer.nvidia.com/nvidia-system-management-interface>.

- 사용 가능한 모든 GPU 및 이를 사용하는 프로세스의 정보 표시:

`nvidia-smi`

- 더 자세한 GPU 정보 표시:

`nvidia-smi --query`

- 1초 간격으로 전체 GPU 사용량 모니터링:

`nvidia-smi dmon`

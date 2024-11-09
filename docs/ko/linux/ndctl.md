---
layout: page
title: linux/ndctl (한국어)
description: "비휘발성 DIMM을 관리하는 도구."
content_hash: 86757580335b0b8cf6d575ad68299ee01b95033a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ndctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ndctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ndctl

비휘발성 DIMM을 관리하는 도구.
더 많은 정보: <https://manned.org/ndctl>.

- 'fsdax' 모드 네임스페이스 생성:

`ndctl create-namespace --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fsdax</span>

- 네임스페이스 모드를 'raw'로 변경:

`ndctl create-namespace --reconfigure=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespaceX.Y</span>` --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>

- 섹터 모드 네임스페이스의 일관성을 검사하고 필요 시 복구:

`ndctl check-namespace --repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespaceX.Y</span>

- 모든 네임스페이스, 영역, 버스 나열 (비활성 포함):

`ndctl list --namespaces --regions --buses --idle`

- 특정 네임스페이스를 나열하고 추가 정보를 많이 포함:

`ndctl list -vvv --namespace=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespaceX.Y</span>

- 'ACPI.NFIT' 버스에서 NVDIMM의 SMART 상태 이벤트 모니터링 실행:

`ndctl monitor --bus=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ACPI.NFIT</span>

- 네임스페이스 제거 (적용 가능한 경우) 또는 초기 상태로 재설정:

`ndctl destroy-namespace --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespaceX.Y</span>

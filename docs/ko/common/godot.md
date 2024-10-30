---
layout: page
title: common/godot (한국어)
description: "오픈 소스 2D 및 3D 게임 엔진."
content_hash: 0faba96bdc8d1ddc6e8ebd45130eda5e6c7bf237
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/godot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/godot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># godot

오픈 소스 2D 및 3D 게임 엔진.
더 많은 정보: <https://godotengine.org/>.

- 현재 디렉터리에 `project.godot` 파일이 포함되어 있으면 프로젝트를 실행하고, 그렇지 않으면 프로젝트 관리자를 열기:

`godot`

- 프로젝트 편집 (현재 디렉토리에 `project.godot` 파일이 포함되어 있어야 함):

`godot -e`

- 현재 디렉터리에 `project.godot` 파일이 포함되어 있어도 프로젝트 관리자를 열기:

`godot -p`

- 주어진 내보내기 사전 설정에 대한 프로젝트 내보내기 (사전 설정은 프로젝트에서 정의되어야 함):

`godot --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프리셋</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_경로</span>

- 독립형 GDScript 파일을 실행 (스크립트는 `SceneTree` 또는 `MainLoop`에서 상속되어야 함):

`godot -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.gd</span>

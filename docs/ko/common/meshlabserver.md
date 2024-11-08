---
layout: page
title: common/meshlabserver (한국어)
description: "MeshLab 3D 메쉬 처리 소프트웨어의 명령줄 인터페이스."
content_hash: 1cb24766673d193be078a1d50af3b6548a292002
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/meshlabserver.html
    icon: bi bi-globe
tldri18n_status: 2
---
# meshlabserver

MeshLab 3D 메쉬 처리 소프트웨어의 명령줄 인터페이스.
더 많은 정보: <https://manned.org/meshlabserver>.

- STL 파일을 OBJ 파일로 변환:

`meshlabserver -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.stl</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.obj</span>

- WRL 파일을 OFF 파일로 변환하고 출력 메쉬에 버텍스 및 면 노멀 포함:

`meshlabserver -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.wrl</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.off</span>` -om vn fn`

- 사용 가능한 모든 처리 필터 목록을 파일로 덤프:

`meshlabserver -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- MeshLab GUI에서 생성된 필터 스크립트를 사용하여 3D 파일 처리 (Filters > Show current filter script > Save Script):

`meshlabserver -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.ply</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.ply</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필터_스크립트.mlx</span>

- 필터 스크립트를 사용하여 3D 파일을 처리하고 필터 출력 내용을 로그 파일에 기록:

`meshlabserver -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.x3d</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.x3d</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필터_스크립트.mlx</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그파일</span>

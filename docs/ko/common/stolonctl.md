---
layout: page
title: common/stolonctl (한국어)
description: "Stolon의 CLI, PostgreSQL 고가용성을 위한 클라우드 네이티브 PostgreSQL 관리자."
content_hash: ce3989ae5dbc53591c25f29628749f5fdee24658
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stolonctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stolonctl

Stolon의 CLI, PostgreSQL 고가용성을 위한 클라우드 네이티브 PostgreSQL 관리자.
더 많은 정보: <https://github.com/sorintlab/stolon>.

- 클러스터 상태 확인:

`stolonctl --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` --store-backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토어_백엔드</span>` --store-endpoints `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토어_엔드포인트</span>` status`

- 클러스터 데이터 가져오기:

`stolonctl --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` --store-backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토어_백엔드</span>` --store-endpoints `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토어_엔드포인트</span>` clusterdata`

- 클러스터 사양 가져오기:

`stolonctl --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` --store-backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토어_백엔드</span>` --store-endpoints `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토어_엔드포인트</span>` spec`

- JSON 형식의 패치를 사용하여 클러스터 사양 업데이트:

`stolonctl --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` --store-backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토어_백엔드</span>` --store-endpoints `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토어_엔드포인트</span>` update --patch '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_사양</span>`'`

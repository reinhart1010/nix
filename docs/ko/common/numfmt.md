---
layout: page
title: common/numfmt (한국어)
description: "숫자를 사람이 읽기 쉬운 문자열로 변환하거나 그 반대로 변환."
content_hash: 05929b7c5a64b7393e46b978a94a7ddedc019e01
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/numfmt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/numfmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# numfmt

숫자를 사람이 읽기 쉬운 문자열로 변환하거나 그 반대로 변환.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>.

- 1.5K(SI 단위)를 1500으로 변환:

`numfmt --from=si 1.5K`

- 5번째 필드(1부터 시작)를 IEC 단위로 변환하되 헤더는 변환하지 않음:

`ls -l | numfmt --header=1 --field=5 --to=iec`

- IEC 단위로 변환하고, 5자리를 채워 왼쪽 정렬:

`du -s * | numfmt --to=iec --format="%-5f"`

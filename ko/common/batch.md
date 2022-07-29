---
layout: page
title: common/batch (한국어)
description: "시스템 로드 레벨이 허가된 후, 명령을 실행하십시오. 실제로 실행하기 위해서는 atd (혹은 atrun) 를 실행해야합니다."
content_hash: 872682cff88f645083b5b327dc94ab636b439790
related_topics:
  - title: English version
    url: /en/common/batch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/batch.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/batch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/batch.html
    icon: bi bi-globe
---
# batch

시스템 로드 레벨이 허가된 후, 명령을 실행하십시오. 실제로 실행하기 위해서는 atd (혹은 atrun) 를 실행해야합니다.
더 많은 정보: <https://manned.org/batch>.

- 표준 입력에서 명령 실행하기 (완료 시 `Ctrl + D` 를 누릅니다):

`batch`

- 표준 입력에서의 명령 실행하기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | batch`

- 특정 파일에서 명령 실행하기:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

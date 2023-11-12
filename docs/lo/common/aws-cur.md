---
layout: page
title: common/aws-cur (ລາວ)
description: "Create, query, ແລະ delete AWS ທີ່ສະແດງເຖິງຄຳຈຳກັດຄວາມ."
content_hash: b68bb4dd09d40f5434cf488aa9b1dd786194a02b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-cur.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-cur.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-cur.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-cur.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws cur

Create, query, ແລະ delete AWS ທີ່ສະແດງເຖິງຄຳຈຳກັດຄວາມ.
ຂໍ້ມູນເພີ່ມເຕີມ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- ສ້າງຕົ້ນທຶນ AWS ແລະ ລາຍງານການໃຊ້ງານຈາກໄຟລ໌ JSON:

`aws cur put-report-definition --report-definition file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/report_definition.json</span>

- ລາຍງານກາຍເຄື່ອນໄຫວຂອງບັນຊີ:

`aws cur describe-report-definitions`

- ລຶບລາຍງານການເຄື່ອນໄຫວ:

`aws cur --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_region</span>` delete-report-definition --report-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">report</span>

---
layout: page
title: linux/findfs (English)
description: "Finds a filesystem by label or UUID."
content_hash: 495e0703261d7f2b7f3c4189698e2c8e78f2e914
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# findfs

Finds a filesystem by label or UUID.
More information: <https://mirrors.edge.kernel.org/pub/linux/utils/util-linux>.

- Search block devices by filesystem label:

`findfs LABEL=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>

- Search by filesystem UUID:

`findfs UUID=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- Search by partition label (GPT or MAC partition table):

`findfs PARTLABEL=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partition_label</span>

- Search by partition UUID (GPT partition table only):

`findfs PARTUUID=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partition_uuid</span>

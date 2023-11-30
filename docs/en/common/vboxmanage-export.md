---
layout: page
title: common/vboxmanage-export (English)
description: "Export virtual machines to a virtual appliance (ISO) or a cloud service."
content_hash: 2e4b9f7e83f6ebd08383ae0d215442394e508c9b
last_modified_at: 2023-11-30
tldri18n_status: 2
---
# vboxmanage-export

Export virtual machines to a virtual appliance (ISO) or a cloud service.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-export>.

- Specify the target OVA file:

`VBoxManage export --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.ova</span>

- Export in OVF 0.9 legacy mode:

`VBoxManage export --legacy09`

- Export in OVF (0.9|1.0|2.0) format:

`VBoxManage export --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ovf09|ovf10|ovf20</span>

- Create manifest of the exported files:

`VBoxManage export --manifest`

- Specify a description of the VM:

`VBoxManage export --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_description</span>`"`

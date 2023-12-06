---
layout: page
title: common/vboxmanage-extpack (English)
description: "Manage extension packs for Oracle VirtualBox."
content_hash: b0e3b958257c1d2137be613a9c0649294d4d769e
last_modified_at: 2023-12-06
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-extpack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-extpack

Manage extension packs for Oracle VirtualBox.
More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-extpack>.

- Install extension packs to VirtualBox (Note: you need to remove the existing version of the extension pack before installing a new version.):

`VBoxManage extpack install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.vbox-extpack</span>

- Remove the existing version of the VirtualBox extension pack:

`VBoxManage extpack install --replace`

- Uninstall extension packs from VirtualBox:

`VBoxManage extpack uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension_pack_name</span>

- Uninstall extension packs and skip most uninstallation refusals:

`VBoxManage extpack uninstall --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension_pack_name</span>

- Clean up temporary files and directories left by extension packs:

`VBoxManage extpack cleanup`

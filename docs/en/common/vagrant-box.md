---
layout: page
title: common/vagrant-box (English)
description: "Manage Vagrant boxes (virtual machine images)."
content_hash: 2f7f40756c1a78de67f5bc5a9222ba0c0cd853f0
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/vagrant-box.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vagrant box

Manage Vagrant boxes (virtual machine images).
See also: `vagrant`.
More information: <https://developer.hashicorp.com/vagrant/docs/cli/box>.

- List all installed boxes:

`vagrant box list`

- Add a new box:

`vagrant box add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hashicorp/bionic64</span>

- Add a box from a custom URL:

`vagrant box add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my-box</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/my-box.box</span>

- Remove an installed box:

`vagrant box remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hashicorp/bionic64</span>

- Update all boxes that are in use in the current Vagrant environment:

`vagrant box update`

- Update a specific box:

`vagrant box update --box `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bento/debian-12</span>

- Check if there is a new version available for the box that you are using:

`vagrant box outdated`

- Clean up old versions of installed boxes:

`vagrant box prune`

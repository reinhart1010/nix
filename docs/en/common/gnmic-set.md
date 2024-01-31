---
layout: page
title: common/gnmic-set (English)
description: "Modify gnmi network device configuration."
content_hash: 5b5948b2c979826460e7805c3575c1333db89cf3
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# gnmic set

Modify gnmi network device configuration.
More information: <https://gnmic.kmrd.dev/cmd/set>.

- Update the value of a path:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` set --update-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` --update-value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Update the value of a path to match the contents of a JSON file:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` set --update-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` --update-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filepath</span>

- Replace the value of a path to match the contents of a JSON file:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` set --replace-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` --replace-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filepath</span>

- Delete the node at a given path:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` set --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

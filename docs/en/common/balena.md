---
layout: page
title: common/balena (English)
description: "Interact with the balenaCloud, openBalena and the balena API from the command-line."
content_hash: cc314138383bc60cf6a32b525b297ea7c337f0ac
related_topics:
  - title: 한국어 version
    url: /ko/common/balena.html
    icon: bi bi-globe
---
# balena

Interact with the balenaCloud, openBalena and the balena API from the command-line.
More information: <https://www.balena.io/docs/reference/cli/>.

- Log in to the balenaCloud account:

`balena login`

- Create a balenaCloud or openBalena application:

`balena app create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- List all balenaCloud or openBalena applications within the account:

`balena apps`

- List all devices associated with the balenaCloud or openBalena account:

`balena devices`

- Flash a balenaOS image to a local drive:

`balena local flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/balenaos.img</span>` --drive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_location</span>

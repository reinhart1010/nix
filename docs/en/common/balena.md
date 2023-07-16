---
layout: page
title: common/balena (English)
description: "Interact with the balenaCloud, openBalena and the balena API."
content_hash: 22aae16601cd90b58d0e8bfd9995d439b54a4457
last_modified_at: 2023-07-16
related_topics:
  - title: français version
    url: /fr/common/balena.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/balena.html
    icon: bi bi-globe
---
# balena

Interact with the balenaCloud, openBalena and the balena API.
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

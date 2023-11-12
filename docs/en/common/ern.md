---
layout: page
title: common/ern (English)
description: "Electrode Native platform command-line client."
content_hash: a8f59dfe5b51d054bff1b595f42d112869529506
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ern

Electrode Native platform command-line client.
More information: <https://native.electrode.io/reference/index-6>.

- Create a new `ern` application (`MiniApp`):

`ern create-miniapp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Run one or more `MiniApps` in the iOS/Android Runner application:

`ern run-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ios|android</span>

- Create an Electrode Native container:

`ern create-container --miniapps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/miniapp_directory</span>` --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ios|android</span>

- Publish an Electrode Native container to a local Maven repository:

`ern publish-container --publisher `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maven</span>` --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android</span>` --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"groupId":"com.walmart.ern","artifactId":"quickstart"}'</span>

- Transform an iOS container into a pre-compiled binary framework:

`ern transform-container --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ios</span>` --transformer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcframework</span>

- List all installed versions of Electrode Native:

`ern platform versions`

- Set a logging level:

`ern platform config set logLevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trace|debug</span>

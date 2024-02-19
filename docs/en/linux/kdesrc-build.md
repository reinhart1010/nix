---
layout: page
title: linux/kdesrc-build (English)
description: "Easily build KDE components from its source repositories."
content_hash: b6e6db2afff04a89224f6cbea796df7842a8ce70
last_modified_at: 2024-02-19
tldri18n_status: 2
---
# kdesrc-build

Easily build KDE components from its source repositories.
More information: <https://invent.kde.org/sdk/kdesrc-build>.

- Initialize `kdesrc-build`:

`kdesrc-build --initial-setup`

- Compile a KDE component and its dependencies from source:

`kdesrc-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Compile a component without updating its local code and without compiling its dependencies:

`kdesrc-build --no-src --no-include-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Refresh the build directories before compiling:

`kdesrc-build --refresh-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Resume compilation from a specific dependency:

`kdesrc-build --resume-from=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency_component</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Print full compilation info:

`kdesrc-build --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Build all configured components:

`kdesrc-build`

- Use system libraries in place of a component if it fails to build:

`kdesrc-build --no-stop-on-failure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

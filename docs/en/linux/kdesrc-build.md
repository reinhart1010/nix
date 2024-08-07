---
layout: page
title: linux/kdesrc-build (English)
description: "Easily build KDE components from its source repositories."
content_hash: 3803de769d0ed942aeff4fe9cad495766b3cdac9
last_modified_at: 2024-08-07
tldri18n_status: 2
---
# kdesrc-build

Easily build KDE components from its source repositories.
More information: <https://docs.kde.org/trunk5/en/kdesrc-build/kdesrc-build/index.html>.

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

- Run a component with a specified executable name:

`kdesrc-build --run --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Build all configured components:

`kdesrc-build`

- Use system libraries in place of a component if it fails to build:

`kdesrc-build --no-stop-on-failure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

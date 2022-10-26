---
layout: page
title: common/pyats-shell (English)
description: "Start a pre-loaded pyATS interactive Python Shell to save time in prototyping."
content_hash: ff4a7d2b64ec5c291fb18613d1068c3f9883d68d
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pyats shell

Start a pre-loaded pyATS interactive Python Shell to save time in prototyping.
More information: <https://pubhub.devnetcloud.com/media/genie-docs/docs/cli/genie_shell.html>.

- Open pyATS shell with a defined Testbed file:

`pyats shell --testbed-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/testbed.yaml</span>

- Open pyATS shell with a defined Pickle file:

`pyats shell --pickle-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pickle.file</span>

- Open pyATS with IPython disabled:

`pyats shell --no-ipython`

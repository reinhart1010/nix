---
layout: page
title: linux/xcowsay (English)
description: "Display a cute cow and message on your Linux desktop."
content_hash: d6a7db3ec04311d8c0193682b136aca3ab94d3c9
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/xcowsay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcowsay

Display a cute cow and message on your Linux desktop.
The cow is displayed for either a fixed amount of time, or an amount of time calculated from the size of the text. Click on the cow to dismiss it immediately.
More information: <https://www.doof.me.uk/xcowsay/>.

- Display a cow saying "hello, world":

`xcowsay "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello, world</span>`"`

- Display a cow with output from another command:

`ls | xcowsay`

- Display a cow at the specified X and Y coordinates:

`xcowsay --at=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Y</span>

- Display a different sized cow:

`xcowsay --cow-size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">small|med|large</span>

- Display a thought bubble instead of a speech bubble:

`xcowsay --think`

- Display a different image instead of the default cow:

`xcowsay --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

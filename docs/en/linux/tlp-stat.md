---
layout: page
title: linux/tlp-stat (English)
description: "Generate TLP status reports."
content_hash: d315b13d02624644cbf609f931b14770a087ac32
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# tlp-stat

Generate TLP status reports.
See also `tlp`.
More information: <https://linrunner.de/tlp/usage/tlp-stat>.

- Generate status report with configuration and all active settings:

`sudo tlp-stat`

- Show information about various devices:

`sudo tlp-stat --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">battery|disk|processor|graphics|pcie|rfkill|usb</span>

- Show verbose information about devices that support verbosity:

`sudo tlp-stat --verbose --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">battery|processor|pcie|usb</span>

- Show configuration:

`sudo tlp-stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>

- Monitor [p]ower supply `udev` [ev]ents:

`sudo tlp-stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-P|--pev</span>

- Show [p]ower [sup]ply diagonistics:

`sudo tlp-stat --psup`

- Show [temp]eratures and fan speed:

`sudo tlp-stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--temp</span>

- Show general system information:

`sudo tlp-stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--system</span>

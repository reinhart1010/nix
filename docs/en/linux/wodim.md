---
layout: page
title: linux/wodim (English)
description: "Command (aliased as `cdrecord` on some systems) for recording data to CDs or DVDs."
content_hash: 294e12b4787b8e17877a309e4642f35c5bf0699a
last_modified_at: 2024-06-11
tldri18n_status: 2
---
# wodim

Command (aliased as `cdrecord` on some systems) for recording data to CDs or DVDs.
Some invocations of wodim can cause destructive actions, such as erasing all the data on a disc.
More information: <https://manned.org/wodim>.

- Display optical drives available to `wodim`:

`wodim --devices`

- Record ("burn") an audio-only disc:

`wodim dev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/optical_drive</span>` -audio `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">track*.cdaudio</span>

- Burn a file to a disc, ejecting the disc once done (some recorders require this):

`wodim -eject dev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/optical_drive</span>` -data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.iso</span>

- Burn a file to the disc in an optical drive, potentially writing to multiple discs in succession:

`wodim -tao dev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/optical_drive</span>` -data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.iso</span>

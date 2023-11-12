---
layout: page
title: common/rtl_sdr (English)
description: "Raw data recorder for RTL-SDR receivers."
content_hash: c7efd45678401a1dfb6d1c351b808b4c61fc491b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rtl_sdr

Raw data recorder for RTL-SDR receivers.
Data is encoded using I/Q sampling (aka quadrature sampling).
More information: <https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr>.

- Save RAW data from a frequency (specified in Hz) to a file:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Pipe data to another program:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` - | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplay</span>

- Read a specified number of samples:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -`

- Specify the sample rate in Hz (ranges 225001-300000 and 900001-3200000):

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2400000</span>` -`

- Specify the device by its index:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` -`

- Specify the gain:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -`

- Specify the output block size:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9999999</span>` -`

- Use synchronous output:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -S -`

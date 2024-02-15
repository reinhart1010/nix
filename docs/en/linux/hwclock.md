---
layout: page
title: linux/hwclock (English)
description: "Read or change the hardware clock. Usually requires root."
content_hash: 3aa5bb027e629f768dddd8cb58c5a5e5cc931a95
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# hwclock

Read or change the hardware clock. Usually requires root.
More information: <https://manned.org/hwclock>.

- Display the current time as reported by the hardware clock:

`hwclock`

- Write the current software clock time to the hardware clock (sometimes used during system setup):

`hwclock --systohc`

- Write the current hardware clock time to the software clock:

`hwclock --hctosys`

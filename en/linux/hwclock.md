---
layout: page
title: linux/hwclock (English)
description: "Used for reading or changing the hardware clock. Usually requires root."
content_hash: 17982af4c8ac48ad503cdbc64b206e43f7ecd2c2
---
# hwclock

Used for reading or changing the hardware clock. Usually requires root.
More information: <https://manned.org/hwclock>.

- Display the current time as reported by the hardware clock:

`hwclock`

- Write the current software clock time to the hardware clock (sometimes used during system setup):

`hwclock --systohc`

- Write the current hardware clock time to the software clock:

`hwclock --hctosys`

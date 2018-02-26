#include <tunables/global>

/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java {
  #include <abstractions/base>
  capability dac_override,
  /bin/dash mrix,
  /bin/stty px,
  /dev/tty r,
  /etc/host.conf r,
  /etc/hosts r,
  /etc/java-8-openjdk/** r,
  /etc/nsswitch.conf r,
  /etc/passwd r,
  /etc/signal/** rw,
  /etc/signal/data/** rwk,
  /etc/timezone r,
  /home/** r,
  /opt/signal-cli-0.5.6/** r,
  /proc/** r,
  /run/resolvconf/resolv.conf r,
  /sys/devices/system/cpu/ r,
  /tmp/ r,
  /tmp/hsperfdata_ossec/ rw,
  /tmp/hsperfdata_ossec/** rw,
  /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java r,
  /usr/share/javazi/** r,
  /var/ossec/ r,
  /var/tmp/ r,
}

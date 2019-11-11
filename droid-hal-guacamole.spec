# These and other macros are documented in dhd/droid-hal-device.inc

%define device guacamole
%define vendor oneplus

%define vendor_pretty OnePlus
%define device_pretty OnePlus 7 Pro

%define installable_zip 1
%define droid_target_aarch64 1
%define enable_kernel_update 1

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define straggler_files \
/bt_firmware \
/dsp \
/firmware \
/persist \
%{nil}

%include rpm/dhd/droid-hal-device.inc

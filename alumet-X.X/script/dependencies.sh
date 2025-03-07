#!/bin/bash

URL="https://sh.rustup.rs"
REQUIRED="1.76"

DEP_RUST="rustc"
DEP_PKG=("curl" "git" "build-essential" "protobuf-compiler" "libssl-dev" "pkg-config")

##
# Check and install potentially missing system dependencies with APT manager.
# It ensure that all tools handling files, folders and compilation on targeted architecture are here.
##
OS_utils(){
    for pkg_os in "${DEP_PKG[@]}"; do
        if ! dpkg -l | grep -q "^ii  $pkg_os "; then
            echo -e "\e[33mWARNING\e[0m : Packages '$pkg_os' required. Installation..."
            apt install -y "$pkg_os" || exit
        fi
    done
}

##
# Check and install potentially missing RUST dependencies with 'rustup' toolchain management.
# It ensure that the RUST version is at least REQUIRED version to compile 'Alumet' correctly.
##
RUST_utils(){
    if ! dpkg -l | grep -q "^ii  $DEP_RUST "; then
        echo -e "\e[33mWARNING\e[0m : Rust packages required. Installation..."
        curl --proto '=https' --tlsv1.2 -sSf "$URL" | sh -s -- -y || exit

        echo 'source $HOME/.cargo/env' >> $HOME/.bashrc
        source $HOME/.cargo/env
    fi

    version=$(rustc --version | cut -d' ' -f2)
    [ -z "$version" ] && version="none"

    if [ "$(printf '%s\n' "$REQUIRED" "$version" | sort -V | head -n1)" != "$REQUIRED" ]; then
        echo -e "\e[33mWARNING\e[0m : Rust '$version' is too old. Installation of rust '$REQUIRED'..."
        rustup default nightly
    elif [ "$version" == "none" ]; then
        echo -e "\e[31mERROR\e[0m : 'rustc' command does not recognized..."
        exit 1
    fi
}

clear
echo -e "<< \e[35m CHECK DEPENDENCIES \e[0m >>\n"

OS_utils
RUST_utils
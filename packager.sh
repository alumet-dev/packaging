#!/bin/bash

NAME="alumet"
VERSION="0.8"
REVISION="1"
DISTRO="stable"
URGENCY="medium"

AUTHOR="Guillaume Raffin"
MAIL="theelectronwill@gmail.com"
MESSAGE="Message"

URL="https://github.com/alumet-dev/alumet/archive/refs/heads/main.zip"
ARCHIVE="sources.zip"

FILES=files
BIN="alumet-agent"

DEP_PKG=("build-essential" "devscripts" "debhelper")

export DEBFULLNAME="$AUTHOR"
export DEBEMAIL="$MAIL"

##
# Running a command with sudo permissions
##
permission() {
    if ! sudo -n true 2>/dev/null; then
        echo -e "\e[33mWARNING\e[0m : Root permissions are needed"
        if ! sudo "$@"; then
            echo -e "\e[31mERROR\e[0m : Failed to obtain root permissions."
            exit 1
        fi
    fi
}

##
# Check and install potentially missing dependencies
##
required(){
    permission apt update

    for i in "${DEP_PKG[@]}"; do
        if ! dpkg -l | grep -q "^ii  $i "; then
            echo -e "\e[33mWARNING\e[0m : Packages '$i' required. Installation..."
            apt install -y "$i" || exit
        fi
    done
}

##
# Download of 'Alumet' project source code from GitHub repository
##
download(){
    clear
    echo -e "<< \e[35m SOURCES DOWNLOADING \e[0m >>\n"

    base=$(find . -maxdepth 1 -type d -name "$NAME-*")
    dir="$NAME"-"$VERSION"

    if [ -d "$base" ]; then
        if [ ! -d "$dir" ]; then
            mv -f "$base" "$dir"
        fi
    else
        echo "\e[31mERROR\e[0m : No directory '$dir' found."
        exit 1
    fi

    cd "$dir" || exit
    curl -L "$URL" -o "$ARCHIVE" || exit

    unzip "$ARCHIVE" || exit
    rm "$ARCHIVE"
}

##
# Compile files in DEB package
##
package(){
    chmod -R 775 script || exit
    rm -f debian/changelog

    tar -czf ../"$NAME"_"$VERSION".orig.tar.gz . || exit
    dch --create \
        --package "$NAME" \
        --newversion "$VERSION"-"$REVISION" \
        --distribution "$DISTRO" \
        --urgency "$URGENCY" \
        "$MESSAGE" || exit

    dpkg-buildpackage -us -uc -b
}

##
# Cleaning useless construction files
##
cleaning(){
    dpkg-buildpackage -T clean
    rm -rf ${FILES:?}/$BIN
}

clear
echo -e "<< \e[35m PACKAGE CONSTRUCTION \e[0m >>\n"

required
download
package
cleaning
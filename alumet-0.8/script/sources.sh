#!/bin/bash

BIN="alumet-agent"
CONF="alumet-config.toml"
CMD="alumet"

REPO=alumet-main
FILES=files

##
# Rust compilation of 'Alumet' source code project
##
compile(){
    cd $REPO || exit
    source $HOME/.cargo/env
    cargo build --release -p "$BIN" --bins --all-features || exit
    cd ../
}

##
# Dispatch compiled binary from 'Alumet' source code project
##
dispatch(){
    cp $REPO/target/release/$BIN $FILES/ || exit

    chmod 775 debian/preinst debian/postinst || exit
    chmod 775 $FILES/$BIN $FILES/$CMD || exit
    chmod 775 $FILES/$CONF || exit

    rm -rf $REPO
}

clear
echo -e "<< \e[35m SOURCES COMPILATION \e[0m >>\n"

compile
dispatch
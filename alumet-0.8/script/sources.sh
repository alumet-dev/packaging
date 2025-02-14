#!/bin/bash

BIN="alumet-agent"
CONF="alumet-config.toml"
CMD="alumet"

FOLDER=alumet
FILES=files

##
# Rust compilation of 'Alumet' source code project
##
compile(){
    cd $FOLDER || exit
    source $HOME/.cargo/env
    cargo build --release -p "$BIN" --bins --all-features || exit
    cd ../
}

##
# Dispatch compiled binary from 'Alumet' source code project
##
dispatch(){
    cp $FOLDER/target/release/$BIN $FILES/ || exit

    chmod 775 debian/preinst debian/postinst || exit
    chmod 775 $FILES/$BIN $FILES/$CMD || exit
    chmod 775 $FILES/$CONF || exit

    rm -rf $FOLDER
}

clear
echo -e "<< \e[35m SOURCES COMPILATION \e[0m >>\n"

compile
dispatch
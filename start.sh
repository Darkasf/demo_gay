#!/bin/sh

COMMAND='python3 demogay.py'
LOGFILE=restart.txt

writelog() {
    now=`date`
    echo "$now $*" >> $LOGFILE
}

writelog "-------\nStarting\n--------"
while true ; do
    if $COMMAND; [ "$?" -eq 122 ]; then
        writelog "Stopping" && exit 0
    else
    writelog "Exited with status $?"
    writelog "Restarting"
    fi
done

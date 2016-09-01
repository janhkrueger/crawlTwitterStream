#!/bin/bash
#
# check, if script is already running

# Usage: change the patch for the lockfile

SCRIPTNAME='basename $0'
LOCKFILENAME="/var/lock/KillReporter/`basename $0`"
if [ -z "$FLOCK_SET" ] ; then
exec env FLOCK_SET=1 flock -n "${LOCKFILENAME}" "$0" "$@"
fi

python run.py --client=config.json

rm ${LOCKFILENAME}

#
# ---- END ----
#


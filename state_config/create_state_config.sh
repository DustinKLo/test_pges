#!/bin/bash
BASE_PATH=$(dirname "${BASH_SOURCE}")
BASE_PATH=$(cd "${BASE_PATH}"; pwd)

# source PGE env
export PGES_HOME=/home/ops/verdi/ops/test_pges
export PYTHONPATH=$BASE_PATH:$PGES_HOME:$PYTHONPATH
export PATH=$BASE_PATH:$PATH
export PYTHONDONTWRITEBYTECODE=1

# source environment
source $HOME/verdi/bin/activate

echo "##########################################" 1>&2
echo -n "Running Radar Mode PGE"
date 1>&2
echo -n "Running python code: create_state_config.py"
python $BASE_PATH/create_state_config.py $* > create_state_config.log
STATUS=$?
echo -n "Finished running create_state_config.py: " 1>&2
date 1>&2
if [ $STATUS -ne 0 ]; then
  echo "Failed to run create_state_config.py" 1>&2
  cat create_state_config.log 1>&2
  echo "{}"
  exit $STATUS
fi

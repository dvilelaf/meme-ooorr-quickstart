#!/bin/bash

# ------------------------------------------------------------------------------
#
#   Copyright 2024 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

if [ "$(git rev-parse --is-inside-work-tree)" = true ]
then
    poetry install
    poetry run python stop_service.py || echo "Stopping the deployment failed. Continuing with cleanup."
    docker rm -f $(docker ps -a -q --filter name=optimus)
    sudo rm -rf .optimus/services/*/deployment
else
    echo "$directory is not a git repo!"
    exit 1
fi

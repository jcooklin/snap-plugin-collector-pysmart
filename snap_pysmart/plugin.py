#!/usr/bin/env python

# http://www.apache.org/licenses/LICENSE-2.0.txt
#
# Copyright 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from snap_pysmart import Smartmon
from pkg_resources import get_distribution
import re


def run():
    version = 1
    _ver = re.search('^(\d+).*$', get_distribution("snap-plugin-collector-pysmart").version) 
    if len(_ver.groups()) > 0:
        version = _ver.groups()[0]
    Smartmon("SmartmonCollectorPlugin-py", int(version)).start_plugin()

if __name__ == "__main__":
    run()

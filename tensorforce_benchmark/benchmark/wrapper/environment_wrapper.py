# Copyright 2017 reinforce.io. All Rights Reserved.
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
# ==============================================================================

"""
Environment wrapper class.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

class EnvironmentWrapper(object):
    """
    Wraps around an environment to enable additional metrics for external libraries.
    """
    def __init__(self, env):
        self.env = env
        self.episode_end_callbacks = set()

    def reset(self):
        return self.env.reset()

    def close(self):
        return self.env.close()

    def add_episode_end_callback(self, callback):
        self.episode_end_callbacks.add(callback)
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

"""
To add a new task to PET, both a DataProcessor and a PVP for this task must
be added. The PVP is responsible for applying patterns to inputs and mapping
labels to their verbalizations (see the paper for more details on PVPs).
This file shows an example of a PVP for a new task.
"""

from typing import List

import petal
from pet.pvp import PVP, PVPS
from pet.utils import InputExample


class MyTaskPVP2(PVP):
    """
    Example for a pattern-verbalizer pair (PVP).
    """

    # Set this to the name of the task
    TASK_NAME = "my-task-pvp-2"

    # Set this to the verbalizer for the given task: a mapping from the task's labels (which can be obtained using
    # the corresponding DataProcessor's get_labels method) to tokens from the language model's vocabulary
    VERBALIZER = {}

    with open('/content/drive/MyDrive/Handshake/Handshake_Secure/Handshake_US/BMNT/InsightAI/Files_in_use/verbalizers.json') as json_file:
        VERBALIZER = json.load(json_file)




# register the PVP for this task with its name
PVPS[MyTaskPVP2.TASK_NAME] = MyTaskPVP2

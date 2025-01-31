# Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
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

NEED_TO_FIX_OP_LIST = [
    'fused_elemwise_activation',
    'bilinear_tensor_product',
    'conv2d_transpose',
    'depthwise_conv2d_transpose',
    'grid_sampler',
    'lstmp',
    'margin_rank_loss',
    'matmul',
    'scatter',
    'soft_relu',
    'squared_l2_distance',
    'tree_conv',
    'cvm',
    'cudnn_lstm',
    'rnn',
    'multi_dot',
    'index_add',
    'reshape2',
]

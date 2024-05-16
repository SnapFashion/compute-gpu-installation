# Copyright 2024 Google LLC
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

import pathlib

INSTALLER_DIR = pathlib.Path("/opt/google/cuda-installer/")
try:
    INSTALLER_DIR.mkdir(parents=True, exist_ok=True)
except PermissionError:
    pass


K80_DRIVER_VERSION = "470.239.06"
K80_DEVICE_CODE = "10de:102d"
K80_DRIVER_URL = f"https://us.download.nvidia.com/tesla/{K80_DRIVER_VERSION}/NVIDIA-Linux-x86_64-{K80_DRIVER_VERSION}.run"
K80_DRIVER_SHA256_SUM = (
    "7d74caac140a0432d79ebe8e4330dc796f39ba7dd40b3fcd61df760181bf9ccc"
)

CUDA_TOOLKIT_URL = "https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_530.30.02_linux.run"
CUDA_TOOLKIT_SHA256_SUM = (
    "68699036c12d71adb9ad2799dce2ff070270fab4488b90920b9756ab3f52c41c"
)

CUDA_SAMPLES_TARGZ = (
    "https://github.com/NVIDIA/cuda-samples/archive/refs/tags/v12.1.tar.gz"
)
CUDA_SAMPLES_SHA256_SUM = (
    "f758160645b366d79c2638d8dfd389f01029b8d179ab0c11726b9ef58aecebd9"
)

CUDA_PROFILE_FILENAME = pathlib.Path("/etc/profile.d/google_cuda_install.sh")
CUDA_BIN_FOLDER = "/usr/local/cuda-12.1/bin"
CUDA_LIB_FOLDER = "/usr/local/cuda-12.1/lib64"

NVIDIA_PERSISTANCED_INSTALLER = (
    "/usr/share/doc/NVIDIA_GLX-1.0/samples/nvidia-persistenced-init.tar.bz2"
)

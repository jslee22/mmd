import torch ,torchvision
print(torch.__version__,torch.cuda.is_available())

#检查mmdetection
import mmdet
print(mmdet.__version__)

#检查mmcv
from mmcv.ops import get_compiling_cuda_version,get_compiler_version
print(get_compiler_version())
print(get_compiling_cuda_version())

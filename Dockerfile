#FROM tensorflow/tensorflow:nightly-gpu
FROM nvcr.io/nvidia/tensorflow:20.07-tf2-py3

RUN pip uninstall tensorflow nvidia-dali-cuda110 nvidia-dali-tf-plugin-cuda110 -y

RUN pip install --no-cache --no-cache-dir tf-nightly

RUN pip install --no-cache --no-cache-dir \
      --extra-index-url https://developer.download.nvidia.com/compute/redist \
      nvidia-dali-cuda110 && \
    pip install --no-cache --no-cache-dir \
      --extra-index-url https://developer.download.nvidia.com/compute/redist \
      nvidia-dali-tf-plugin-cuda110

WORKDIR /workspace
COPY main.py .
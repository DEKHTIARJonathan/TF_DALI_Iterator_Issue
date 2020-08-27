docker build --network=host -t dali_test:latest .

# docker run -it --rm \
#   --gpus all \
#   --shm-size=2g --ulimit memlock=-1 --ulimit stack=67108864 \
#   dali_test:latest

docker run -it --rm --network=host \
  --gpus="device=1" \
  --shm-size=2g --ulimit memlock=-1 --ulimit stack=67108864 \
  dali_test:latest
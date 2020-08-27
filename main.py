import tensorflow as tf
import nvidia.dali.fn as fn
from nvidia.dali.pipeline import Pipeline
import nvidia.dali.plugin.tf as dali_tf

tf.compat.v1.disable_eager_execution()


def dali_const_dataset(batch_size, sample_size, device_id):
    pipeline = Pipeline(batch_size, 4, device_id)
    const = fn.constant(device='gpu', fdata=sample_size * [1.])
    pipeline.set_outputs(const)
    dali_dataset = dali_tf.DALIDataset(
        pipeline=pipeline,
        batch_size=batch_size,
        output_shapes=((batch_size, sample_size)),
        output_dtypes=(tf.float32),
        device_id=device_id)
    return dali_dataset


dali_dataset = dali_const_dataset(4, 2, 0)

# print("=======================================================================")
# print("TF2 Eager Mode")
# iterator = iter(dali_dataset)
# batch = iterator.get_next()
# print(batch[0].device)

print("=======================================================================")
print("TF2 Compat Mode")
iterator = tf.compat.v1.data.make_initializable_iterator(dali_dataset)
batch = iterator.get_next()
print(batch[0].device)

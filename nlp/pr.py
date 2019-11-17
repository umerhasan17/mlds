# Temporary storage for pr changes

# 254
tf.compat.v1.summary.FileWriterCache.clear()

# 23
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)

# 119
tf.io.decode_csv

# 221
tf.compat.v1.get_collection
tf.compat.v1.GraphKeys

# 226
tf.compat.v1.train.get_global_step

"""
INFO:tensorflow:TF_CONFIG environment variable: {u'environment': u'cloud', u'cluster': {}, u'job': {u'args': [u'--train_data_path=/home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/data/sines/train-1.csv', u'--eval_data_path=/home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/data/sines/valid-1.csv', u'--output_dir=/home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/trained/sines', u'--model=linear', u'--train_steps=10', u'--sequence_length=50'], u'job_name': u'sinemodel.task'}, u'task': {}}
INFO:tensorflow:Using config: {'_save_checkpoints_secs': 60, '_num_ps_replicas': 0, '_keep_checkpoint_max': 5, '_task_type': 'worker', '_global_id_in_cluster': 0, '_is_chief': True, '_cluster_spec': <tensorflow.python.training.server_lib.ClusterSpec object at 0x7fbdebc189d0>, '_model_dir': '/home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/trained/sines/', '_protocol': None, '_save_checkpoints_steps': None, '_keep_checkpoint_every_n_hours': 10000, '_service': None, '_session_config': allow_soft_placement: true
graph_options {
  rewrite_options {
    meta_optimizer_iterations: ONE
  }
}
, '_tf_random_seed': None, '_save_summary_steps': 100, '_device_fn': None, '_session_creation_timeout_secs': 7200, '_experimental_distribute': None, '_num_worker_replicas': 1, '_task_id': 0, '_log_step_count_steps': 100, '_experimental_max_worker_delay_secs': None, '_evaluation_master': '', '_eval_distribute': None, '_train_distribute': None, '_master': ''}
INFO:tensorflow:Not using Distribute Coordinator.
INFO:tensorflow:Running training and evaluation locally (non-distributed).
INFO:tensorflow:Start train and evaluate loop. The evaluate will happen after every checkpoint. Checkpoint frequency is determined based on RunConfig arguments: save_checkpoints_steps None or save_checkpoints_secs 60.
WARNING:tensorflow:From /usr/local/lib/python2.7/dist-packages/tensorflow_core/python/training/training_util.py:236: initialized_value (from tensorflow.python.ops.variables) is deprecated and will be removed in a future version.
Instructions for updating:
Use Variable.read_value. Variables in 2.X are initialized automatically both in eager and graph (inside tf.defun) contexts.
WARNING:tensorflow:From /usr/local/lib/python2.7/dist-packages/tensorflow_estimator/python/estimator/api/_v1/estimator/__init__.py:12: The name tf.estimator.inputs is deprecated. Please use tf.compat.v1.estimator.inputs instead.

WARNING:tensorflow:From /usr/local/lib/python2.7/dist-packages/tensorflow_core/python/autograph/converters/directives.py:119: The name tf.decode_csv is deprecated. Please use tf.io.decode_csv instead.

WARNING:tensorflow:From sinemodel/model.py:154: make_one_shot_iterator (from tensorflow.python.data.ops.dataset_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use `for ... in dataset:` to iterate over a dataset. If using `tf.estimator`, return the `Dataset` object directly from your input function. As a last resort, you can use `tf.compat.v1.data.make_one_shot_iterator(dataset)`.
INFO:tensorflow:Calling model_fn.
WARNING:tensorflow:From sinemodel/model.py:41: dense (from tensorflow.python.layers.core) is deprecated and will be removed in a future version.
Instructions for updating:
Use keras.layers.Dense instead.
WARNING:tensorflow:From /usr/local/lib/python2.7/dist-packages/tensorflow_core/python/layers/core.py:187: apply (from tensorflow.python.keras.engine.base_layer) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `layer.__call__` method instead.
WARNING:tensorflow:From sinemodel/model.py:177: The name tf.losses.mean_squared_error is deprecated. Please use tf.compat.v1.losses.mean_squared_error instead.

WARNING:tensorflow:From /usr/local/lib/python2.7/dist-packages/tensorflow_core/python/ops/losses/losses_impl.py:121: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
WARNING:tensorflow:From sinemodel/model.py:178: The name tf.metrics.root_mean_squared_error is deprecated. Please use tf.compat.v1.metrics.root_mean_squared_error instead.

WARNING:tensorflow:From sinemodel/model.py:221: The name tf.get_collection is deprecated. Please use tf.compat.v1.get_collection instead.

WARNING:tensorflow:From sinemodel/model.py:221: The name tf.GraphKeys is deprecated. Please use tf.compat.v1.GraphKeys instead.

WARNING:tensorflow:
The TensorFlow contrib module will not be included in TensorFlow 2.0.
For more information, please see:
  * https://github.com/tensorflow/community/blob/master/rfcs/20180907-contrib-sunset.md
  * https://github.com/tensorflow/addons
  * https://github.com/tensorflow/io (for I/O related ops)
If you depend on functionality not listed there, please file an issue.

WARNING:tensorflow:From sinemodel/model.py:226: The name tf.train.get_global_step is deprecated. Please use tf.compat.v1.train.get_global_step instead.

INFO:tensorflow:Done calling model_fn.
INFO:tensorflow:Create CheckpointSaverHook.
INFO:tensorflow:Graph was finalized.
2019-11-17 17:50:25.169747: I tensorflow/core/platform/cpu_feature_guard.cc:145] This TensorFlow binary is optimized with Intel(R) MKL-DNN to use the following CPU instructions in performance critical operations:  AVX2 FMA
To enable them in non-MKL-DNN operations, rebuild TensorFlow with the appropriate compiler flags.
2019-11-17 17:50:25.178644: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2200000000 Hz
2019-11-17 17:50:25.179248: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x564942541c90 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2019-11-17 17:50:25.179308: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2019-11-17 17:50:25.179704: I tensorflow/core/common_runtime/process_util.cc:115] Creating new thread pool with default inter op setting: 2. Tune using inter_op_parallelism_threads for best performance.
INFO:tensorflow:Running local_init_op.
INFO:tensorflow:Done running local_init_op.
INFO:tensorflow:Saving checkpoints for 0 into /home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/trained/sines/model.ckpt.
INFO:tensorflow:loss = 1.3969852, step = 1
INFO:tensorflow:Saving checkpoints for 10 into /home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/trained/sines/model.ckpt.
INFO:tensorflow:Calling model_fn.
INFO:tensorflow:Done calling model_fn.
INFO:tensorflow:Starting evaluation at 2019-11-17T17:50:26Z
INFO:tensorflow:Graph was finalized.
INFO:tensorflow:Restoring parameters from /home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/trained/sines/model.ckpt-10
INFO:tensorflow:Running local_init_op.
INFO:tensorflow:Done running local_init_op.
INFO:tensorflow:Finished evaluation at 2019-11-17-17:50:27
INFO:tensorflow:Saving dict for global step 10: RMSE = 0.5602834, RMSE_same_as_last = 0.2961621, global_step = 10, loss = 0.3139175
INFO:tensorflow:Saving 'checkpoint_path' summary for global step 10: /home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/trained/sines/model.ckpt-10
WARNING:tensorflow:From sinemodel/model.py:161: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

INFO:tensorflow:Calling model_fn.
INFO:tensorflow:Done calling model_fn.
WARNING:tensorflow:From /usr/local/lib/python2.7/dist-packages/tensorflow_core/python/saved_model/signature_def_utils_impl.py:201: build_tensor_info (from tensorflow.python.saved_model.utils_impl) is deprecated and will be removed in a future version.
Instructions for updating:
This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.utils.build_tensor_info or tf.compat.v1.saved_model.build_tensor_info.
INFO:tensorflow:Signatures INCLUDED in export for Eval: None
INFO:tensorflow:Signatures INCLUDED in export for Classify: None
INFO:tensorflow:Signatures INCLUDED in export for Regress: None
INFO:tensorflow:Signatures INCLUDED in export for Predict: ['serving_default', 'predictions']
INFO:tensorflow:Signatures INCLUDED in export for Train: None
INFO:tensorflow:Restoring parameters from /home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/trained/sines/model.ckpt-10
INFO:tensorflow:Assets added to graph.
INFO:tensorflow:No assets to write.
INFO:tensorflow:SavedModel written to: /home/jupyter/training-data-analyst/courses/machine_learning/deepdive/09_sequence/trained/sines/export/exporter/temp-1574013027/saved_model.pb
INFO:tensorflow:Loss for final step: 0.33425674.


"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: readdata.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/07/11 11:31:43
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import math
import os
import random
import zipfile 

import numpy as np
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

def __init__(self, is_training, config):
    self.batch_size = batch_size = config.batch_size
    self.num_steps = num_steps = config.num_steps
    size = config.hidden_size
    vocab_size = config.vocab_size
     
    #�����Ƕ�������tensor��placeholder�����ǿɼ��������������룬
    # һ�������ݣ�һ����Ŀ��
    self._input_data = tf.placeholder(tf.int32, [batch_size, num_steps])
    self._targets = tf.placeholder(tf.int32, [batch_size, num_steps])
 
    # Slightly better results can be obtained with forget gate biases
    # initialized to 1 but the hyperparameters of the model would need to be
    # different than reported in the paper.
    # �������ȶ�����һ����lstm��cell�����cell�����parameter��������
    # number of units in the lstm cell, forget gate bias, һ���Ѿ�deprecated��
    # parameter input_size, state_is_tuple=False, �Լ�activation=tanh.��������
    # ������������parameter,��size��Ҳ���������ĵ�Ԫ�����Լ���forget gate
    # ��biasΪ0. �����Ƕ�Ӣ��ע����ʵ��˵��������bias��Ϊ1Ч�����ã���Ȼ
    # ���������ͬ��ԭ���ĵĽ����
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(size, forget_bias=0.0)
    if is_training and config.keep_prob < 1: # ��ѵ���Լ�Ϊ����ı�������С��1ʱ
      # �������dropoutwrapper��ʵ��Ϊÿһ��lstm cell�������Լ����������dropout����
      lstm_cell = tf.nn.rnn_cell.DropoutWrapper(
          lstm_cell, output_keep_prob=config.keep_prob)
    # �����cell��ʵ����һ�����Ľṹ�ˡ�����ÿһ����lstm cell������һ��õ����
    # ��RNN
    cell = tf.nn.rnn_cell.MultiRNNCell([lstm_cell] * config.num_layers)
    # �������ĵ�4ҳ�½�4.1�������ĳ�ʼֵ����Ϊ0
    self._initial_state = cell.zero_state(batch_size, tf.float32)
     
    with tf.device("/cpu:0"):
      # �趨embedding�����Լ�ת�����뵥��Ϊembedding��Ĵ�������embedding_lookup������
      embedding = tf.get_variable("embedding", [vocab_size, size])
      inputs = tf.nn.embedding_lookup(embedding, self._input_data)
 
    if is_training and config.keep_prob < 1:
      # ���������dropout
      inputs = tf.nn.dropout(inputs, config.keep_prob)
 
    # Simplified version of tensorflow.models.rnn.rnn.py's rnn().
    # This builds an unrolled LSTM for tutorial purposes only.
    # In general, use the rnn() or state_saving_rnn() from rnn.py.
    #
    # The alternative version of the code below is:
    #
    # from tensorflow.models.rnn import rnn
    # inputs = [tf.squeeze(input_, [1])
    #           for input_ in tf.split(1, num_steps, inputs)]
    # outputs, state = rnn.rnn(cell, inputs, initial_state=self._initial_state)
     
    outputs = []
    state = self._initial_state
    with tf.variable_scope("RNN"):
      for time_step in range(num_steps):
        if time_step > 0: tf.get_variable_scope().reuse_variables()
        # ��state��ʼ����RNN�ܹ������Ϊcell������Լ��µ�state.
        (cell_output, state) = cell(inputs[:, time_step, :], state)
        outputs.append(cell_output)
 
    # �������Ϊcell���������softmax weight w�����softmax bias b. �ⱻ����logit
    output = tf.reshape(tf.concat(1, outputs), [-1, size])
    softmax_w = tf.get_variable("softmax_w", [size, vocab_size])
    softmax_b = tf.get_variable("softmax_b", [vocab_size])
    logits = tf.matmul(output, softmax_w) + softmax_b
    # loss������average negative log probability, �����������ֳɵĺ���sequence_loss_by_example
    # ���ﵽ���Ч����
    loss = tf.nn.seq2seq.sequence_loss_by_example(
        [logits],
        [tf.reshape(self._targets, [-1])],
        [tf.ones([batch_size * num_steps])])
    self._cost = cost = tf.reduce_sum(loss) / batch_size
    self._final_state = state
 
    if not is_training:
      return
    # learning rate
    self._lr = tf.Variable(0.0, trainable=False)
    tvars = tf.trainable_variables()
    # ����������ĺ͵�norm��clip�������
    grads, _ = tf.clip_by_global_norm(tf.gradients(cost, tvars),
                                      config.max_grad_norm)
    # ��֮ǰ�ı���learning rate����ʼ�ݶ��½��Ż�����
    optimizer = tf.train.GradientDescentOptimizer(self.lr)
    # һ���minimizeΪ��ȡcompute_gradient,����apply_gradient
    # �������ǲ���Ҫcompute gradient, ����ֱ�ӵ��ڽ���minimize�����ĺ��Ρ�
    self._train_op = optimizer.apply_gradients(zip(grads, tvars))##

def run_epoch(session, m, data, eval_op, verbose=False):
  """Runs the model on the given data."""
  epoch_size = ((len(data) // m.batch_size) - 1) // m.num_steps
  start_time = time.time()
  costs = 0.0
  iters = 0
  state = m.initial_state.eval()
  # ptb_iterator�����ڽ��������룬batch size�Լ����е�step�������
  # �������Լ�ÿһ��������Ӧ��һ��x��y��batch���ݣ���СΪ[batch_size, num_step]
  for step, (x, y) in enumerate(reader.ptb_iterator(data, m.batch_size,
                                                    m.num_steps)):
    # �ں����������session������rnnͼ��cost�� fina_state���������Ҳ����eval_op�Ľ��
    # ����eval_op����Ϊ�ú��������롣
    cost, state, _ = session.run([m.cost, m.final_state, eval_op],
                                 {m.input_data: x,
                                  m.targets: y,
                                  m.initial_state: state})
    costs += cost
    iters += m.num_steps
    # ÿһ�������к����Ŀǰ���
    if verbose and step % (epoch_size // 10) == 10:
      print("%.3f perplexity: %.3f speed: %.0f wps" %
            (step * 1.0 / epoch_size, np.exp(costs / iters),
             iters * m.batch_size / (time.time() - start_time)))
 
  return np.exp(costs / iters)
def main(_):
  # ��Ҫ����ȷ���������ݵ�path����Ȼû��ѵ��ģ��
  if not FLAGS.data_path:
    raise ValueError("Must set --data_path to PTB data directory")
  # ��ȡ�������ݲ������ǲ�ֿ�
  raw_data = reader.ptb_raw_data(FLAGS.data_path)
  train_data, valid_data, test_data, _ = raw_data
  # ��ȡ�û������config�������þ߾�������С���л��Ǵ�ģ��
  config = get_config()
  eval_config = get_config()
  eval_config.batch_size = 1
  eval_config.num_steps = 1
  # ������һ��defaultͼ����ʼsession
  with tf.Graph().as_default(), tf.Session() as session:
    #�Ƚ���initialization
    initializer = tf.random_uniform_initializer(-config.init_scale,
                                                config.init_scale)
    #ע�⣬�������variable scope�������ˣ�
    with tf.variable_scope("model", reuse=None, initializer=initializer):
      m = PTBModel(is_training=True, config=config)
    with tf.variable_scope("model", reuse=True, initializer=initializer):
      mvalid = PTBModel(is_training=False, config=config)
      mtest = PTBModel(is_training=False, config=eval_config)
 
    tf.initialize_all_variables().run()
     
    for i in range(config.max_max_epoch):
      # �ݼ�learning rate
      lr_decay = config.lr_decay ** max(i - config.max_epoch, 0.0)
      m.assign_lr(session, config.learning_rate * lr_decay)
      #��ӡ��perplexity
      print("Epoch: %d Learning rate: %.3f" % (i + 1, session.run(m.lr)))
      train_perplexity = run_epoch(session, m, train_data, m.train_op,
                                   verbose=True)
      print("Epoch: %d Train Perplexity: %.3f" % (i + 1, train_perplexity))
      valid_perplexity = run_epoch(session, mvalid, valid_data, tf.no_op())
      print("Epoch: %d Valid Perplexity: %.3f" % (i + 1, valid_perplexity))
 
    test_perplexity = run_epoch(session, mtest, test_data, tf.no_op())
    print("Test Perplexity: %.3f" % test_perplexity)

if __name__ == "__main__":
  main()

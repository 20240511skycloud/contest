<template>
  <el-table :data="tasks" style="width: 100%">
    <el-table-column prop="title" label="任务名称" width="180" />
    <el-table-column prop="dueDate" label="截止日期" width="180" />
    <el-table-column prop="status" label="状态" width="180" />
    <el-table-column prop="description" label="描述" />
    <el-table-column label="操作">
      <template #default="scope">
        <el-button size="small" @click="editTask(scope.row)">编辑</el-button>
        <el-popconfirm title="确定删除此任务吗？" @confirm="deleteTask(scope.row)">
          <template #reference>
            <el-button size="small" type="danger">删除</el-button>
          </template>
        </el-popconfirm>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import { defineEmits } from 'vue';
import api from '../services/api';  // 或者你的 API 服务

export default {
  props: {
    tasks: {
      type: Array,
      required: true,
    },
  },
  emits: ['task-updated', 'task-deleted'],
  setup(props, { emit }) {
    const editTask = (task) => {
      // 处理任务编辑逻辑
      emit('task-updated');
    };

    const deleteTask = async (task) => {
      try {
        await api.delete(`/api/tasks/${task.id}`); // 替换为你的 API 路径
        emit('task-deleted');
      } catch (error) {
        console.error(error);
      }
    };

    return {
      editTask,
      deleteTask,
    };
  },
};
</script>
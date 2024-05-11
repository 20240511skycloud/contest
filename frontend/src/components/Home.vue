<template>
  <el-container direction="vertical" style="height: 100vh;">
    <el-header>...</el-header>
    <el-main>
      <h1>欢迎来到任务管理系统</h1>
      <el-button type="danger" @click="logout">退出登录</el-button>
      <el-button type="primary" @click="$router.push('/create')">创建新任务</el-button>
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
    </el-main>
    <el-footer>...</el-footer>
  </el-container>
</template>

<script>
import {reactive, onMounted, ref} from 'vue';
import { defineEmits } from 'vue';

import api from '../services/api';
import {useRouter} from "vue-router";  // 或者你的 API 服务

export default {
  components: {
  },
  methods: {
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/login');
    },
  },
  emits: ['task-updated', 'task-deleted'],
  setup(props, { emit }) {
    const tasks = ref([]);
    const router = useRouter();

    const fetchTasks = async () => {
      try {
        const response = await api.get('/api/tasks'); // 替换为你的 API 路径
        tasks.value = response.data;
      } catch (error) {
        console.error(error);
      }
    };
    const editTask = (task) => {
      router.push({ path: '/create', query: { taskId: task.id, taskName: task.name }});      // 处理任务编辑逻辑
    };

    const deleteTask = async (task) => {
      try {
        await api.delete(`/api/tasks/${task.id}`); // 替换为你的 API 路径
        emit('task-deleted');
        //请求接口获取新的任务列表
        await fetchTasks();
      } catch (error) {
        console.error(error);
      }
    };

    onMounted(fetchTasks);

    return {
      tasks,
      fetchTasks,
      editTask,
      deleteTask,
    };
  },
};
</script>
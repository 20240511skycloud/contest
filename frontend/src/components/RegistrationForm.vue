<template>
  <el-container direction="vertical" style="height: 100vh;">
    <el-header>...</el-header>
    <el-main>
      <el-form :model="user" label-width="100px" @submit.prevent="handleSubmit">
        <el-form-item label="用户名">
          <el-input v-model="user.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="user.password" type="password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="user.email" placeholder="请输入邮箱"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit">注册</el-button>
        </el-form-item>
      </el-form>
    </el-main>
    <el-footer>...</el-footer>
  </el-container>
</template>

<script>
import { ref } from 'vue';
import api from '../services/api';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const user = ref({
      username: '',
      password: '',
      email: '',
    });
    const router = useRouter();

    const handleSubmit = async () => {
      try {
        await api.post('/api/users', user.value);
        // Redirect to login page
        router.push('/login');
      } catch (error) {
        console.error(error);
      }
    };

    return { user, handleSubmit };
  },
};
</script>
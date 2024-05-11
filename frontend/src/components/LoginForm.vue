<template>
  <el-container direction="vertical" style="height: 100vh;">
    <el-header>...</el-header>
    <el-main>
      <el-form :model="credentials" label-width="100px" @submit.prevent="handleSubmit">
        <el-form-item label="用户名">
          <el-input v-model="credentials.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="credentials.password" type="password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit">登录</el-button>
          <el-button @click="$router.push('/register')">注册</el-button>
        </el-form-item>
      </el-form>
    </el-main>
    <el-footer>...</el-footer>
  </el-container>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '../services/api'; // 调整路径以匹配你的项目结构


export default {
  setup() {
    const credentials = ref({
      username: '',
      password: '',
    });
    const router = useRouter();

    const handleSubmit = async () => {
      try {
        const response = await api.post('/api/users/login', credentials.value);
        // Store token in localStorage or Vuex
        localStorage.setItem('token', response.data.token);
        // Redirect to home page
        router.push('/home');
      } catch (error) {
        console.error(error);
        alert('出现错误，请重试或联系管理员');
      }
    };

    return { credentials, handleSubmit };
  },
};
</script>
<template>
  <el-container>
  <el-main>
    <el-form :model="task" label-width="100px" @submit.prevent="handleSubmit">
      <el-form-item label="标题">
        <el-input v-model="task.title" placeholder="请输入任务标题"></el-input>
      </el-form-item>
      <el-form-item label="描述">
        <el-input v-model="task.desc"  placeholder="请输入描述"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSubmit">保存</el-button>
      </el-form-item>
    </el-form>
  </el-main>
    </el-container>
</template>

<script>
import { ref } from 'vue';
import api from '../services/api';
import {useRouter} from "vue-router";

export default {
  props: {
    initialTask: {
      type: Object,
      default: () => ({}),
    },
  },
  setup(props, { emit }) {
    const task = ref({ ...props.initialTask });
    const router = useRouter();
    const handleSubmit = async () => {
      try {
        if (task.value.id) {
          // Update existing task
          await api.put(`/api/tasks/${task.value.id}`, task.value);
        } else {
          // Create new task
          await api.post('/api/tasks', task.value);
        }
        // Reset form or navigate back to task list
        //回到任务列表页面
        router.push('/home');
      } catch (error) {
        console.error(error);
      }
    };

    return { task, handleSubmit };
  },mounted() {
    //是否存在taskid，如果存在，则为编辑模式
    if(this.$route.query.taskId){
      api.get('/api/tasks/'+this.$route.query.taskId).then(res => {
        this.task = res.data;
        this.task.desc = res.data.description;
      });
    }
  }
};
</script>
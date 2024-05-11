import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/LoginForm.vue';
import Home from '../components/Home.vue';
import Register from '../components/RegistrationForm.vue';
import TaskDetails from '../components/TaskList.vue';
import TaskForm from "../components/TaskForm.vue";
// 导入其他需要的组件，例如 TaskDetails

const routes = [
    {
        path: '/',
        redirect: '/login', // 将根路径重定向到登录页
    },
    {
        path: '/home',
        name: 'HOME',
        component: Home,
        meta: { requiresAuth: true },
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
    },
    // 添加其他路由，例如：
    {
        path: '/tasks/:id',
        name: 'TaskDetails',
        component: TaskDetails,
        meta: { requiresAuth: true },
    },
    {
        path: '/create',
        name: 'createTask',
        component: TaskForm,
        meta: { requiresAuth: true },
    },
    // ...
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

// 可选：添加导航守卫来检查身份验证
router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth && !localStorage.getItem('token')) {
        // 如果路由需要身份验证但用户未登录，则重定向到登录页
        next('/login');
    } else {
        next();
    }
});

export default router;
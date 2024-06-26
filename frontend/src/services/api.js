import axios from "axios";

const api = axios.create({
    baseURL: 'http://127.0.0.1:5000/', // Replace with your backend API URL
});

// Add token to request headers
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Authorization ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export default api;
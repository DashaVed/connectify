import {API_URL} from "./consts";
import axios from "axios";

export const instance = axios.create({
    baseURL: API_URL,
});

instance.interceptors.request.use(function (config) {
    const access = localStorage.getItem('access');
    if (access) {
        config.headers['Authorization'] = `JWT ${access}`;
    } else {
        config.headers['Authorization'] = '';
    }
    return config;
}, function (error) {
    return Promise.reject(error);
});

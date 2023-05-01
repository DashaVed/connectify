import {API_URL} from "./consts";
import axios from "axios";
import {useTokenStore} from "@/stores/token";

const instance = axios.create({
    baseURL: API_URL,
});

instance.interceptors.request.use(function (config) {
    const token = useTokenStore();
    if (token.access) {
        config.headers['Authorization'] = `JWT ${token.access}`;
    } else {
        config.headers['Authorization'] = '';
    }
    return config;
}, function (error) {
    return Promise.reject(error);
});

export async function registerUser(formData) {
    try {
        const response = await instance.post('auth/users/', formData);
        return response.data
    } catch (e) {
        if (e.response.data.email) {
            throw new Error(e.response.data.email);
        }else {
            throw new Error(e.response.data.password);
        }
    }
}

export async function login(email, password) {
    try {
        const response = await instance.post('auth/jwt/create/', {email, password})
        return response.data
    } catch (e) {
        throw new Error(e.response.data)
    }
}

export async function refreshUserToken(refresh) {
    console.log(refresh)
    const response = await instance.post('auth/jwt/refresh', {refresh: refresh})
    return response.data.access
}

export async function getUser(id) {
    const response = await instance.get(`/users/${id}`);
    if (response.status === 404) {
        console.log(response)
    }
    return response.data
}

export async function createGroup(formData) {
    const response = await instance.post('/groups/', formData)
    if (response.status < 400) {
        return response.data
    }
    console.log(response)
    throw new Error("Не получилось создать группу, попробуйте еще раз");
}
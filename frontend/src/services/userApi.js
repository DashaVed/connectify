import {instance} from "@/services/api";
import {useAuthStore} from "@/stores/auth";


export async function registerUser(formData) {
    try {
        const response = await instance.post('auth/users/', formData);
        return response.data
    } catch (e) {
        if (e.response.data.email) {
            throw new Error(e.response.data.email);
        } else {
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

export async function resetPassword(email) {
    try {
        return await instance.post('auth/users/reset_password/', {email})
    } catch (e) {
        return e.response
    }
}

export async function resetPasswordConfirm(formData) {
    try {
        return await instance.post('auth/users/reset_password_confirm/', formData)
    } catch (e) {
        return e.response
    }
}

export async function changePassword(formData) {
    try {
        return await instance.put(`auth/change/password/${useAuthStore().user.id}`, formData)
    } catch (e) {
        throw new Error(e.response.data.old_password)
    }
}

export async function getProfile() {
    try {
        const response = await instance.get('auth/users/me/')
        return response.data
    } catch (e) {
        console.log(e)
    }
}

export async function refreshUserToken(refresh) {
    const response = await instance.post('auth/jwt/refresh', {refresh: refresh})
    return response.data.access
}

export async function getUser(id) {
    if (!id) {
        id = useAuthStore().user.id
    }
    const response = await instance.get(`/users/${id}`);
    if (response.status === 404) {
        console.log(response)
    }
    return response.data
}

export async function updateUser(userData) {
    try {
        const response = await instance.put(`users/${useAuthStore().user.id}/`, userData,
            {headers: {"Content-Type": "multipart/form-data"}});
        return response.data;
    } catch (e) {
        console.log(e.response.data)
        throw new Error(e.response.data)
    }
}
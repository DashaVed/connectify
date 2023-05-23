import {instance} from "@/services/api";


export async function getCategories() {
    return await instance.get('/categories/')
}

export async function getGroups() {
    return await instance.get('/groups/')
}

export async function createGroup(formData) {
    const response = await instance.post('/groups/', formData)
    if (response.status < 400) {
        return response.data
    }
    console.log(response)
    throw new Error("Не получилось создать группу, попробуйте еще раз");
}

export async function getGroup(group_id) {
    try {
        const response = await instance.get(`groups/${group_id}`);
        return response.data
    } catch (e) {
        console.log(e)
    }
}

export async function getUserGroup(user_id) {
    try {
        const response = await instance.get(`users/${user_id}/groups`);
        return response.data
    } catch (e) {
        console.log(e)
    }
}


export async function deleteGroup(group_id) {
    try {
        const response = await instance.delete(`groups/${group_id}`);
        return response.status
    } catch (e) {
        console.log(e)
    }
}


export async function addUserToGroup(data, group_id) {
    const response = await instance.put(`groups/${group_id}/`, data);
    return response.status
}

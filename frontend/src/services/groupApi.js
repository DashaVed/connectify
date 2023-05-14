import {instance} from "@/services/api";


export async function getCategories() {
    return await instance.get('/categories/')
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

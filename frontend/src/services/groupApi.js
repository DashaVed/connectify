import {instance} from "@/services/api";

export async function createGroup(formData) {
    const response = await instance.post('/groups/', formData)
    if (response.status < 400) {
        return response.data
    }
    console.log(response)
    throw new Error("Не получилось создать группу, попробуйте еще раз");
}
import {instance} from "@/services/api";

export async function createMeeting(formData) {
    const response = await instance.post('/meetings/', formData)
    if (response.status < 400) {
        return response.data
    }
    console.log(response)
    throw new Error("Не получилось создать встречу, попробуйте еще раз");
}
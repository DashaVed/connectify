import {instance} from "@/services/api";

export async function createMeeting(formData) {
    const response = await instance.post('/meetings/', formData)
    if (response.status < 400) {
        return response.data
    }
    console.log(response)
    throw new Error("Не получилось создать встречу, попробуйте еще раз");
}

export async function getMeeting(meeting_id) {
    try {
        const response = await instance.get(`meetings/${meeting_id}`);
        return response.data
    } catch (e) {
        console.log(e)
    }
}
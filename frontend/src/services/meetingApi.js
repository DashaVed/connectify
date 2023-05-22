import {instance} from "@/services/api";

export async function createMeeting(formData) {
    const response = await instance.post('/meetings/', formData)
    if (response.status < 400) {
        return response.data
    }
    console.log(response)
    throw new Error("Не получилось создать встречу, попробуйте еще раз");
}

export async function getMeetings() {
    return await instance.get('meetings/')
}

export async function getMeeting(meeting_id) {
    try {
        const response = await instance.get(`meetings/${meeting_id}`);
        return response.data
    } catch (e) {
        console.log(e)
    }
}

export async function getUserMeeting(user_id) {
    try {
        const response = await instance.get(`users/${user_id}/meetings`);
        return response.data
    } catch (e) {
        console.log(e)
    }
}


export async function deleteMeeting(meeting_id) {
    try {
        const response = await instance.delete(`meetings/${meeting_id}`);
        return response.status
    } catch (e) {
        console.log(e)
    }
}


export async function addUserToMeeting(data, meeting_id) {
    const response = await instance.put(`meetings/${meeting_id}/`, data);
    return response.status
}

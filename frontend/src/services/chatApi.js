import {instance} from "@/services/api";


export async function getChatHistory(room) {
    return await instance.get(`/chat?room=${room}`)
}
import {API_URL} from "./consts";
import axios from "axios";

const instance = axios.create({
    baseURL: API_URL,
});

export async function register_user(formData) {
    const response = await instance.post('/register/', formData);
    if (response.status === 500) {
        console.error(response);
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data
}
import axios from "axios";

const api = axios.create({
    baseURL: process.env.DB_HOST,
});

export default api;

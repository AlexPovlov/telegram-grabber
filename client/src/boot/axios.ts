import axios from "axios";
const token = localStorage.getItem("Authorization");
// @ts-ignore
axios.defaults.baseURL = import.meta.env.VITE_AXIOS_BASE || "/";
axios.defaults.headers.common.Authorization = token;
axios.defaults.headers.common["Content-Type"] = "application/json";

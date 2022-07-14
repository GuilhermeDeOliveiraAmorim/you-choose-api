import api from "./backend";

export const getMovies = async () => {
    const response = await api.get("/movies/");
    return response.data;
};

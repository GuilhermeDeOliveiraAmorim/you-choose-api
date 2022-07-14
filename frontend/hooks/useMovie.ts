import api from "../services/backend";
import { useQuery } from "react-query";

const getMovie = async (movie_id) => {
    const response = await api.get(`/movies/${movie_id}`);
    return response.data;
};

export default function useMovie(movie_id) {
    return useQuery(["movie", movie_id], () => getMovie(movie_id));
}

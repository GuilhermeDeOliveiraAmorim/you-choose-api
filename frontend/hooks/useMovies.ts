import api from "../services/backend";
import { useQuery } from "react-query";

const getMovies = async () => {
    const response = await api.get("/movies/");
    return response.data;
};

export default function useMovies() {
    return useQuery(["movies"], () => getMovies());
}

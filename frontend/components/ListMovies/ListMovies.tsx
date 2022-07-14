import { HStack, Spinner } from "@chakra-ui/react";
import Movie from "../Movie";
import useMovies from "../../hooks/useMovies";

const ListMovies = () => {

    const movies = useMovies()

    if (movies.isLoading) {
        return <Spinner />
    }

    return (
        <HStack m={4} spacing={4} overflow={"auto"}>
            {movies.data.map(movie =>
                <Movie id={movie.id} title={movie.title} year={movie.year} poster={movie.poster} imdbRating={movie.imdbRating} />
            )}
        </HStack>

    )
}

export default ListMovies;
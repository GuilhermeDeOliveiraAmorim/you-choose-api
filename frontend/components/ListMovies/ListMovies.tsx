import { Flex, Spinner } from "@chakra-ui/react";
import Movie from "../Movie";
import useMovies from "../../hooks/useMovies";

const ListMovies = () => {

    const movies = useMovies()

    if (movies.isLoading) {
        return <Spinner />
    }

    return (
        <Flex m={4} gap={"2"} flexWrap={"wrap"} justifyContent={"space-between"}>
            {movies.data.map(movie =>
                <Movie id={movie.id} title={movie.title} year={movie.year} poster={movie.poster} imdbRating={movie.imdbRating} />
            )}
        </Flex>
    )
}

export default ListMovies;
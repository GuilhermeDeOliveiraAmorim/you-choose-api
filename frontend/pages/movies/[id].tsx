import { Spinner } from "@chakra-ui/react"
import { useRouter } from "next/router"
import useMovie from "../../hooks/useMovie"

export default function DetalheMovies() {
    const router = useRouter()

    const { id } = router.query

    const movie = useMovie(id)

    if (movie.isFetching) {
        return <Spinner />
    }

    return (
        <div>
            Detalhes do filme: {movie.data.title}, do ano {movie.data.year}
        </div>
    )
}
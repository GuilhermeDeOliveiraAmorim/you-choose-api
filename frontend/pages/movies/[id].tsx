import { Box, Grid, GridItem, Image, Spinner, Text } from "@chakra-ui/react"
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
        <Grid
            h='200px'
            templateRows='repeat(2, 1fr)'
            templateColumns='repeat(5, 1fr)'
            gap={4}
            margin={4}
        >
            <GridItem rowSpan={2} colSpan={1} bg='tomato'>
                <Box shadow='lg'>
                    <Image objectFit='cover' src={movie.data.poster} alt={movie.data.title} />
                </Box>
            </GridItem>
            <GridItem colSpan={4} bg='papayawhip'>
                <Text>
                    {movie.data.title}
                </Text>
                <Text>
                    {movie.data.year}
                </Text>
                <Text>
                    {movie.data.imdbRating}
                </Text>
            </GridItem>
        </Grid>
    )
}
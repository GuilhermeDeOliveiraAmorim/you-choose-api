import { StarIcon } from "@chakra-ui/icons"
import { Badge, Box, Image, useToast } from "@chakra-ui/react"
import Link from "next/link";

interface IProps {
    id: number;
    title: string;
    year: string;
    poster: string;
    imdbRating: number;
}

export default function Movie(props: IProps) {

    const { id, title, year, poster, imdbRating } = props;

    const toast = useToast()

    const handleClick = () => {

        try {
            toast({
                title: "Parabéns",
                status: "success",
                duration: 2000,
                position: "bottom-right",
                isClosable: true
            })
        } catch (err) {
            toast({
                title: "Triste",
                status: "error",
                duration: 2000,
                position: "bottom-right",
                isClosable: true
            })
        }

    }

    return (
        <Link passHref href={`/movies/${id}`}>
            <Box cursor={'pointer'} onClick={handleClick} maxW='sm' borderWidth='1px' borderRadius='lg' overflow='hidden'>
                <Image objectFit='cover' src={poster} alt={title} />
                <Box p='6'>
                    <Box display='flex' alignItems='baseline'>
                        <Badge borderRadius='full' px='2' colorScheme='teal'>
                            gêneros
                        </Badge>
                        <Box
                            color='gray.500'
                            fontWeight='semibold'
                            letterSpacing='wide'
                            fontSize='xs'
                            textTransform='uppercase'
                            ml='2'
                        >
                            Bola, Bala
                        </Box>
                    </Box>

                    <Box
                        mt='1'
                        fontWeight='semibold'
                        as='h4'
                        lineHeight='tight'
                        noOfLines={1}
                    >
                        {title}
                    </Box>

                    <Box>
                        {year}
                    </Box>

                    <Box display='flex' mt='2' alignItems='center'>
                        {Array(10)
                            .fill('')
                            .map((_, i) => (
                                <StarIcon
                                    key={i}
                                    color={i < imdbRating ? 'teal.500' : 'gray.300'}
                                />
                            ))
                        }
                        {imdbRating}/10
                    </Box>
                </Box>
            </Box>
        </Link>

    )
}
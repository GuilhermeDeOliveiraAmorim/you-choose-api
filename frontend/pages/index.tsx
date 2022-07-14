import { Flex } from "@chakra-ui/react";
import ListMovies from "../components/ListMovies/ListMovies";

export default function Home() {
	return (
		<Flex justifyContent={'center'} alignItems={'center'} grow={1}>
			<ListMovies />
		</Flex>
	);
}

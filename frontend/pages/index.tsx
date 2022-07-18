import { Flex } from "@chakra-ui/react";
import LoginComponent from "../components/Login";

export default function Home() {
	return (
		<Flex justifyContent={'center'} alignItems={'center'} grow={1}>
			<LoginComponent />
		</Flex>
	);
}

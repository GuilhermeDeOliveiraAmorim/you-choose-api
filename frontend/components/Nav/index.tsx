import { Box, Center, Flex, Square, Text } from "@chakra-ui/react";

export default function Nav() {
    return (
        <Flex color='white'>

            <Center flex='2' bg='green.500'>

                <Text>Box 1</Text>

            </Center>

            <Box flex='2' bg='tomato'>

                <Text>Box 3</Text>

            </Box>

        </Flex>
    )
}
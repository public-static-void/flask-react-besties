import { Stack, Container, Text } from "@chakra-ui/react";
import Navbar from "./components/Navbar";
import UserGrid from "./components/UserGrid";

function App() {
  return (
    <>
      <Stack minH={"100vh"}>
        <Navbar />

        <Container maxW={"1200px"} my={4}>
          <Text
            fontSize={{ base: "3xl", md: "50" }}
            fontWeight="bold"
            letterSpacing={2}
            textTransform={"uppercase"}
            textAlign={"center"}
            mb={8}
          >
            <Text
              as={"span"}
              bgGradient={"linear(to-r, cyan.400, green.400)"}
              bgClip={"text"}
            >
              My BESTIES
            </Text>
          </Text>
          <UserGrid />
        </Container>
      </Stack>
    </>
  );
}

export default App;

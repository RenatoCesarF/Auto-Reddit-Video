import { useState } from 'react';

import {
  Text,
  Heading,
  Box,
  Flex,
  Tooltip,
  useColorMode,
} from '@chakra-ui/react';

import { ChatIcon } from '@chakra-ui/icons';

import ThemedBox from './ThemedBox';
import UpvoteBar from './UpvoteBar';
import ChakraMarkdown from './ChakraMarkdown';

interface PostInterface{
  subreddit: string,
  author: string,
  title: string,
  body: string,
  numVotes: number,
  numComments:number,
}

const Post = ({
  subreddit,
  author,
  title,
  body,
  numVotes,
  numComments,
}: PostInterface) => {
  const { colorMode } = useColorMode();
  const postDetailColor = 'gray.500';
  const postDetailBgColor = colorMode === 'light' ? 'gray.100' : 'gray.600';
  const deletedText = '[deleted]';
  return (
    <ThemedBox
      p={4}
      borderRadius="md"
      width="100%"
      light="gray.50"
      dark="gray.700"
    >
      <Flex>
        <UpvoteBar
          type="post"
          numVotes={numVotes}
        />
        <Box flexGrow={1}>
          <Text            
            color={postDetailColor}
            fontWeight="bold"
          >
            {`r/${subreddit}`}
          </Text>{' '}
          <Text as="span" color={postDetailColor}>
            {`Posted by `}
          </Text>
          <Text as="span">{author ? `u/${author}` : deletedText}</Text>
          <Text as="span" color={postDetailColor}>
            {' '}
          </Text>
          <Heading
            display="block"
            mt={2}
            mb={4}
            fontSize="1.5em"
            fontWeight="500"
          >
            {title || deletedText}
          </Heading>
            <Box listStylePosition="inside">
              <ChakraMarkdown>{body}</ChakraMarkdown>
            </Box>
          <Flex
            mt={3}
            alignItems="center"
            color={postDetailColor}
            fontWeight="bold"
          >
            <Box
              p={2}
              borderRadius="sm"
              _hover={{ backgroundColor: postDetailBgColor }}
            >
              <ChatIcon mr={2} />
              {numComments} {numComments === 1 ? 'comment' : 'comments'}
            </Box>
          </Flex>
        </Box>
      </Flex>
    </ThemedBox>
  );
};

export default Post
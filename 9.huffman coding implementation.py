import heapq
import os

class BinaryTreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

class HuffmanCoding:

    def __int__(self, path):
        self.path = path
        self.__heap = []
        self.__codes = {}

    def __make_frequency_dict(self, text):
        freq_dict = {}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1
        return freq_dict

    def __buildHeap(self, freq_dict):
        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = BinarytreeNode(key, frequency)
            heapq.heappush(self.__heap, binary_tree_node)
            
    def __buildTree(self):
        while(len(self.__heap) > 1):
            binary_tree_node_1 = heapq.heappop(self.__heap)
            binary_tree_node_2 = heapq.heappop(self.__heap)
            freq_sum = binary_tree_node_1.freq + binary_tree_node_2.freq
            newNode = BinaryTreeNode(None, freq_sum)
            newNode.left = binary_tree_node_1
            newNode.right = binary_tree_node_2
            heapq.heappush(self.__heap, newNode)
        return

    def __buildCodesHelper(self, root, curr_bits):

        if root is None:
            return

        if root.value is not None:
            self.__codes[root.value] = curr_bits
            return
            
        self.__buildCodesHelper(self, root.left, curr_bits + "0")
        self.__buildCodesHelper(self, root.right, curr_bits + "1")

    def __buildCodes(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root, "")

    def __getEncodedText(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.__codes[char]
        return encoded_text

    def __getPaddedEncodedText(self, encoded_text):
        padded_amount = 8 - (len(encoded_text)%)

        for i in range(padded_amount):
            encoded_text += '0'

        padded_info = {"0:08b"}.format(padded_amount)
        padded_encoded_text = padded_info + encoded_text
        return padded_encoded_text

    def __getBytesArray(self, padded_encoded_text):
        array = []
        
        for i in range(len(padded_encoded_text)):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte, 2))
            
        return array        
    
    def compress(self):
        
        file_name, file_extension = os.path.splitext(self.path)
        output_path = file_name + ".bin"

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            # get file from path
            # read text from file
        
            text = file.read()
            text = text.rstrip()
        
            # step1: make frequency dictionary using the text

            freq_dict = self.__make_frequency_dict(text)
            
            # step2: construct the heap from the frequency_dict

            self.__buildHeap(freq_dict)
            
            # step3: construct the binary tree from the heap

            self.__buildTree()
            
            # step4: construct the codes from binary tree

            self.__buildCodes()
            
            # step5: creating the encoded text using the code

            encoded_text = self.__getEncodedText(text)
            
            # step6: put this encoded text into the binary file

            padded_encoded_text = self.__getPaddedEncodedText(text)

            bytes_array = self.__getBytesArray(padded_encoded_text)
            
            # step7: return this binary file as output
            final_bytes = bytes(bytes_array)
            output.write(final_bytes)

        print('Compressed')
        return output_path

    def __removePadding(self,text):
        padded_info = text[:8]
        extra_padding = int(padded_info,2)
        text = text[8:]
        text_after_padding_removed = text[:-1 * extra_padding]
        return text_after_padding_removed

    def __decodeText(self,Text):
        decode_text=""
        current_bits=""
        for bit in text:
            current_bits+=bit
            if current_bits in self.reverseCodes:
                character=self.__reverseCodes[current_bits]
                decoded_text=""
                current_bits=""
                
                for bit in text:
                    current_bits+=bit
                    if current_bits in self.__reverseCodes:
                        character=self.__reverseCodes[current_bits]
                        decoded_text+=character
                        current_bits=""
                    return decoded_text

    def decompress(self,input_path):
        filename,file_extension=os.path.splitext(self.path)
        output_path=filename + "_decompressed" + ".txt"
        with open(input_path,'rb') as file,open(output_path,'w')as output:
            bit_string=""
            byte=file.read(1)
            while byte:
                byte=ord(byte)
                bits=bin(byte)[2:].rjust(8,'0')
                bit_string+=bits
                byte=file.read(1)
            actual_text=self.__removePadding(bit_string)
            decompressed_text = self.__decodeText(actual_text)
            output.write(decompressed_text)

path = '/Users/dsa/desktop/sample.txt'
h = HuffmanCoding(path)
output_path = h.compress()
h.decompress(output_path)

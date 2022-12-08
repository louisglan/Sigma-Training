my_file =  open('characters.txt', 'r')
data = my_file.read()
def findMarker(string, packet_length):
    for i in range(len(string[packet_length-1:])):
        def isMatch(chars):
            check_list = []
            for j in range(packet_length):
                if chars[j] not in check_list:
                    check_list.append(chars[j])
            if len(check_list) == packet_length:
                return True
        chars = string[i:i+packet_length]
        if isMatch(chars):
            return i+packet_length
print(findMarker(data, 14))